import { backend_url_prod } from "../utils/global_variable.tsx"

// Erreur levée pour toute réponse HTTP non 2xx : TanStack Query la range dans `error`
export class ApiError extends Error {
  status: number

  constructor(status: number) {
    super(`Erreur HTTP ${status}`)
    this.name = "ApiError"
    this.status = status
  }
}

type ApiFetchOptions = {
  method?: "GET" | "POST"
  body?: any
  response_type?: "json" | "blob"
}

// Tous les appels au backend passent par ici, et sont appelés uniquement depuis TanStack Query (voir queries.ts)
export async function api_fetch(path: string, options: ApiFetchOptions = {}) {
  console.log(path,options)
  const response = await fetch(`${backend_url_prod}${path}`, {
    method: options.method ?? "GET",
    headers: {"Content-Type" : "application/json"},
    body: options.body === undefined ? undefined : JSON.stringify(options.body),
  })

  if (!response.ok) {
    throw new ApiError(response.status)
  }
  if (options.response_type === "blob") {
    return response.blob()
  }
  return response.json()
}
