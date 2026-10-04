import { BLACK_BUTTON } from "../utils/styles.ts"
import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { SearchIcon } from "lucide-react";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger, Button, Spinner, Tabs, TabsContent, TabsList, TabsTrigger } from "@steevenakintilo/ui";

import {THEME_TO_SUB_THEMES_FOR_RANKING, LIST_OF_THEME_FOR_RANKING , LIST_OF_THEME_FOR_GENDER_RATIO , THEME_TO_SUB_THEMES_FOR_GENDER_RATIO} from '../utils/global_variable'

import {make_a_graphic ,generate_list_of_dict_with_three_params_as_data, generate_list_of_dict_with_four_params_as_data , make_a_stacked_bar_graphic , is_screen_for_mobile} from "../utils/utility_function.tsx";
import { other_statistics_query, retry_if_failed } from "../api/queries.ts";
import { DataTableDialog } from "../components/data_table_dialog.tsx";
import { EmptyState, ErrorState, LoadingState, PageHeader } from "../components/page.tsx";
import { StatChartCard } from "../components/stat_chart.tsx";

const NO_DATA = {}
const NO_CHARTS = {
  list_of_graph: [], list_of_dict: [], list_of_keys_name: [],
  list_of_graph2: [], list_of_dict2: [], list_of_keys_name2: [],
}

const format_number = (value: any) => (typeof value === "number" ? value.toLocaleString("fr-FR") : value)

// Construit les graphiques de classement (1) et de ratio hommes / femmes (2)
function build_charts(list_of_ranking_data: any, list_of_gender_data: any) {
  const keys = Object.keys(list_of_ranking_data);
  const keys2 = Object.keys(list_of_gender_data);

  const list_of_graph: any[] = [];
  const list_of_dict: any[] = [];
  const list_of_keys_name: string[] = [];

  const list_of_graph2: any[] = [];
  const list_of_dict2: any[] = [];
  const list_of_keys_name2: string[] = [];
  let number_of_bar_to_display = 10;
  if (is_screen_for_mobile() == true) {
    number_of_bar_to_display = 3
  }

  for (let i = 0; i < keys.length - 1; i++) {
      const key = keys[i];

      if (list_of_ranking_data[key].length >= 1) {
        const generic_dict = generate_list_of_dict_with_three_params_as_data(
            list_of_ranking_data[key],
            number_of_bar_to_display
        );

        list_of_keys_name.push(key);
        list_of_graph.push(make_a_graphic("bar", generic_dict, key));
        list_of_dict.push(generate_list_of_dict_with_three_params_as_data(list_of_ranking_data[key], 50000000));
      }
  }

  for (let i = 0; i < keys2.length - 1; i++) {
      const key = keys2[i];

      if (list_of_gender_data[key].length >= 1) {
        const generic_dict = generate_list_of_dict_with_four_params_as_data(
            list_of_gender_data[key],
            number_of_bar_to_display
        );

        list_of_keys_name2.push(key);
        list_of_graph2.push(make_a_stacked_bar_graphic(generic_dict, key));
        list_of_dict2.push(generate_list_of_dict_with_four_params_as_data(list_of_gender_data[key], 50000000));
      }
  }

  return { list_of_graph, list_of_dict, list_of_keys_name, list_of_graph2, list_of_dict2, list_of_keys_name2 }
}

function total_occurences(data_dict: any[]) {
  let total_number = 0
  data_dict.forEach((data: any) => {
    total_number += data.data_occurence
  })
  return total_number
}

// Titre du tableau : le nom de la statistique quand c'en est un ("Les …")
function detail_title(keys_info: string) {
  return keys_info[0] == "L" ? keys_info : "Statistiques détaillées"
}

