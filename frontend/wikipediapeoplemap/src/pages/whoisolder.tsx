import { BLACK_BUTTON } from "../utils/styles.ts"
import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { CircleCheckIcon, GamepadIcon, SearchXIcon, SlidersHorizontalIcon } from "lucide-react";
import { Alert, AlertDescription, AlertTitle, Badge, Button, Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle, Spinner } from "@steevenakintilo/ui";

import { ApiError } from "../api/client.ts"
import { create_who_was_born_first_game } from "../api/queries.ts"
import { ActiveFilters, AdvancedSearchDialog } from "../components/advanced_search.tsx";
import { count_active_filters, GAME_FILTERS } from "../components/advanced_search_config.ts";
import { ErrorState, LoadingState, PageHeader, TooMuchRequestError } from "../components/page.tsx";

const EARTH_GIF = "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790349009/earth_qha8vm.gif"

const WhoIsOlder = () => {
    const [dict_of_advance_search,set_dict_of_advance_search] : any = useState({})
    const [filters_open,set_filters_open] = useState(false)

    // L'appel API passe par TanStack Query (mutation : génère un fichier, rien à mettre en cache)
    
    
    const game_loading = useMutation({
      mutationFn: create_who_was_born_first_game,
    })

    const [round_nb,set_round_nb] = useState(0)
    const [number_of_tries_left,set_number_of_tries_left] = useState(3)
    const [feedback,set_feedback] = useState<{success: boolean, text: string} | null>(null)
    const loading = game_loading.isPending
    const all_game_data : any[] = game_loading.data?.all_game_data ?? []
    const current_round = all_game_data[round_nb]
    const is_last_round = round_nb >= all_game_data.length - 1
    const has_lost = number_of_tries_left <= 0
    const has_won = feedback?.success === true && is_last_round
    const no_result_found = (game_loading.error instanceof ApiError && game_loading.error.status == 404)
      || (game_loading.isSuccess && all_game_data[0]?.page_name === "personne")
    const server_error_found = game_loading.isError && !no_result_found
    var error_type = 0
    if (server_error_found) {
      error_type = 1
    }
    if (game_loading.error?.toString() === "ApiError: Erreur HTTP 429") {
      error_type = 2;
    }

    const active_filters_count = count_active_filters(GAME_FILTERS, dict_of_advance_search)
    
    function reset_game() {
        set_round_nb(0)
        set_number_of_tries_left(3)
        set_feedback(null)
    }

    // choice : 1 = première personne, 2 = deuxième personne
    function validate_choice(choice:1|2) {
        if (feedback || has_lost || !current_round) return
        const year_1 = Number(current_round.birth_year)
        const year_2 = Number(current_round.birth_year2)

        if (year_1 === year_2) {
            set_feedback({
                success: true,
                text: `Réussi ! ${current_round.page_name} et ${current_round.page_name2} ont le même âge (nés en ${year_1}).`,
            })
            return
        }

        const first_is_older = year_1 < year_2
        const older_name = first_is_older ? current_round.page_name : current_round.page_name2
        const older_year = first_is_older ? year_1 : year_2
        const younger_name = first_is_older ? current_round.page_name2 : current_round.page_name
        const younger_year = first_is_older ? year_2 : year_1
        const younger_sentence = `${younger_name} est né(e) en ${younger_year}.`
        const is_correct = (choice === 1) === first_is_older

        if (is_correct) {
            set_feedback({ success: true, text: `Réussi ! ${older_name} est la personne la plus âgée (née en ${older_year}). ${younger_sentence}` })
        } else {
            set_number_of_tries_left(number_of_tries_left - 1)
            set_feedback({ success: false, text: `Raté ! ${older_name} est la personne la plus âgée (née en ${older_year}). ${younger_sentence}` })
        }
    }

    function next_round() {
        set_round_nb(round_nb + 1)
        set_feedback(null)
    }

    function get_list_of_user_advanced_search() {
      set_filters_open(false)
      reset_game()
      game_loading.mutate(dict_of_advance_search)
    }

    // if (loading) {
    //     console.log("game_loading " , game_loading.data.all_game_data)
    // }

   return (
    <main className="mx-auto w-full max-w-3xl flex-1 space-y-6 px-4 py-10">
      
      
      {/* {game_loading.isSuccess != true &&(

      )}
       */}

        {game_loading.isSuccess == false &&(
            
            <PageHeader
                title="Qui est né avant?"
                description="Jeu simple où vous allez avoir une série de personnes (2 par round) et où vous devrez deviner qui est né avant qui."
            />

        )}
      <div className="space-y-6 md:block">
        <Card>
          <CardHeader>
            <CardTitle>Personnes à exporter</CardTitle>
            <CardDescription>
              {active_filters_count === 0
                ? "Aucun filtre : le jeu contiendra toutes les personnes."
                : "Le jeu contiendra les personnes correspondant à ces filtres."}
            </CardDescription>
          </CardHeader>
          {active_filters_count > 0 && (
            <CardContent>
              <ActiveFilters sections={GAME_FILTERS} filters={dict_of_advance_search} set_filters={set_dict_of_advance_search} />
            </CardContent>
          )}
          <CardFooter className="flex-wrap gap-2">
            <Button variant="outline" onClick={() => set_filters_open(true)}>
              <SlidersHorizontalIcon /> Filtres avancés
              {active_filters_count > 0 && <Badge className="ml-1">{active_filters_count}</Badge>}
            </Button>
            <Button className={BLACK_BUTTON} onClick={() => get_list_of_user_advanced_search()} disabled={loading}>
              {loading ? <Spinner /> : <GamepadIcon />} Générer une partie
            </Button>
          </CardFooter>
        </Card>

        {loading && <LoadingState title="Génération de la partie…" />}

        {error_type == 1 &&(
            <ErrorState on_retry={() => game_loading.mutate()} />
        )}
              
        {error_type == 2 &&(
          <TooMuchRequestError description="Tu as fait trop de requêtes, patiente 15 minutes." on_retry={() => game_loading.mutate()} />
        )}
        

        {!loading && no_result_found && (
          <Alert>
            <SearchXIcon />
            <AlertTitle>Aucun résultat</AlertTitle>
            <AlertDescription>Aucune page Wikipédia ne correspond à ces filtres : essayez-en d'autres.</AlertDescription>
          </Alert>
        )}
        
        {/* //   <Alert>
        //     <CircleCheckIcon />
        //     <AlertTitle>La partie va commencer</AlertTitle>
        //     <AlertDescription>TOTO.</AlertDescription>
        //   </Alert>
         */}
      </div>
      
      
      
      {game_loading.isSuccess &&(
            <PageHeader
                title="Qui est le plus agé?"
            />
        )}


      {!loading && game_loading.isSuccess && !no_result_found && current_round && (
        <Card className="w-full max-w-2xl mx-auto">
            <CardHeader>
                <CardTitle>
                Round: {round_nb + 1}/{all_game_data.length}
                </CardTitle>
                <CardTitle>
                Nombre d'essais restants : {number_of_tries_left}
                </CardTitle>
            </CardHeader>
            <CardContent className="space-y-6 pt-6">
                {has_lost ? (
                  <Alert variant="destructive">
                    <AlertTitle>Tu as perdu</AlertTitle>
                    <AlertDescription>{feedback?.text}</AlertDescription>
                  </Alert>
                ) : (
                  <>
                    <p className="text-center text-sm text-muted-foreground">Qui est la personne la plus âgée ?</p>
                    <div className="grid grid-cols-2 gap-4 w-full justify-items-center">
                      {([1, 2] as const).map((choice) => {
                        const name = choice === 1 ? current_round.page_name : current_round.page_name2
                        const picture_url = choice === 1 ? current_round.picture_url : current_round.picture_url2
                        return (
                          <div key={choice} className="flex flex-col items-center gap-4 w-full max-w-[400px] h-[400px]">
                            <Button variant="outline" disabled={feedback !== null} onClick={() => validate_choice(choice)}>
                              {name}
                            </Button>
                            <img
                              src={decodeURIComponent(decodeURIComponent(picture_url))}
                              className={`max-w-full max-h-full object-contain ${feedback === null ? "cursor-pointer" : ""}`}
                              onClick={() => validate_choice(choice)}
                            />
                          </div>
                        )
                      })}
                    </div>
                    {feedback && (
                      <Alert variant={feedback.success ? "default" : "destructive"}>
                        <AlertTitle>{feedback.success ? "Bravo" : "Raté"}</AlertTitle>
                        <AlertDescription>{feedback.text}</AlertDescription>
                      </Alert>
                    )}
                    {has_won && (
                      <Alert>
                        <CircleCheckIcon />
                        <AlertTitle>Partie terminée</AlertTitle>
                        <AlertDescription>Tu as terminé tous les rounds, bravo !</AlertDescription>
                      </Alert>
                    )}
                  </>
                )}
            </CardContent>
            <CardFooter className="gap-2">
                {!has_lost && feedback && !is_last_round && (
                  <Button className={BLACK_BUTTON} onClick={() => next_round()}>Round suivant</Button>
                )}
                {/* {(has_lost || has_won) && (
                  <Button className={BLACK_BUTTON} onClick={() => reset_game()}>Recommencer</Button>
                )}
                 */}
            </CardFooter>
        </Card>
        )}
      <AdvancedSearchDialog
        open={filters_open}
        on_open_change={set_filters_open}
        sections={GAME_FILTERS}
        filters={dict_of_advance_search}
        set_filters={set_dict_of_advance_search}
        on_search={() => get_list_of_user_advanced_search()}
        search_label="Générer une partie"
      />
    </main>

  );
};

export default WhoIsOlder;
