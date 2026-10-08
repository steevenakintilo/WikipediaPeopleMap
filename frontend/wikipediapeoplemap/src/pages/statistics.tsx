import { BLACK_BUTTON } from "../utils/styles.ts"
import { useState } from 'react';
import { keepPreviousData, useQuery } from '@tanstack/react-query';
import { SearchIcon, SlidersHorizontalIcon } from "lucide-react";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger, Badge, Button, Spinner } from "@steevenakintilo/ui";

import {LIST_OF_THEME} from '../utils/global_variable'
import {VAR_TO_DESCRIPTION,STAT_TO_DESCRIPTION,SUB_THEME_TO_THEME,LIST_OF_VARIABLE_THAT_NEED_COMPUTING} from "../utils/global_variable.tsx"
import { generate_list_of_dict , make_a_graphic ,generate_list_of_dict_with_a_lenght_limit,is_screen_for_mobile} from "../utils/utility_function.tsx";
import { advanced_statistics_query, retry_if_failed } from "../api/queries.ts";
import { ActiveFilters, AdvancedSearchDialog } from "../components/advanced_search.tsx";
import { count_active_filters, STATISTICS_FILTERS } from "../components/advanced_search_config.ts";
import { DataTableDialog } from "../components/data_table_dialog.tsx";
import { EmptyState, ErrorState, LoadingState, PageHeader,TooMuchRequestError } from "../components/page.tsx";
import { StatChartCard } from "../components/stat_chart.tsx";

const NO_DATA = {}
const NO_CHARTS = { list_of_graph: [], list_of_dict: [], list_of_keys_name: [] }

const format_number = (value: any) => (typeof value === "number" ? value.toLocaleString("fr-FR") : value)

// Construit les graphiques et les tableaux détaillés à partir des statistiques reçues
function build_charts(list_of_user_data: any) {
  const keys = Object.keys(list_of_user_data);

  const list_of_graph: any[] = [];
  const list_of_dict: any[] = [];
  const list_of_keys_name: string[] = [];

  let number_of_bar_to_display = 10;
  if (is_screen_for_mobile() == true) {
    number_of_bar_to_display = 3
  }

  for (let i = 0; i < keys.length - 1; i++) {

      const key = keys[i];

      if (list_of_user_data[key].length > 0) {

          list_of_keys_name.push(key);

          if (
              key !== "age" &&
              key !== "grade_over_20" &&
              key !== "wikipedia_page_lenght" &&
              key !== "preciseness_level" &&
              key !== "dict_of_error" &&
              key !== "number_of_error_per_page" &&
              key !== "age_group" &&
              key !== "birth_year" &&
              key !== "death_year" &&
              key !== "birth_and_death_year" &&
              key !== "birth_year_from_1900" &&
              key !== "death_year_from_1900" &&
              key !== "birth_and_death_year_from_1900" &&
              key !== "number_of_view" &&
              key !== "century_of_birth" &&
              key !== "century_of_death"
          ) {

              const generic_dict = generate_list_of_dict(
                  list_of_user_data[key],
                  number_of_bar_to_display
              );

              list_of_graph.push(make_a_graphic("bar", generic_dict, VAR_TO_DESCRIPTION[key]));

              if (key === "first_name" || key === "first_name_standard") {
                  // Prénoms avec et sans accent, limités à 10000
                  list_of_dict.push(generate_list_of_dict(list_of_user_data[key], 10000));
              } else if (
                  key !== "town_birth_and_death_place" &&
                  key !== "town_birth_place" &&
                  key !== "town_death_place" &&
                  key !== "dict_of_error_counter"
              ) {
                  list_of_dict.push(generate_list_of_dict(list_of_user_data[key], 2000));
              } else {
                  list_of_dict.push(generate_list_of_dict(list_of_user_data[key], 500));
              }

          } else if (key === "dict_of_error") {

              const generic_dict = generate_list_of_dict(
                  list_of_user_data[key],
                  3
              );

              list_of_graph.push(make_a_graphic("bar", generic_dict, VAR_TO_DESCRIPTION[key]));
              list_of_dict.push(generate_list_of_dict(list_of_user_data[key], 500));

          } else if (
              key === "birth_year" ||
              key === "death_year" ||
              key === "birth_and_death_year"
          ) {

              const generic_dict = generate_list_of_dict_with_a_lenght_limit(
                  list_of_user_data[key],
                  50000000
              );

              list_of_graph.push(make_a_graphic("bar", generic_dict as any, VAR_TO_DESCRIPTION[key]));
              list_of_dict.push(generate_list_of_dict_with_a_lenght_limit(list_of_user_data[key], 50000000));

          } else {

              const generic_dict = generate_list_of_dict(
                  list_of_user_data[key],
                  10000000
              );

              list_of_graph.push(make_a_graphic("bar", generic_dict, VAR_TO_DESCRIPTION[key]));
              list_of_dict.push(generate_list_of_dict(list_of_user_data[key], 50000000));
          }
      }
  }

  return { list_of_graph, list_of_dict, list_of_keys_name }
}

