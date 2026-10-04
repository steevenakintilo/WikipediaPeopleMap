import { QueryClient } from "@tanstack/react-query"

import { ApiError } from "./client.ts"

const MINUTE = 60 * 1000

export const query_client = new QueryClient({
  defaultOptions: {
    queries: {
      // Les données Wikipédia changent rarement : pendant 10 min une réponse est
      // servie depuis le cache, sans rappeler le backend
      staleTime: 10 * MINUTE,
      // Une réponse qui n'est plus affichée reste 30 min en mémoire
      gcTime: 30 * MINUTE,
      // Pas de nouvel essai sur une erreur 4xx, un seul sur une erreur réseau / 5xx
      retry: (failure_count, error) => !(error instanceof ApiError && error.status < 500) && failure_count < 1,
      refetchOnWindowFocus: false,
    },
  },
})
