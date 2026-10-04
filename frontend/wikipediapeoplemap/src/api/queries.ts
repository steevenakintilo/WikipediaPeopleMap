import { queryOptions, type QueryKey } from "@tanstack/react-query"

import { api_fetch } from "./client.ts"
import { query_client } from "./query_client.ts"

// Chaque requête est identifiée par sa queryKey : même clé = même entrée dans le cache.
// Les filtres de recherche font partie de la clé, donc une recherche déjà faite
// (ou une page déjà vue) s'affiche instantanément.

export const RANDOM_CHUNK = 999999999

// Liste affichée sur la carte : une page de la liste complète (search null) ou d'une recherche avancée.
// La page aléatoire reçoit un random_id différent à chaque clic : jamais servie depuis le cache.
export function user_list_query(request: { chunk: number, search: any, random_id?: number }) {
  return queryOptions({
    queryKey: ["users", "list", request],
    queryFn: () => request.search === null
      ? api_fetch(`/display_chunck_of_user_info/${request.chunk}`)
      : api_fetch(`/display_chunck_of_user_info_advanced_search/${request.chunk}/`, { method: "POST", body: request.search }),
    ...(request.random_id === undefined ? {} : { gcTime: 0 }),
  })
}

export function user_info_query(user: string) {
  return queryOptions({
    queryKey: ["users", "info", user],
    queryFn: () => api_fetch(`/display_user_info/${user}`),
    // Jamais servie depuis le cache : chaque ouverture appelle le backend (compteur de vues, statut des signalements)
    staleTime: 0,
  })
}

export function advanced_statistics_query(search: any) {
  return queryOptions({
    queryKey: ["statistics", "advanced", search],
    queryFn: () => api_fetch("/get_advanced_statistics", { method: "POST", body: search }),
  })
}

export function other_statistics_query() {
  return queryOptions({
    queryKey: ["statistics", "other"],
    queryFn: () => api_fetch("/get_other_statistics"),
  })
}

// Génère un fichier à télécharger : c'est une action (useMutation), pas une donnée à mettre en cache
export function download_qjis_csv(search: any): Promise<Blob> {
  return api_fetch("/display_chunck_of_user_info_advanced_search_qjis", { method: "POST", body: search, response_type: "blob" })
}

// Relancer une recherche identique répond depuis le cache, sauf si sa dernière
// tentative a échoué : dans ce cas on refait l'appel
export function retry_if_failed(query_key: QueryKey) {
  query_client.refetchQueries({
    queryKey: query_key,
    exact: true,
    predicate: (query) => query.state.status === "error",
  })
}

// Signalement d'une fiche : la personne + les champs (noms du modèle Django WikipediaUser) à vérifier
export type ReportableField =
  | "picture_url" | "birth_date" | "death_date" | "is_alive" | "gender" | "age" | "job"
  | "town_birth_place" | "country_birth_place" | "continent_of_birth" | "region_of_birth"
  | "town_death_place" | "country_death_place" | "continent_of_death" | "region_of_death" | "time_period_of_birth"

// username = page_name de la personne (même identifiant que la route display_user_info/<username>)
export type UserInfoReport = { username: string, fields: ReportableField[] }

export function update_user_info_status(report: UserInfoReport) {
  return api_fetch("/update_user_info_status", { method: "POST", body: report })
}