// Nombre d'éléments, moyenne et médiane du tableau détaillé (même calcul qu'avant)
function compute_summary(data_dict: any, keys_info: string, list_of_user_data: any) {
  let total_number : any = 0
  let text_to_display = "Part (%)"
  let display_average = false
  let avg : any = 0
  let average : any = 0
  let mediane : any = 0
  let average_step_list : any = 0

  data_dict.forEach((data:any) => {
    total_number += data.data_number
  })
  if (keys_info == "dict_of_error") {
    total_number = list_of_user_data.number_of_user_found
    text_to_display = "% de personnes avec cette erreur"
  }
  if (data_dict.length > 2) {
      mediane = data_dict[Math.round(data_dict.length/2)].data_name
  }

  for (let i = 0; i < data_dict.length; i++) {
      if (total_number/2 >= average_step_list) {
        mediane=data_dict[i].data_name
      }
      average_step_list+=data_dict[i].data_number
  }
  if (LIST_OF_VARIABLE_THAT_NEED_COMPUTING.includes(keys_info)) {
      data_dict.forEach((data:any) => {
        avg += (data.data_name * data.data_number)
      })

    display_average = true
    average=(Math.round(avg/total_number * 10) * 10)/100
  }

  if (average == 0 && display_average == true) {
    mediane=0
  }

  return { total_number, text_to_display, display_average, average, mediane }
}

