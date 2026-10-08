import { BLACK_BUTTON } from "../utils/styles.ts"
import type { Dispatch, SetStateAction } from "react"
import { RotateCcwIcon, SearchIcon, XIcon } from "lucide-react"
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
  Badge,
  Button,
  Combobox,
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  Field,
  FieldDescription,
  FieldLabel,
  Input,
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
  ToggleGroup,
  ToggleGroupItem,
} from "@steevenakintilo/ui"

import { COUNTRY_OPTIONS, displayed_value, is_active, NO_PREFERENCE, without_key, count_active_filters, type FilterField, type FilterSection, type Filters } from "./advanced_search_config.ts"

type FiltersStateProps = {
  sections: FilterSection[]
  filters: Filters
  set_filters: Dispatch<SetStateAction<any>>
}

// Les filtres en cours sous forme de badges, chacun supprimable
export function ActiveFilters({ sections, filters, set_filters }: FiltersStateProps) {
  const active_fields = sections.flatMap((section) => section.fields).filter((field) => is_active(filters[field.key]))
  if (active_fields.length === 0) {
    return null
  }

  return (
    <div className="flex flex-wrap items-center gap-1.5">
      {active_fields.map((field) => (
        <Badge key={field.key} variant="secondary" className="h-auto gap-1 py-0.5 pr-0.5 whitespace-normal">
          <span className="text-muted-foreground">{field.label} :</span>
          {displayed_value(field, filters[field.key])}
          <button
            type="button"
            aria-label={`Retirer le filtre ${field.label}`}
            className="rounded-sm p-0.5 hover:bg-foreground/10"
            onClick={() => set_filters((prev: Filters) => without_key(prev, field.key))}
          >
            <XIcon className="size-3" />
          </button>
        </Badge>
      ))}
      <Button variant="link" size="xs" onClick={() => set_filters({})}>
        Tout effacer
      </Button>
    </div>
  )
}

function FilterInput({ field, filters, set_filters }: { field: FilterField } & Omit<FiltersStateProps, "sections">) {
  const id = `filter-${field.key}`
  const value = filters[field.key]

  function set_value(next: string | undefined) {
    set_filters((prev: Filters) => (next === undefined ? without_key(prev, field.key) : { ...prev, [field.key]: next }))
  }

  if (field.type === "country") {
    return (
      <Field>
        <FieldLabel htmlFor={id}>{field.label}</FieldLabel>
        <Combobox
          id={id}
          options={COUNTRY_OPTIONS}
          value={value}
          onValueChange={set_value}
          placeholder="Tous"
          searchPlaceholder="Rechercher un pays, une région…"
          emptyText="Aucun pays trouvé."
        />
      </Field>
    )
  }

  if (field.type === "choice") {
    return (
      <Field>
        <FieldLabel>{field.label}</FieldLabel>
        <ToggleGroup
          type="single"
          variant="outline"
          size="sm"
          aria-label={field.label}
          value={value ?? ""}
          // Recliquer sur l'option choisie la désélectionne (= pas de filtre)
          onValueChange={(next) => set_value(next === "" ? undefined : next)}
        >
          {field.options.map((option) => (
            <ToggleGroupItem key={option.value} value={option.value} className="data-[state=on]:border-primary data-[state=on]:bg-primary/10 data-[state=on]:text-primary">
              {option.label}
            </ToggleGroupItem>
          ))}
        </ToggleGroup>
      </Field>
    )
  }

  if (field.type === "select") {
    return (
      <Field>
        <FieldLabel htmlFor={id}>{field.label}</FieldLabel>
        <Select value={value ?? ""} onValueChange={(next) => set_value(next === NO_PREFERENCE ? undefined : next)}>
          <SelectTrigger id={id} className="w-full">
            <SelectValue placeholder={field.placeholder} />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value={NO_PREFERENCE}>{field.placeholder}</SelectItem>
            {field.options.map((option) => (
              <SelectItem key={option.value} value={option.value}>
                {option.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </Field>
    )
  }

  return (
    <Field>
      <FieldLabel htmlFor={id}>{field.label}</FieldLabel>
      <Input
        id={id}
        type={field.type === "number" ? "number" : "text"}
        inputMode={field.type === "number" ? "numeric" : undefined}
        min={field.type === "number" ? field.min : undefined}
        max={field.type === "number" ? field.max : undefined}
        step={field.type === "number" ? 1 : undefined}
        placeholder={field.placeholder}
        value={value ?? ""}
        onChange={(event) => set_value(event.target.value)}
      />
      {field.type === "text" && field.description && <FieldDescription>{field.description}</FieldDescription>}
    </Field>
  )
}

type AdvancedSearchDialogProps = FiltersStateProps & {
  open: boolean
  on_open_change: (open: boolean) => void
  on_search: () => void
  on_reset?: () => void
  search_label?: string
}

export function AdvancedSearchDialog({ open, on_open_change, sections, filters, set_filters, on_search, on_reset, search_label = "Rechercher" }: AdvancedSearchDialogProps) {
  const active_count = count_active_filters(sections, filters)

  return (
    <Dialog open={open} onOpenChange={on_open_change}>
      {/* Pas de focus automatique dans le premier champ : évite d'ouvrir le clavier sur mobile */}
      <DialogContent className="flex max-h-[90dvh] flex-col gap-0 p-0 sm:max-w-3xl" onOpenAutoFocus={(event) => event.preventDefault()}>
        <DialogHeader className="border-b p-4">
          <DialogTitle>Recherche avancée</DialogTitle>
          <DialogDescription>
            {active_count === 0 ? "Aucun filtre : toutes les personnes sont prises en compte." : `${active_count} filtre${active_count > 1 ? "s" : ""} actif${active_count > 1 ? "s" : ""}.`}
          </DialogDescription>
        </DialogHeader>

        <div className="min-h-0 flex-1 overflow-y-auto px-4 py-2">
          {/* Seule la première section (thème principal) est ouverte, les autres se déplient à la demande */}
          <Accordion type="multiple" defaultValue={sections.slice(0, 1).map((section) => section.title)}>
            {sections.map((section) => {
              const section_active_count = section.fields.filter((field) => is_active(filters[field.key])).length
              return (
                <AccordionItem key={section.title} value={section.title}>
                  <AccordionTrigger>
                    <span className="flex items-center gap-2">
                      {section.title}
                      {section_active_count > 0 && <Badge variant="secondary">{section_active_count}</Badge>}
                    </span>
                  </AccordionTrigger>
                  <AccordionContent>
                    <div className="grid gap-4 p-1 sm:grid-cols-2">
                      {section.fields.map((field) => (
                        <FilterInput key={field.key} field={field} filters={filters} set_filters={set_filters} />
                      ))}
                    </div>
                  </AccordionContent>
                </AccordionItem>
              )
            })}
          </Accordion>
        </div>

        <DialogFooter className="m-0 flex-row items-center border-t p-4">
          <Button variant="ghost" className="mr-auto" onClick={on_reset ?? (() => set_filters({}))} disabled={active_count === 0 && on_reset === undefined}>
            <RotateCcwIcon /> Réinitialiser
          </Button>
          <DialogClose asChild>
            <Button variant="outline">Fermer</Button>
          </DialogClose>
          <Button className={BLACK_BUTTON} onClick={on_search}>
            <SearchIcon /> {search_label}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
