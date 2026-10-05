import { BLACK_BUTTON } from "../utils/styles.ts"
import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { CircleCheckIcon, DownloadIcon, MonitorIcon, SearchXIcon, SlidersHorizontalIcon } from "lucide-react";
import { Alert, AlertDescription, AlertTitle, Badge, Button, Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle, Spinner, toast } from "@steevenakintilo/ui";

import { ApiError } from "../api/client.ts"
import { download_qjis_csv } from "../api/queries.ts"
import { ActiveFilters, AdvancedSearchDialog } from "../components/advanced_search.tsx";
import { count_active_filters, STATISTICS_FILTERS } from "../components/advanced_search_config.ts";
import { EmptyState, ErrorState, LoadingState, PageHeader, TooMuchRequestError } from "../components/page.tsx";

const EARTH_GIF = "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790349009/earth_qha8vm.gif"
const FILE_NAME = "qjis_localisation.csv"

function download_file(blob: Blob, file_name: string) {
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = file_name;
  document.body.appendChild(a);
  a.click();

  a.remove();
  window.URL.revokeObjectURL(url);
}

const QjisMap = () => {
    const [dict_of_advance_search,set_dict_of_advance_search] : any = useState({})
    const [filters_open,set_filters_open] = useState(false)

    // L'appel API passe par TanStack Query (mutation : génère un fichier, rien à mettre en cache)
    const qjis_csv = useMutation({
      mutationFn: download_qjis_csv,
      onSuccess: (blob) => {
        download_file(blob, FILE_NAME)
        toast.success("Fichier généré", { description: `Le téléchargement de ${FILE_NAME} a démarré.` })
      },
    })
    const loading = qjis_csv.isPending
    const no_result_found = qjis_csv.error instanceof ApiError && qjis_csv.error.status == 404
    const server_error_found = qjis_csv.isError && !no_result_found
    var error_type = 0
    if (server_error_found) {
      error_type = 1
    }
    if (qjis_csv.error?.toString() === "ApiError: Erreur HTTP 429") {
      error_type = 2;
    }
    
    const active_filters_count = count_active_filters(STATISTICS_FILTERS, dict_of_advance_search)

    function get_list_of_user_advanced_search() {
      set_filters_open(false)
      qjis_csv.mutate(dict_of_advance_search)
    }

   return (
    <main className="mx-auto w-full max-w-3xl flex-1 space-y-6 px-4 py-10">
      <PageHeader
        title="Export QGIS"
        description="Générez un fichier CSV des positions, utilisable dans QGIS, à partir de la recherche et des filtres avancés."
      />

      {/* QGIS est un logiciel pour ordinateur */}
      <div className="md:hidden">
        <EmptyState
          icon={<MonitorIcon />}
          title="Disponible uniquement sur ordinateur"
          description="Cette fonctionnalité nécessite le logiciel QGIS et n’est donc disponible que sur PC."
        >
          <img src={EARTH_GIF} alt="" className="size-48 rounded-full object-cover" />
        </EmptyState>
      </div>

      <div className="hidden space-y-6 md:block">
        <Card>
          <CardHeader>
            <CardTitle>Personnes à exporter</CardTitle>
            <CardDescription>
              {active_filters_count === 0
                ? "Aucun filtre : le fichier contiendra toutes les personnes."
                : "Le fichier contiendra les personnes correspondant à ces filtres."}
            </CardDescription>
          </CardHeader>
          {active_filters_count > 0 && (
            <CardContent>
              <ActiveFilters sections={STATISTICS_FILTERS} filters={dict_of_advance_search} set_filters={set_dict_of_advance_search} />
            </CardContent>
          )}
          <CardFooter className="flex-wrap gap-2">
            <Button variant="outline" onClick={() => set_filters_open(true)}>
              <SlidersHorizontalIcon /> Filtres avancés
              {active_filters_count > 0 && <Badge className="ml-1">{active_filters_count}</Badge>}
            </Button>
            <Button className={BLACK_BUTTON} onClick={() => get_list_of_user_advanced_search()} disabled={loading}>
              {loading ? <Spinner /> : <DownloadIcon />} Générer le fichier
            </Button>
          </CardFooter>
        </Card>

        {loading && <LoadingState title="Génération du fichier…" />}

        {error_type == 1 &&(
            <ErrorState on_retry={() => qjis_csv.refetch()} />
        )}
              
        {error_type == 2 &&(
          <TooMuchRequestError description="Tu as fait trop de requêtes, patiente 15 minutes." on_retry={() => qjis_csv.refetch()} />
        )}
        

        {!loading && no_result_found && (
          <Alert>
            <SearchXIcon />
            <AlertTitle>Aucun résultat</AlertTitle>
            <AlertDescription>Aucune page Wikipédia ne correspond à ces filtres : essayez-en d'autres.</AlertDescription>
          </Alert>
        )}

        {!loading && qjis_csv.isSuccess && (
          <Alert>
            <CircleCheckIcon />
            <AlertTitle>Fichier prêt</AlertTitle>
            <AlertDescription>Les pages Wikipédia ont été trouvées : le téléchargement de {FILE_NAME} a démarré automatiquement.</AlertDescription>
          </Alert>
        )}
      </div>

      <AdvancedSearchDialog
        open={filters_open}
        on_open_change={set_filters_open}
        sections={STATISTICS_FILTERS}
        filters={dict_of_advance_search}
        set_filters={set_dict_of_advance_search}
        on_search={() => get_list_of_user_advanced_search()}
        search_label="Générer le fichier"
      />
    </main>

  );
};

export default QjisMap;
