import {
  MapContainer,
  TileLayer,
  CircleMarker,
  Polyline,
  useMap,
  useMapEvents,
} from "react-leaflet";

import { useEffect, useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { GamepadIcon, MapPinIcon, SearchXIcon, SlidersHorizontalIcon, TrophyIcon } from "lucide-react";
import { Alert, AlertDescription, AlertTitle, Badge, Button, Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle, Spinner } from "@steevenakintilo/ui";

import { BLACK_BUTTON } from "../utils/styles.ts"
import { ApiError } from "../api/client.ts"
import { create_wiki_birth_guessr_game } from "../api/queries.ts"
import { ActiveFilters, AdvancedSearchDialog } from "../components/advanced_search.tsx";
import { count_active_filters, GAME_FILTERS_WIKIGUESSR } from "../components/advanced_search_config.ts";
import { ErrorState, LoadingState, PageHeader, TooMuchRequestError } from "../components/page.tsx";
import { PersonPicture } from "../components/person_picture.tsx";

// Coordonnée renvoyée par le backend quand le lieu est inconnu
const UNKNOWN_LOCATION = 999999999999999
const DEFAULT_NUMBER_OF_ROUNDS = 5
const MAX_SCORE_PER_ROUND = 2000
// Distance (km) à laquelle le score est divisé par e : ~1000 km donne encore ~1000 points
const SCORE_DECAY_KM = 1500
const EARTH_RADIUS_KM = 6371

const GUESS_COLOR = "#2563eb"
const ANSWER_COLOR = "#16a34a"

type LatLng = [number, number]
type Difficulty = "easy" | "normal" | "hard"

// Indices affichés avant la validation : facile = pays + continent, normal = continent, difficile = rien
const DIFFICULTIES: { id: Difficulty, label: string, description: string }[] = [
  { id: "easy", label: "Facile", description: "Le pays et le continent de naissance sont affichés." },
  { id: "normal", label: "Normal", description: "Seul le continent de naissance est affiché." },
  { id: "hard", label: "Difficile", description: "Aucun indice : uniquement le nom et la photo." },
]

function is_known_location(localisation: any) {
  return Array.isArray(localisation)
    && localisation[0] !== UNKNOWN_LOCATION && localisation[1] !== UNKNOWN_LOCATION
}

// Le backend envoie soit [lat, lon], soit du texte "37° 29′ 37′′ N, 94° 16′ 20′′ W"
const DMS_PATTERN = /(\d+(?:\.\d+)?)\D+(\d+(?:\.\d+)?)\D+(\d+(?:\.\d+)?)\D*([NS])\D+(\d+(?:\.\d+)?)\D+(\d+(?:\.\d+)?)\D+(\d+(?:\.\d+)?)\D*([EW])/i

function parse_localisation(localisation: any): LatLng | null {
  if (is_known_location(localisation)) return [Number(localisation[0]), Number(localisation[1])]
  if (typeof localisation !== "string") return null
  const match = DMS_PATTERN.exec(localisation)
  if (!match) return null
  const to_decimal = (degrees: string, minutes: string, seconds: string, hemisphere: string) => {
    const value = Number(degrees) + Number(minutes) / 60 + Number(seconds) / 3600
    return /[SW]/i.test(hemisphere) ? -value : value
  }
  return [to_decimal(match[1], match[2], match[3], match[4]), to_decimal(match[5], match[6], match[7], match[8])]
}

// Distance à vol d'oiseau (formule de haversine)
function distance_in_km(a: LatLng, b: LatLng) {
  const to_rad = (degrees: number) => degrees * Math.PI / 180
  const d_lat = to_rad(b[0] - a[0])
  const d_lon = to_rad(b[1] - a[1])
  const h = Math.sin(d_lat / 2) ** 2 + Math.cos(to_rad(a[0])) * Math.cos(to_rad(b[0])) * Math.sin(d_lon / 2) ** 2
  return 2 * EARTH_RADIUS_KM * Math.asin(Math.sqrt(h))
}

// Score de 0 à 2000 : décroissance exponentielle avec la distance
function score_of_distance(distance_km: number) {
  return Math.round(MAX_SCORE_PER_ROUND * Math.exp(-distance_km / SCORE_DECAY_KM))
}

function format_distance(distance_km: number) {
  return distance_km < 10 ? `${distance_km.toFixed(1)} km` : `${Math.round(distance_km).toLocaleString("fr-FR")} km`
}

// Le backend renvoie parfois une URL à la place de l'emoji : on ne garde que le vrai emoji
function emoji_of(round: any) {
  const emoji = round.birth_place_emoji
  return typeof emoji === "string" && !emoji.startsWith("http") ? emoji : ""
}

function picture_of(round: any) {
  return decodeURIComponent(decodeURIComponent(round.picture_url))
}

// Un clic sur la carte place (ou déplace) le pin de réponse, tant que le round n'est pas validé
const ClickHandler = ({ on_pick, disabled }: { on_pick: (position: LatLng) => void, disabled: boolean }) => {
  useMapEvents({
    click(event) {
      if (!disabled) on_pick([event.latlng.lat, event.latlng.lng])
    },
  })
  return null
}

// Cadre la carte : monde entier au début de chaque round, puis les deux pins à la révélation.
// Placer ou déplacer le pin ne touche pas au zoom : l'effet de début de round ne dépend pas de guess.
const MapFramer = ({ guess, answer, round_key }: { guess: LatLng | null, answer: LatLng | null, round_key: number }) => {
  const map = useMap()

  useEffect(() => {
    map.setView([25, 10], 2)
  }, [round_key, map])

  useEffect(() => {
    if (answer && guess) {
      map.fitBounds([guess, answer], { padding: [60, 60], maxZoom: 8 })
    }
    // guess est figé une fois le round validé : seule la révélation (answer) déclenche le cadrage
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [answer, map])

  return null
}

const WikiBirthGuessr = () => {
  const [dict_of_advance_search, set_dict_of_advance_search]: any = useState({})
  const [filters_open, set_filters_open] = useState(false)

  const game_loading = useMutation({
    mutationFn: create_wiki_birth_guessr_game,
  })

  const [round_nb, set_round_nb] = useState(0)
  const [guess, set_guess] = useState<LatLng | null>(null)
  const [result, set_result] = useState<{ distance: number, score: number } | null>(null)
  const [scores, set_scores] = useState<number[]>([])
  // Choisie avant la partie, figée pendant celle-ci
  const [difficulty, set_difficulty] = useState<Difficulty>("normal")

  const loading = game_loading.isPending
  // Les personnes dont le lieu de naissance est inconnu ne peuvent pas être jouées
  // (le backend renvoie {} quand une erreur survient côté serveur)
  const received_rounds = game_loading.data?.all_game_data
  const all_game_data: any[] = Array.isArray(received_rounds)
    ? received_rounds
        .map((round: any) => ({ ...round, birth_town_localisation: parse_localisation(round.birth_town_localisation) }))
        .filter((round: any) => round.birth_town_localisation !== null)
    : []
  const current_round = all_game_data[round_nb]
  const is_last_round = round_nb >= all_game_data.length - 1
  const total_score = scores.reduce((sum, score) => sum + score, 0)
  const is_game_over = result !== null && is_last_round
  const game_started = game_loading.isSuccess && all_game_data.length > 0
  const answer: LatLng | null = result && current_round ? current_round.birth_town_localisation : null

  const no_result_found = (game_loading.error instanceof ApiError && game_loading.error.status == 404)
    || (game_loading.isSuccess && (all_game_data.length === 0 || all_game_data[0]?.page_name === "personne"))
  const server_error_found = game_loading.isError && !no_result_found
  const too_many_requests = game_loading.error?.toString() === "ApiError: Erreur HTTP 429"

  const active_filters_count = count_active_filters(GAME_FILTERS_WIKIGUESSR, dict_of_advance_search)

  function reset_game() {
    set_round_nb(0)
    set_guess(null)
    set_result(null)
    set_scores([])
  }

  function start_game() {
    set_filters_open(false)
    reset_game()
    game_loading.mutate({ number_of_rounds: DEFAULT_NUMBER_OF_ROUNDS, ...dict_of_advance_search })
  }

  function validate_guess() {
    if (!guess || result || !current_round) return
    const distance = distance_in_km(guess, current_round.birth_town_localisation)
    const score = score_of_distance(distance)
    set_result({ distance, score })
    set_scores([...scores, score])
  }

  function next_round() {
    set_round_nb(round_nb + 1)
    set_guess(null)
    set_result(null)
  }

  function render_setup() {
    return (
      <div className="space-y-6">
        <PageHeader
          title="Où est-il né ?"
          description={`Une personne Wikipédia s'affiche : placez un pin sur la carte à l'endroit où elle est née. Chaque round rapporte de 0 à ${MAX_SCORE_PER_ROUND} points selon votre précision.`}
        />
        <Card>
          {active_filters_count > 0 && (
            <CardContent>
              <ActiveFilters sections={GAME_FILTERS_WIKIGUESSR} filters={dict_of_advance_search} set_filters={set_dict_of_advance_search} />
            </CardContent>
          )}
          <CardContent className="space-y-2">
            <p className="text-sm font-medium">Difficulté</p>
            <div className="flex flex-wrap gap-2">
              {DIFFICULTIES.map((level) => (
                <Button
                  key={level.id}
                  variant={difficulty === level.id ? "default" : "outline"}
                  aria-pressed={difficulty === level.id}
                  onClick={() => set_difficulty(level.id)}
                >
                  {level.label}
                </Button>
              ))}
            </div>
            <p className="text-xs text-muted-foreground">{DIFFICULTIES.find((level) => level.id === difficulty)?.description}</p>
          </CardContent>
          <CardHeader>
            <CardDescription>
              {active_filters_count === 0
                ? `Aucun filtre : ${DEFAULT_NUMBER_OF_ROUNDS} personnes tirées au hasard.`
                : "La partie contiendra des personnes correspondant à ces filtres."}
            </CardDescription>
          </CardHeader>
          <CardFooter className="flex-wrap gap-2">
            <Button variant="outline" onClick={() => set_filters_open(true)}>
              <SlidersHorizontalIcon /> Filtres avancés
              {active_filters_count > 0 && <Badge className="ml-1">{active_filters_count}</Badge>}
            </Button>
            <Button className={BLACK_BUTTON} onClick={() => start_game()} disabled={loading}>
              {loading ? <Spinner /> : <GamepadIcon />} Générer une partie
            </Button>
          </CardFooter>
        </Card>

        {loading && <LoadingState title="Génération de la partie…" />}
        {server_error_found && !too_many_requests && <ErrorState on_retry={() => start_game()} />}
        {too_many_requests && (
          <TooMuchRequestError description="Tu as fait trop de requêtes, patiente 15 minutes." on_retry={() => start_game()} />
        )}
        {!loading && no_result_found && (
          <Alert>
            <SearchXIcon />
            <AlertTitle>Aucun résultat</AlertTitle>
            <AlertDescription>Pas assez de pages Wikipédia avec un lieu de naissance connu pour ces filtres : essayez-en d'autres.</AlertDescription>
          </Alert>
        )}
      </div>
    )
  }

  function render_round() {
    return (
      <Card className="w-full">
        <CardHeader>
          <CardTitle>Round {round_nb + 1}/{all_game_data.length}</CardTitle>
          <CardDescription>
            {DIFFICULTIES.find((level) => level.id === difficulty)?.label} · Score total : {total_score} / {MAX_SCORE_PER_ROUND * all_game_data.length}
          </CardDescription>
          <CardDescription>
            Mon site peut se tromper!
          </CardDescription>
          
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex flex-col items-center gap-3">
            <PersonPicture src={picture_of(current_round)} name={current_round.page_name} stretch className="size-[220px] [&_[data-slot=avatar-fallback]]:text-5xl" />
            <p className="text-center text-lg font-medium">{current_round.page_name}</p>
            {!result && difficulty !== "hard" && (
              <div className="flex flex-wrap justify-center gap-2">
                {difficulty === "easy" && (
                  <Badge variant="secondary">{emoji_of(current_round)} {current_round.country_of_birth}</Badge>
                )}
                <Badge variant="secondary">{current_round.continent_of_birth}</Badge>
              </div>
            )}
          </div>

          {!result && (
            <p className="text-center text-sm text-muted-foreground">
              {guess ? "Vous pouvez déplacer le pin avant de valider." : "Cliquez sur la carte pour deviner son lieu de naissance."}
            </p>
          )}

          {result && (
            <Alert>
              <MapPinIcon />
              <AlertTitle>{result.score} / {MAX_SCORE_PER_ROUND} points</AlertTitle>
              <AlertDescription>
                Vous étiez à {format_distance(result.distance)}. {current_round.page_name} est né(e) aux/en {current_round.country_of_birth} {emoji_of(current_round)} à {current_round.town_birth_place}  ({current_round.continent_of_birth}).
              </AlertDescription>
            </Alert>
          )}

          {is_game_over && (
            <Alert>
              <TrophyIcon />
              <AlertTitle>Partie terminée</AlertTitle>
              <AlertDescription>Score final : {total_score} / {MAX_SCORE_PER_ROUND * all_game_data.length}</AlertDescription>
            </Alert>
          )}
        </CardContent>
        <CardFooter className="gap-2">
          {!result && (
            <Button className={BLACK_BUTTON} onClick={() => validate_guess()} disabled={!guess}>
              <MapPinIcon /> Valider
            </Button>
          )}
          {result && !is_last_round && (
            <Button className={BLACK_BUTTON} onClick={() => next_round()}>Round suivant</Button>
          )}
          {is_game_over && (
            <Button className={BLACK_BUTTON} onClick={() => game_loading.reset()}>Nouvelle partie</Button>
          )}
        </CardFooter>
      </Card>
    )
  }

  return (
    <main className="flex h-[calc(100dvh-3.5rem)] min-h-0 flex-col md:flex-row">
      {/* isolate : les calques Leaflet restent sous les fenêtres (Dialog, Sheet…) */}
      <div className="relative isolate h-[45%] min-w-0 md:h-auto md:flex-1">
        <MapContainer
          minZoom={2}
          maxZoom={18}
          zoomControl={true}
          scrollWheelZoom={true}
          worldCopyJump={true}
          className="size-full"
          style={{ cursor: game_started && !result ? "crosshair" : undefined }}
        >
          <MapFramer guess={guess} answer={answer} round_key={round_nb} />
          <ClickHandler on_pick={set_guess} disabled={!game_started || result !== null} />
          <TileLayer
            attribution="&copy; Google Maps"
            url="https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
            subdomains={["mt0", "mt1", "mt2", "mt3"]}
          />

          {guess && (
            <CircleMarker center={guess} radius={10} pathOptions={{ fillColor: GUESS_COLOR, color: GUESS_COLOR, fillOpacity: 0.5 }} />
          )}
          {answer && (
            <CircleMarker center={answer} radius={10} pathOptions={{ fillColor: ANSWER_COLOR, color: ANSWER_COLOR, fillOpacity: 0.5 }} />
          )}
          {answer && guess && (
            <Polyline positions={[guess, answer]} pathOptions={{ color: "#6b7280", dashArray: "6 8", weight: 3 }} />
          )}
        </MapContainer>

        {result && (
          <div className="absolute bottom-3 left-3 z-[1000] flex items-center gap-3 rounded-md border bg-background/95 px-3 py-1.5 text-xs shadow-md">
            <span className="flex items-center gap-1"><span className="size-3 rounded-full" style={{ background: GUESS_COLOR }} /> Votre réponse</span>
            <span className="flex items-center gap-1"><span className="size-3 rounded-full" style={{ background: ANSWER_COLOR }} /> Lieu de naissance</span>
          </div>
        )}
      </div>

      <aside className="w-full min-h-0 flex-1 overflow-y-auto border-t p-4 md:w-[420px] md:flex-none md:border-t-0 md:border-l">
        {game_started && current_round ? render_round() : render_setup()}
      </aside>

      <AdvancedSearchDialog
        open={filters_open}
        on_open_change={set_filters_open}
        sections={GAME_FILTERS_WIKIGUESSR}
        filters={dict_of_advance_search}
        set_filters={set_dict_of_advance_search}
        on_search={() => start_game()}
        search_label="Générer une partie"
      />
    </main>
  );
};

export default WikiBirthGuessr;
