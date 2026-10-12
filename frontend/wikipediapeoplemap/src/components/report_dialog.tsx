import { useState } from "react"
import { useMutation } from "@tanstack/react-query"
import { FlagIcon, SendIcon } from "lucide-react"
import { useTranslation } from "react-i18next"
import type { TFunction } from "i18next"
import {
  Button,
  Checkbox,
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  Field,
  FieldLabel,
  Spinner,
  toast,
} from "@steevenakintilo/ui"

import { translate_job, translate_place } from "../i18n/data_names.ts"
import { update_user_info_status, type ReportableField } from "../api/queries.ts"

type ReportField = { field: ReportableField, label: string, current: (user: any, t: TFunction) => string, dead_only?: boolean }

const GENDERS: Record<string, string> = { Man: "Homme", Woman: "Femme", Unclear: "Non précisé" }

// Informations qu'un visiteur peut signaler comme fausses ou manquantes (field = nom du champ Django)
const REPORT_FIELDS: ReportField[] = [
  { field: "picture_url", label: "Photo de profil", current: () => "" },
  { field: "birth_date", label: "Date de naissance", current: (user) => user.birth_date },
  { field: "is_alive", label: "Statut (vivant / décédé)", current: (user, t) => (user.is_alive ? t("Vivant(e)") : t("Décédé(e)")) },
  { field: "death_date", label: "Date de mort", current: (user) => user.death_date, dead_only: true },
  { field: "gender", label: "Genre", current: (user, t) => t(GENDERS[user.gender] ?? user.gender) },
  { field: "age", label: "Âge", current: (user, t) => (user.age > 0 ? t("{{n}} ans", { n: user.age }) : "") },
  { field: "job", label: "Métier", current: (user, t) => translate_job(user.job, t) },
  { field: "town_birth_place", label: "Lieu de naissance (ville)", current: (user) => user.town_birth_place },
  { field: "birth_town_localisation", label: "Localisation de naissance (ville)", current: (user) => user.birth_town_localisation },
  { field: "country_birth_place", label: "Pays de naissance", current: (user, t) => translate_place(user.country_birth_place, t) },
  { field: "continent_of_birth", label: "Continent de naissance", current: (user, t) => translate_place(user.continent_of_birth, t) },
  { field: "region_of_birth", label: "Région de naissance", current: (user, t) => translate_place(user.region_of_birth, t) },
  { field: "town_death_place", label: "Lieu de mort (ville)", current: (user) => user.town_death_place, dead_only: true },
  { field: "death_town_localisation", label: "Localisation de mort (ville)", current: (user) => user.town_death_localisation, dead_only:true },
  { field: "country_death_place", label: "Pays de mort", current: (user, t) => translate_place(user.country_death_place, t), dead_only: true },
  { field: "continent_of_death", label: "Continent de mort", current: (user, t) => translate_place(user.continent_of_death, t), dead_only: true },
  { field: "region_of_death", label: "Région de mort", current: (user, t) => translate_place(user.region_of_death, t), dead_only: true },
  { field: "time_period_of_birth", label: "Période historique", current: (user) => user.time_period_of_birth},
  
]

const REPORT_FIELDS2: ReportField[] = [
  { field: "picture_url", label: "Photo de profil", current: () => "" },
  { field: "is_alive", label: "Statut (vivant / décédé)", current: (user, t) => (user.is_alive ? t("Vivant(e)") : t("Décédé(e)")) },
  { field: "death_date", label: "Date de mort", current: (user) => user.death_date, dead_only: true },
  { field: "age", label: "Âge", current: (user, t) => (user.age > 0 ? t("{{n}} ans", { n: user.age }) : "") },
  { field: "town_death_place", label: "Lieu de mort (ville)", current: (user) => user.town_death_place, dead_only: true },
  { field: "country_death_place", label: "Pays de mort", current: (user, t) => translate_place(user.country_death_place, t), dead_only: true },
  { field: "continent_of_death", label: "Continent de mort", current: (user, t) => translate_place(user.continent_of_death, t), dead_only: true },
  { field: "region_of_death", label: "Région de mort", current: (user, t) => translate_place(user.region_of_death, t), dead_only: true },
  
]

const RED_BUTTON = "bg-red-600 text-white hover:bg-red-700"
const ORANGE_BUTTON = "bg-orange-400 text-white hover:bg-orange-500";

// Bouton rouge + fenêtre : le visiteur coche les informations fausses ou manquantes, la vérification est faite à la main
export function ReportButton({ user }: { user: any }) {
  const { t } = useTranslation()
  const [open, set_open] = useState(false)
  const [checked_fields, set_checked_fields] = useState<ReportableField[]>([])
  var fields = REPORT_FIELDS.filter((field) => !field.dead_only || !user.is_alive)

  if (user.update_level == 2) {
    fields = REPORT_FIELDS2.filter((field) => !field.dead_only || !user.is_alive)
  }
  
  const report = useMutation({
    mutationFn: update_user_info_status,
    onSuccess: () => {
      toast.success(t("Merci !"), { description: t("Ton signalement a bien été envoyé, il sera vérifié.") })
      set_open(false)
      set_checked_fields([])
    },
    onError: () => toast.error(t("Envoi impossible"), { description: t("Le signalement n'a pas pu être envoyé, réessaie plus tard.") }),
  })

  function toggle(field: ReportableField, checked: boolean) {
    set_checked_fields((prev) => (checked ? [...prev, field] : prev.filter((item) => item !== field)))
  }

  var button_color : string = ORANGE_BUTTON
  if (user.update_level == 3) {
    button_color = RED_BUTTON
  } 
  return (
    <>
      <Button size="sm" className={button_color} onClick={() => set_open(true)}>
        <FlagIcon /> {t("Reporter une information erronée ou inexistante")}
      </Button>

      
      <Dialog open={open} onOpenChange={set_open}>
        <DialogContent className="flex max-h-[90dvh] flex-col gap-0 p-0 sm:max-w-xl">
          <DialogHeader className="border-b p-4">
            <DialogTitle>{t("Reporter une information : {{name}}", { name: user.page_name })}</DialogTitle>
            <DialogDescription>{t("Coche les informations fausses ou manquantes, elles seront vérifiées.")}</DialogDescription>
          </DialogHeader>

          <div className="min-h-0 flex-1 space-y-2 overflow-y-auto p-4">
            {fields.map((field) => {
              const id = `report-${field.field}`
              return (
                <Field key={field.field} orientation="horizontal" className="rounded-lg border p-3">
                  <Checkbox id={id} checked={checked_fields.includes(field.field)} onCheckedChange={(value) => toggle(field.field, value === true)} />
                  <FieldLabel htmlFor={id} className="flex-1">
                    {t(field.label)}
                    {field.current(user, t) && <span className="ml-auto truncate text-xs font-normal text-muted-foreground">{t("Actuel :")} {field.current(user, t)}</span>}
                  </FieldLabel>
                </Field>
              )
            })}
          </div>

          <DialogFooter className="m-0 flex-row items-center border-t p-4">
            <span className="mr-auto text-sm text-muted-foreground">
              {t(checked_fields.length > 1 ? "{{n}} informations cochées" : "{{n}} information cochée", { n: checked_fields.length })}
            </span>
            <DialogClose asChild>
              <Button variant="outline">{t("Annuler")}</Button>
            </DialogClose>
            <Button
              className={RED_BUTTON}
              disabled={checked_fields.length === 0 || report.isPending}
              onClick={() => report.mutate({ username: user.page_name, fields: checked_fields })}
            >
              {report.isPending ? <Spinner /> : <SendIcon />} {t("Envoyer")}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </>
  )
}
