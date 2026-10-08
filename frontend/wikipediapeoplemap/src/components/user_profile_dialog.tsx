import { useImperativeHandle, useState, type ReactNode, type Ref } from "react"
import { useQuery } from "@tanstack/react-query"
import { CircleCheckIcon , ExternalLinkIcon, TriangleAlertIcon } from "lucide-react"
import {
  Alert,
  AlertDescription,
  Button,
  cn,
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  Separator,
  Skeleton,
} from "@steevenakintilo/ui"

import { NUMBER_OF_USER } from "../utils/global_variable.tsx"
import { ErrorState } from "./page.tsx"
import { ReportButton } from "./report_dialog.tsx"
import { user_info_query } from "../api/queries.ts"
import { validate_an_user } from "../api/queries.ts"
import { query_client } from "../api/query_client.ts"
import {voted_users} from "../utils/global_variable.tsx"

const GRAY_BUTTON = "bg-gray-300 text-gray-800 hover:bg-gray-400";

const gender_to_french_dict : any = {
  "Man":"Homme",
  "Woman":"Femme",
  "Unclear":"Non précisé"
}

// Texte affiché selon update_level (backend) ; les autres valeurs n'affichent rien
const UPDATE_LEVEL_TEXT: Record<number, string> = {
  1: "Page vérifiée et validée.",
  2: "Page vérifiée et validée, mais la personne a pu prendre un an de plus ou mourir depuis.",
  4: "Page en cours de validation.",
}

const format_number =(value: any) => (typeof value === "number" ? value.toLocaleString("fr-FR") : value)

// "Vivant", "Décédée"… accordé selon le genre quand il est connu
function status_of(user_data_info: any) {
  const dead = !user_data_info.is_alive
  if (user_data_info.gender === "Man") {
    return dead ? "Décédé" : "Vivant"
  }
  if (user_data_info.gender === "Woman") {
    return dead ? "Décédée" : "Vivante"
  }
  return dead ? "Décédé(e)" : "Vivant(e)"
}

// Une information principale de la fiche : libellé au-dessus, valeur en gras
function KeyFact({ label, className, children }: { label: string, className?: string, children: ReactNode }) {
  return (
    <div className={cn("rounded-lg border px-3 py-2", className)}>
      <dt className="text-xs text-muted-foreground">{label}</dt>
      <dd className="font-medium text-pretty">{children}</dd>
    </div>
  )
}

function InfoRow({ label, children }: { label: string, children: ReactNode }) {
  return (
    <div className="flex justify-between gap-4 py-1.5 text-sm">
      <dt className="text-muted-foreground">{label}</dt>
      <dd className="text-right font-medium">{children}</dd>
    </div>
  )
}

function Section({ title, children }: { title: string, children: ReactNode }) {
  return (
    <section className="rounded-xl border p-4">
      <h3 className="mb-1 text-sm font-semibold">{title}</h3>
      <dl className="divide-y">{children}</dl>
    </section>
  )
}

function TopList({ title, items }: { title: string, items: any[] | undefined }) {
  if (items === undefined || items.length === 0) {
    return null
  }

  return (
    <div className="pt-2">
      <p className="mb-1 text-xs text-muted-foreground">{title} (top {items.length})</p>
      <ol className="list-inside list-decimal space-y-0.5 text-sm">
        {items.map((item: any, i: number) => (
          <li key={i}>{item}</li>
        ))}
      </ol>
    </div>
  )
}

function check_validate_vote(user:string,id:number) {
  if (voted_users.has(id) == false) {
    validate_an_user(user)
    voted_users.add(id);
    localStorage.setItem(
      "votedUsers",
      JSON.stringify([...voted_users])
    );
  }
}
function has_complete_date(week_day: string, day: string, year: number) {
  return week_day != "Indéfini" && day != "Indéfini" && year != 123456789
}

