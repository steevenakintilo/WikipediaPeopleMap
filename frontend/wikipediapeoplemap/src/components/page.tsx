import type { ReactNode } from "react"
import { RotateCcwIcon, TriangleAlertIcon } from "lucide-react"
import { Alert, AlertAction, AlertDescription, AlertTitle, Button, Spinner } from "@steevenakintilo/ui"

const HOMER_GIF = "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790270925/homer-simpson-the-simpsons_ovduma.gif"

export function PageHeader({ title, description, children }: { title: string, description?: ReactNode, children?: ReactNode }) {
  return (
    <div className="flex flex-col gap-4 border-b pb-6 sm:flex-row sm:items-end sm:justify-between">
      <div className="space-y-1.5">
        <h1 className="text-2xl font-semibold tracking-tight text-balance sm:text-3xl">{title}</h1>
        {description && <p className="max-w-2xl text-pretty text-muted-foreground">{description}</p>}
      </div>
      {children && <div className="flex flex-wrap gap-2">{children}</div>}
    </div>
  )
}

export function LoadingState({ title = "Ça charge…", description = "Veuillez patienter, cela peut prendre quelques minutes." }: { title?: string, description?: string }) {
  return (
    <div role="status" aria-live="polite" className="flex flex-col items-center gap-4 rounded-xl border border-dashed px-4 py-10 text-center">
      <img src={HOMER_GIF} alt="" className="size-44 rounded-lg object-cover sm:size-56" />
      <div className="flex items-center gap-2 font-medium">
        <Spinner /> {title}
      </div>
      <p className="text-sm text-muted-foreground">{description}</p>
    </div>
  )
}

export function ErrorState({ title = "Erreur serveur", description = "Veuillez patienter quelques minutes puis réessayer.", on_retry }: { title?: string, description?: string, on_retry?: () => void }) {
  return (
    <div>
      <Alert variant="destructive">
        <TriangleAlertIcon />
        <AlertTitle>{title}</AlertTitle>
        <AlertDescription>{description}</AlertDescription>
        {on_retry && (
          <AlertAction>
            <Button variant="outline" size="sm" onClick={on_retry}>
              <RotateCcwIcon /> Réessayer
            </Button>
            
          </AlertAction>
        )}
      </Alert>
      <div className="flex justify-center">
        <img
          src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790977037/blob_pbtk_lcqgcu.jpg"
          alt="Erreur"
        />
      </div>
    </div>
  )
}

export function EmptyState({ icon, title, description, children }: { icon?: ReactNode, title: string, description?: ReactNode, children?: ReactNode }) {
  return (
    <div className="flex flex-col items-center gap-3 rounded-xl border border-dashed px-4 py-12 text-center">
      {icon && <div className="flex size-11 items-center justify-center rounded-full bg-muted text-muted-foreground [&_svg]:size-5">{icon}</div>}
      <p className="font-medium">{title}</p>
      {description && <p className="max-w-md text-sm text-pretty text-muted-foreground">{description}</p>}
      {children && <div className="mt-2 flex flex-wrap justify-center gap-2">{children}</div>}
    </div>
  )
}