const OtherStatistics = () => {

    const [search_launched,set_search_launched] = useState(false)
    // Tableau détaillé ouvert : graphique de classement ou de ratio
    const [detail,set_detail] = useState<{ kind: "ranking" | "gender", index: number } | null>(null)

    // L'appel API passe par TanStack Query : relancer la recherche répond depuis le cache
    const other_statistics = useQuery({
      ...other_statistics_query(),
      enabled: search_launched,
    })
    const list_of_ranking_data : any = other_statistics.data?.ranking_list_of_dict ?? NO_DATA
    const list_of_gender_data : any = other_statistics.data?.gender_ratio_list_of_dict ?? NO_DATA
    const loading = other_statistics.isLoading
    const server_error_found = other_statistics.isError
    const result_found = other_statistics.data !== undefined && !other_statistics.isError

    const charts = result_found ? build_charts(list_of_ranking_data, list_of_gender_data) : NO_CHARTS

    const ranking_rows : any[] = detail?.kind === "ranking" ? (charts.list_of_dict[detail.index] ?? []) : []
    const ranking_key = detail?.kind === "ranking" ? charts.list_of_keys_name[detail.index] : ""
    const gender_rows : any[] = detail?.kind === "gender" ? (charts.list_of_dict2[detail.index] ?? []) : []
    const gender_key = detail?.kind === "gender" ? charts.list_of_keys_name2[detail.index] : ""

    function get_list_of_user_other_advanced_statistics() {
      set_search_launched(true)
      retry_if_failed(other_statistics_query().queryKey)
    }

    function close_detail(open: boolean) {
      if (!open) {
        set_detail(null)
      }
    }

   return (
    <main className="mx-auto w-full max-w-7xl flex-1 space-y-6 px-4 py-10">
      <PageHeader
        title="Autres statistiques"
        description="Classements des noms, villes, pays… par rapport à un score, et ratio hommes / femmes par ville, pays, âge, etc."
      >
        {result_found && (
          <Button variant="outline" onClick={() => other_statistics.refetch()} disabled={other_statistics.isFetching}>
            {other_statistics.isFetching ? <Spinner /> : <SearchIcon />} Actualiser
          </Button>
        )}
      </PageHeader>

      {server_error_found && <ErrorState on_retry={() => other_statistics.refetch()} />}

      {loading && <LoadingState />}

      {!loading && result_found && (
        <Tabs defaultValue="gender" className="gap-4">
          <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
            <TabsList>
              <TabsTrigger value="gender">Ratio hommes / femmes</TabsTrigger>
              <TabsTrigger value="ranking">Classements</TabsTrigger>
            </TabsList>
            <p className="text-sm text-muted-foreground">
              Le score correspond à la moyenne de tous les utilisateurs possédant cette variable.
            </p>
          </div>

          <TabsContent value="gender">
            <Accordion type="multiple" className="rounded-xl border px-4">
              {charts.list_of_keys_name2.map((key: string) => (
                LIST_OF_THEME_FOR_GENDER_RATIO.includes(key) && (
                  <AccordionItem key={key} value={key}>
                    <AccordionTrigger className="text-base">
                      {THEME_TO_SUB_THEMES_FOR_GENDER_RATIO[key].split("classé(e)s")[0]}
                    </AccordionTrigger>
                    <AccordionContent>
                      <div className="space-y-10 pt-2">
                        {charts.list_of_graph2.map((graph: any, index2: number) => (
                          THEME_TO_SUB_THEMES_FOR_GENDER_RATIO[charts.list_of_keys_name2[index2]] === key && (
                            <StatChartCard key={index2} options={graph} on_show_table={() => set_detail({ kind: "gender", index: index2 })} />
                          )
                        ))}
                      </div>
                    </AccordionContent>
                  </AccordionItem>
                )
              ))}
            </Accordion>
          </TabsContent>

          <TabsContent value="ranking">
            <Accordion type="multiple" className="rounded-xl border px-4">
              {charts.list_of_keys_name.map((key: string) => (
                LIST_OF_THEME_FOR_RANKING.includes(key) && (
                  <AccordionItem key={key} value={key}>
                    <AccordionTrigger className="text-base">
                      {THEME_TO_SUB_THEMES_FOR_RANKING[key].split("classé(e)s")[0]}
                    </AccordionTrigger>
                    <AccordionContent>
                      <div className="space-y-10 pt-2">
                        {charts.list_of_graph.map((graph: any, index2: number) => (
                          THEME_TO_SUB_THEMES_FOR_RANKING[charts.list_of_keys_name[index2]] === key && (
                            <StatChartCard key={index2} options={graph} on_show_table={() => set_detail({ kind: "ranking", index: index2 })} />
                          )
                        ))}
                      </div>
                    </AccordionContent>
                  </AccordionItem>
                )
              ))}
            </Accordion>
          </TabsContent>
        </Tabs>
      )}

      {!loading && !result_found && !server_error_found && (
        <EmptyState
          title="Consultez d'autres statistiques liées aux pages Wikipédia"
          description="Le chargement peut prendre quelques minutes la première fois, ensuite les résultats sont gardés en cache."
        >
          <Button className={BLACK_BUTTON} onClick={() => get_list_of_user_other_advanced_statistics()}>
            <SearchIcon /> Afficher les statistiques
          </Button>
        </EmptyState>
      )}

      <DataTableDialog
        open={detail?.kind === "ranking"}
        on_open_change={close_detail}
        title={detail_title(ranking_key)}
        summary={[{ label: "Nombre d'éléments", value: format_number(total_occurences(ranking_rows)) }]}
        columns={[
          { header: "Élément", cell: (data) => data.data_name },
          { header: "Score", numeric: true, cell: (data) => format_number(data.data_number) },
          { header: "Occurrences", numeric: true, cell: (data) => format_number(data.data_occurence) },
        ]}
        rows={ranking_rows}
      />

      <DataTableDialog
        open={detail?.kind === "gender"}
        on_open_change={close_detail}
        title={detail_title(gender_key)}
        summary={[{ label: "Nombre d'éléments", value: format_number(total_occurences(gender_rows)) }]}
        columns={[
          { header: "Élément", cell: (data) => data.data_name },
          { header: "% de femmes", numeric: true, cell: (data) => format_number(data.ratio_girl) },
          { header: "% d'hommes", numeric: true, cell: (data) => format_number(data.ratio_boy) },
          { header: "Occurrences", numeric: true, cell: (data) => format_number(data.data_occurence) },
        ]}
        rows={gender_rows}
      />
    </main>

  );
};

export default OtherStatistics;