function ProfileContent({ user_data_info }: { user_data_info: any }) {
  return (
    <div className="space-y-4">
      {/* Grande photo carrée, et les informations principales juste en dessous */}
      <div className="flex flex-col items-center gap-4">
         <img
            src={decodeURIComponent(
              decodeURIComponent(user_data_info.picture_url)
            )}
            style={{ cursor: "pointer" }}
            alt=""
            width="200"
            height="200"
            className="me-2"
          />
        <dl className="grid w-full max-w-lg grid-cols-3 gap-2 text-center">
          <KeyFact label="Statut">{status_of(user_data_info)}</KeyFact>
          <KeyFact label="Genre">{gender_to_french_dict[user_data_info.gender] ?? "Non précisé"}</KeyFact>
          <KeyFact label={user_data_info.is_alive ? "Âge" : "Âge au décès"}>
            {user_data_info.age > 0 ? `${user_data_info.age} ans` : "Inconnu"}
          </KeyFact>
          <KeyFact label="Métier" className="col-span-3">{user_data_info.job || "Non précisé"}</KeyFact>
          <KeyFact label="Nombre de vue sur le site" className="col-span-3">{format_number(user_data_info.number_of_views + 1)}</KeyFact>
          {UPDATE_LEVEL_TEXT[user_data_info.update_level] && (
            <KeyFact label="Vérification de la page" className="col-span-3">{UPDATE_LEVEL_TEXT[user_data_info.update_level]}</KeyFact>
          )}
          
        </dl>
        <Button variant="outline" size="sm" asChild>
          <a href={user_data_info.page_url} target="_blank" rel="noopener noreferrer">
            <ExternalLinkIcon /> Voir sur Wikipédia
          </a>
        </Button>
        
        {(user_data_info.update_level == 3) && voted_users.has(user_data_info.id) == false &&(
          <Button size="sm" className={GRAY_BUTTON} onClick={() => check_validate_vote(user_data_info.page_name,user_data_info.id)}>
            <CircleCheckIcon /> Valider les informations de la personne
          </Button>
          
        )}
        
        {(user_data_info.update_level == 2 || user_data_info.update_level == 3) && (
          <ReportButton user={user_data_info} />
        )}
        
      </div>

      {user_data_info.age >= 110 && user_data_info.is_alive == true && (user_data_info.update_level == 3 || user_data_info.update_level == 4) && (
        <Alert>
          <TriangleAlertIcon />
          <AlertDescription>
            Cette personne est probablement décédée : le site se trompe souvent pour les âges très élevés.
          </AlertDescription>
        </Alert>
      )}

      <div className="grid gap-3">
        <Section title="Naissance">
          <InfoRow label="Date">{user_data_info.birth_date}</InfoRow>
          {has_complete_date(user_data_info.week_day_of_birth, user_data_info.birth_day, user_data_info.birth_year) && (
            <InfoRow label="Date complète">
              {user_data_info.week_day_of_birth} {user_data_info.birth_day} {user_data_info.birth_month} {user_data_info.birth_year}
            </InfoRow>
          )}
          <InfoRow label="Lieu">
            {user_data_info.country_birth_place_emoji} {user_data_info.town_birth_place}, {user_data_info.country_birth_place}
          </InfoRow>
          <InfoRow label="Région du monde">{user_data_info.region_of_birth}</InfoRow>
          <InfoRow label="Continent">{user_data_info.continent_of_birth}</InfoRow>
          <InfoRow label="Période historique">{user_data_info.time_period_of_birth}</InfoRow>
        </Section>

        {!user_data_info.is_alive && (
          <Section title="Décès">
            {user_data_info.is_cause_of_death_known == true && (
              <InfoRow label="Cause">{user_data_info.cause_of_death}</InfoRow>
            )}
            <InfoRow label="Date">{user_data_info.death_date}</InfoRow>
            {has_complete_date(user_data_info.week_day_of_death, user_data_info.death_day, user_data_info.death_year) && (
              <InfoRow label="Date complète">
                {user_data_info.week_day_of_death} {user_data_info.death_day} {user_data_info.death_month} {user_data_info.death_year}
              </InfoRow>
            )}
            <InfoRow label="Lieu">
              {user_data_info.country_death_place_emoji} {user_data_info.town_death_place}, {user_data_info.country_death_place}
            </InfoRow>
            <InfoRow label="Région du monde">{user_data_info.region_of_death}</InfoRow>
            <InfoRow label="Continent">{user_data_info.continent_of_death}</InfoRow>
          </Section>
        )}

        <Section title="Classement">
          <InfoRow label="Position">{format_number(user_data_info.position + 1)} / {format_number(NUMBER_OF_USER)}</InfoRow>
          <InfoRow label="Score">{user_data_info.power_ranking}</InfoRow>
          <InfoRow label="Note">{user_data_info.grade_over_20} / 20</InfoRow>
          <InfoRow label="Position en %">top {user_data_info.position_percentage} % des meilleures pages</InfoRow>
        </Section>

        <Section title="Précision des données">
          <InfoRow label="Niveau de précision">{user_data_info.preciseness_level} / 100</InfoRow>
          <InfoRow label="Éléments non trouvés sur la page">{user_data_info.number_of_unpreciseness_date}</InfoRow>
          {user_data_info.list_of_unpreciseness_data?.length > 0 && (
            <div className="pt-2">
              <p className="mb-1 text-xs text-muted-foreground">Erreurs sur la page</p>
              <ul className="list-inside list-disc space-y-0.5 text-sm">
                {user_data_info.list_of_unpreciseness_data.map((error: any, i: number) => (
                  <li key={i}>{error}</li>
                ))}
              </ul>
            </div>
          )}
        </Section>
      </div>

      <Section title="Page Wikipédia">
        <InfoRow label="Longueur de la page">{format_number(user_data_info.wikipedia_page_length)} caractères</InfoRow>
        <InfoRow label="Nombre de liens">{format_number(user_data_info.number_of_links)}</InfoRow>
        <InfoRow label="Personnes qui la mentionnent">{format_number(user_data_info.number_of_user_who_have_linked_this_user)}</InfoRow>
        <InfoRow label="Ami(e)s (mentions dans les deux sens)">{format_number(user_data_info.number_of_friends)}</InfoRow>
        <InfoRow label="Nombre de langues dans lesquelles la page est traduite">{format_number(user_data_info.nb_of_translation)}</InfoRow>
        
        <div className="grid gap-x-6">
          <TopList title="Liens sur sa page" items={user_data_info.all_links_of_a_page} />
          <TopList title="Personnes qui la mentionnent" items={user_data_info.list_of_page_name_linked_sorted} />
          <TopList title="Ami(e)s" items={user_data_info.list_of_friend_of_user} />
        </div>
      </Section>
    </div>
  )
}