const Statistics = () => {
    const [dict_of_advance_search,set_dict_of_advance_search] : any = useState({})
    // Filtres de la dernière recherche lancée (null tant qu'aucune recherche n'a été faite)
    const [submitted_search,set_submitted_search] : any = useState(null)
    const [filters_open,set_filters_open] = useState(false)
    // Graphique dont le tableau détaillé est ouvert
    const [detail_index,set_detail_index] = useState<number | null>(null)

    // L'appel API passe par TanStack Query : une recherche déjà faite revient du cache
    const statistics_query = useQuery({
      ...advanced_statistics_query(submitted_search),
      enabled: submitted_search !== null,
      // Garde les résultats précédents en mémoire pendant le chargement d'une nouvelle recherche
      placeholderData: keepPreviousData,
    })
    const list_of_user_data : any = statistics_query.data?.all_wikipedia_info ?? NO_DATA
    const loading = statistics_query.isLoading || statistics_query.isPlaceholderData
    const server_error_found = statistics_query.isError
    var error_type = 0
    if (server_error_found) {
      error_type = 1
    }
    if (statistics_query.error?.toString() === "ApiError: Erreur HTTP 429") {
      error_type = 2;
    }
    
    
    // 0 OK
    // 1 ERREUR SERVEUR
    // 2 TROP DE REQUETTES
    
    const result_found = statistics_query.data !== undefined && !statistics_query.isError
    const active_filters_count = count_active_filters(STATISTICS_FILTERS, dict_of_advance_search)

    const { list_of_graph, list_of_dict, list_of_keys_name } = result_found ? build_charts(list_of_user_data) : NO_CHARTS

    const detail_rows : any[] = detail_index === null ? [] : (list_of_dict[detail_index] ?? [])
    const detail_key = detail_index === null ? "" : list_of_keys_name[detail_index]
    const summary = compute_summary(detail_rows, detail_key, list_of_user_data)

    function get_list_of_user_advanced_statistics() {
      set_filters_open(false)
      set_submitted_search(dict_of_advance_search)
      retry_if_failed(advanced_statistics_query(dict_of_advance_search).queryKey)
    }

   return (
    <main className="mx-auto w-full max-w-7xl flex-1 space-y-6 px-4 py-10">
      <PageHeader
        title="Statistiques détaillées"
        description="Consultez les statistiques détaillées des pages Wikipédia et affinez vos recherches grâce aux filtres avancés."
      >
        <Button variant="outline" onClick={() => set_filters_open(true)}>
          <SlidersHorizontalIcon /> Filtres avancés
          {active_filters_count > 0 && <Badge className="ml-1">{active_filters_count}</Badge>}
        </Button>
        <Button className={BLACK_BUTTON} onClick={() => get_list_of_user_advanced_statistics()} disabled={loading}>
          {loading ? <Spinner /> : <SearchIcon />} Rechercher
        </Button>
      </PageHeader>

      <ActiveFilters sections={STATISTICS_FILTERS} filters={dict_of_advance_search} set_filters={set_dict_of_advance_search} />

      {error_type == 1 &&(
          <ErrorState on_retry={() => statistics_query.refetch()} />
      )}
            
      {error_type == 2 &&(
        <TooMuchRequestError description="Tu as fait trop de requêtes, patiente 15 minutes." on_retry={() => statistics_query.refetch()} />
      )}

      {loading && <LoadingState />}

      {!loading && result_found && (
        <section className="space-y-4">
          <h2 className="text-lg font-semibold">
            Statistiques des {format_number(list_of_user_data.number_of_user_found ?? 0)} pages Wikipédia trouvées
          </h2>

          <Accordion type="multiple" className="rounded-xl border px-4">
            {list_of_keys_name.map((key: string) => (
              LIST_OF_THEME.includes(key) && (
                <AccordionItem key={key} value={key}>
                  <AccordionTrigger className="text-base">
                    {LIST_OF_THEME.indexOf(key) + 1}. {STAT_TO_DESCRIPTION[key]}
                  </AccordionTrigger>
                  <AccordionContent>
                    <div className="space-y-10 pt-2">
                      {list_of_graph.map((graph: any, index2: number) => (
                        SUB_THEME_TO_THEME[list_of_keys_name[index2]] === key && (
                          <StatChartCard key={index2} options={graph} on_show_table={() => set_detail_index(index2)} />
                        )
                      ))}
                    </div>
                  </AccordionContent>
                </AccordionItem>
              )
            ))}
          </Accordion>
        </section>
      )}

      {!loading && !result_found && !server_error_found && (
        <EmptyState
          title="Lancez une recherche pour afficher les statistiques"
          description="Sans filtre, les statistiques portent sur toutes les pages Wikipédia. Utilisez les filtres avancés pour cibler un métier, un pays, une époque…"
        >
          <Button variant="outline" onClick={() => set_filters_open(true)}>
            <SlidersHorizontalIcon /> Filtres avancés
          </Button>
          <Button className={BLACK_BUTTON} onClick={() => get_list_of_user_advanced_statistics()}>
            <SearchIcon /> Rechercher
          </Button>
        </EmptyState>
      )}

      <AdvancedSearchDialog
        open={filters_open}
        on_open_change={set_filters_open}
        sections={STATISTICS_FILTERS}
        filters={dict_of_advance_search}
        set_filters={set_dict_of_advance_search}
        on_search={() => get_list_of_user_advanced_statistics()}
      />

      <DataTableDialog
        open={detail_index !== null}
        on_open_change={(open) => { if (!open) set_detail_index(null) }}
        title={VAR_TO_DESCRIPTION[detail_key] ?? "Statistiques détaillées"}
        summary={[
          { label: "Nombre d'éléments", value: format_number(Number(summary.total_number) || 0) },
          ...(summary.display_average ? [
            { label: "Moyenne", value: summary.average },
            { label: "Médiane", value: summary.mediane },
          ] : []),
        ]}
        // Villes sans localisation : seulement la colonne ville, pour la copier-coller
        hide_index={detail_key === "town_with_no_locolisation_counter"}
        columns={detail_key === "town_with_no_locolisation_counter" ? [
          { header: "Ville", cell: (data) => data.data_name },
        ] : [
          { header: "Élément", cell: (data) => data.data_name },
          { header: "Occurrences", numeric: true, cell: (data) => format_number(data.data_number) },
          { header: summary.text_to_display, numeric: true, cell: (data) => format_number(Math.round((data.data_number/summary.total_number * 100) * 100)/100) },
        ]}
        rows={detail_rows}
      />
    </main>

  );
};

export default Statistics;
