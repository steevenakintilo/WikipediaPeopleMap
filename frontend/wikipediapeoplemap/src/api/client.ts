import { backend_url_prod } from "../utils/global_variable.tsx"
import i18n from "../i18n/index.ts"
import { job_filter_to_french } from "../i18n/jobs.ts"

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
  //console.log(path,options)
  let body = options.body
  // Les métiers sont en français dans la base : une recherche saisie en anglais ("actor") est convertie avant l'envoi
  if (i18n.language === "en" && typeof body?.job === "string") {
    body = { ...body, job: job_filter_to_french(body.job) }
  }
  const response = await fetch(`${backend_url_prod}${path}`, {
    method: options.method ?? "GET",
    headers: {"Content-Type" : "application/json"},
    body: body === undefined ? undefined : JSON.stringify(body),
  })

  if (!response.ok) {
    throw new ApiError(response.status)
  }
  
  if (options.response_type === "blob") {
    return response.blob()
  }
  return response.json()
}
