import type { ReactNode } from "react"
import { RotateCcwIcon, TriangleAlertIcon } from "lucide-react"
import { useTranslation } from "react-i18next"
import { Alert, AlertAction, AlertDescription, AlertTitle, Button, Spinner } from "@steevenakintilo/ui"

const HOMER_GIF = "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790270925/homer-simpson-the-simpsons_ovduma.gif"

// Les textes reçus en français (clés de traduction) sont traduits ici, les pages n'ont donc rien à faire
export function PageHeader({ title, description, children }: { title: string, description?: ReactNode, children?: ReactNode }) {
  const { t } = useTranslation()

  return (
    <div className="flex flex-col gap-4 border-b pb-6 sm:flex-row sm:items-end sm:justify-between">
      <div className="space-y-1.5">
        <h1 className="text-2xl font-semibold tracking-tight text-balance sm:text-3xl">{t(title)}</h1>
        {description && <p className="max-w-2xl text-pretty text-muted-foreground">{typeof description === "string" ? t(description) : description}</p>}
      </div>
      {children && <div className="flex flex-wrap gap-2">{children}</div>}
    </div>
  )
}

export function LoadingState({ title = "Ça charge…", description = "Veuillez patienter, cela peut prendre quelques minutes." }: { title?: string, description?: string }) {
  const { t } = useTranslation()

  return (
    <div role="status" aria-live="polite" className="flex flex-col items-center gap-4 rounded-xl border border-dashed px-4 py-10 text-center">
      <img src={HOMER_GIF} alt="" className="size-44 rounded-lg object-cover sm:size-56" />
      <div className="flex items-center gap-2 font-medium">
        <Spinner /> {t(title)}
      </div>
      <p className="text-xl text-muted-foreground">{t(description)}</p>
    </div>
  )
}

export function ErrorState({ title = "Erreur serveur", description = "Veuillez patienter quelques minutes puis réessayer.", on_retry }: { title?: string, description?: string, on_retry?: () => void }) {
  const { t } = useTranslation()

  return (
    <div>
      <Alert variant="destructive">
        <TriangleAlertIcon />
        <AlertTitle>{t(title)}</AlertTitle>
        <AlertDescription>{t(description)}</AlertDescription>
        {on_retry && (
          <AlertAction>
            <Button variant="outline" size="sm" onClick={on_retry}>
              <RotateCcwIcon /> {t("Réessayer")}
            </Button>
            
          </AlertAction>
        )}
      </Alert>
      <div className="flex justify-center">
        <img
          src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790977037/blob_pbtk_lcqgcu.jpg"
          alt={t("Erreur")}
        />
      </div>
    </div>
  )
}


export function TooMuchRequestError({ title = "Trop de requêtes", description = "Tu as fait trop de requêtes, patiente quelques minutes.", on_retry }: { title?: string, description?: string, on_retry?: () => void }) {
  const { t } = useTranslation()

  return (
    <div>
      <Alert variant="destructive">
        <TriangleAlertIcon />
        <AlertTitle>{t(title)}</AlertTitle>
        <AlertDescription>{t(description)}</AlertDescription>
        {on_retry && (
          <AlertAction>
            <Button variant="outline" size="sm" onClick={on_retry}>
              <RotateCcwIcon /> {t("Réessayer")}
            </Button>
            
          </AlertAction>
        )}
      </Alert>
      <div className="flex justify-center">
        <img
          src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1791235259/Peter-griffin-death-pose-meme-5_xhteqx.jpg"
          alt={t("Trop de requêtes")}
        />
      </div>
    </div>
  )
}

export function EmptyState({ icon, title, description, children }: { icon?: ReactNode, title: string, description?: ReactNode, children?: ReactNode }) {
  const { t } = useTranslation()

  return (
    <div className="flex flex-col items-center gap-3 rounded-xl border border-dashed px-4 py-12 text-center">
      {icon && <div className="flex size-11 items-center justify-center rounded-full bg-muted text-muted-foreground [&_svg]:size-5">{icon}</div>}
      <p className="font-medium">{t(title)}</p>
      {description && <p className="max-w-md text-sm text-pretty text-muted-foreground">{typeof description === "string" ? t(description) : description}</p>}
      {children && <div className="mt-2 flex flex-wrap justify-center gap-2">{children}</div>}
    </div>
  )
}