function ProfileSkeleton() {
  return (
    <div className="space-y-4" aria-busy="true">
      <div className="flex flex-col items-center gap-4">
        <Skeleton className="size-[250px] max-w-full rounded-none" />
        <div className="grid w-full max-w-lg grid-cols-3 gap-2">
          <Skeleton className="h-14 rounded-lg" />
          <Skeleton className="h-14 rounded-lg" />
          <Skeleton className="h-14 rounded-lg" />
          <Skeleton className="col-span-3 h-14 rounded-lg" />
        </div>
      </div>
      <Separator />
      <div className="grid gap-3">
        <Skeleton className="h-40 rounded-xl" />
        <Skeleton className="h-40 rounded-xl" />
      </div>
    </div>
  )
}

type UserProfileDialogProps = {
  open: boolean
  on_open_change: (open: boolean) => void
  page_name: string
  user_info: { data: any, isLoading: boolean, isError: boolean, refetch: () => unknown }
}

export function UserProfileDialog({ open, on_open_change, page_name, user_info }: UserProfileDialogProps) {
  return (
    // Non modale : avec 500 lignes et 500 cercles sur la carte, le mode modal de Radix
    // (blocage du défilement, masquage du reste de la page) faisait ramer l’ouverture.
    // Le fond sombre est un simple div, qui ferme la fiche au clic comme l’ancienne modale.
    <>
    {open && <div aria-hidden="true" className="fixed inset-0 z-50 bg-black/40" onClick={() => on_open_change(false)} />}
    <Dialog open={open} onOpenChange={on_open_change} modal={false}>
      <DialogContent className="max-h-[90dvh] overflow-y-auto sm:max-w-3xl">
        <DialogHeader>
          <DialogTitle className="pr-8 text-xl">{user_info.data?.page_name ?? page_name}</DialogTitle>
          <DialogDescription>
          
          <strong>ATTENTION: Le site peut se tromper.</strong>
            
          </DialogDescription>
        </DialogHeader>

        {user_info.isLoading && <ProfileSkeleton />}
        {user_info.isError && <ErrorState description="Impossible de charger ce profil pour le moment." on_retry={() => user_info.refetch()} />}
        {!user_info.isError && user_info.data && <ProfileContent user_data_info={user_info.data} />}

      </DialogContent>
    </Dialog>
    </>
  )
}

// Fiche autonome : garde elle-même son état (personne affichée, ouverture, chargement).
// La page Carte appelle seulement ref.current.open(nom) : ouvrir la fiche ne re-rend pas la carte.
export type ProfileHostHandle = { open: (page_name: string) => void }

export function ProfileHost({ ref }: { ref: Ref<ProfileHostHandle> }) {
  const [page_name, set_page_name] = useState("")
  const [open, set_open] = useState(false)
  const user_info = useQuery({
    ...user_info_query(page_name),
    enabled: page_name != "",
  })

  useImperativeHandle(ref, () => ({
    open: (name: string) => {
      set_page_name(name)
      set_open(true)
      // Nouvel appel à chaque ouverture, même pour une fiche déjà consultée
      query_client.invalidateQueries({ queryKey: user_info_query(name).queryKey })
    },
  }), [])

  return <UserProfileDialog open={open} on_open_change={set_open} page_name={page_name} user_info={user_info} />
}
