import { useState, type ReactNode } from "react"
import { SearchIcon } from "lucide-react"
import { useTranslation } from "react-i18next"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  InputGroup,
  InputGroupAddon,
  InputGroupInput,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@steevenakintilo/ui"

export type DataColumn = {
  header: string
  cell: (row: any) => ReactNode
  numeric?: boolean
}

type DataTableDialogProps = {
  open: boolean
  on_open_change: (open: boolean) => void
  title: string
  description?: string
  summary?: { label: string, value: ReactNode }[]
  columns: DataColumn[]
  rows: any[]
  /** Masque la colonne de numérotation (pour copier-coller une seule colonne) */
  hide_index?: boolean
}

// Vue tableau d'un graphique : toutes les valeurs, avec recherche par élément
export function DataTableDialog({ open, on_open_change, title, description, summary, columns, rows, hide_index = false }: DataTableDialogProps) {
  const { t } = useTranslation()
  const [search, set_search] = useState("")
  const visible_rows = rows
    .map((row, index) => ({ row, index }))
    .filter(({ row }) => String(row.data_name).toLowerCase().includes(search.toLowerCase()))

  function handle_open_change(next_open: boolean) {
    on_open_change(next_open)
    if (!next_open) {
      set_search("")
    }
  }

  return (
    <Dialog open={open} onOpenChange={handle_open_change}>
      <DialogContent className="flex max-h-[90dvh] flex-col sm:max-w-4xl">
        <DialogHeader>
          <DialogTitle className="pr-8 text-pretty">{t(title)}</DialogTitle>
          <DialogDescription>{description ? t(description) : t(rows.length > 1 ? "{{n}} éléments" : "{{n}} élément", { n: rows.length })}</DialogDescription>
        </DialogHeader>

        {summary && summary.length > 0 && (
          <dl className="grid grid-cols-2 gap-2 sm:grid-cols-4">
            {summary.map((item) => (
              <div key={item.label} className="rounded-lg border px-3 py-2">
                <dt className="text-xs text-muted-foreground">{t(item.label)}</dt>
                <dd className="text-base font-semibold">{item.value}</dd>
              </div>
            ))}
          </dl>
        )}

        <InputGroup>
          <InputGroupAddon>
            <SearchIcon />
          </InputGroupAddon>
          <InputGroupInput
            placeholder={t("Chercher un élément")}
            aria-label={t("Chercher un élément")}
            value={search}
            onChange={(event) => set_search(event.target.value)}
          />
        </InputGroup>

        <div className="min-h-0 flex-1 overflow-y-auto rounded-lg border">
          <Table>
            <TableHeader>
              <TableRow>
                {!hide_index && <TableHead className="w-20">#</TableHead>}
                {columns.map((column) => (
                  <TableHead key={column.header} className={column.numeric ? "text-right" : undefined}>
                    {t(column.header)}
                  </TableHead>
                ))}
              </TableRow>
            </TableHeader>
            <TableBody>
              {visible_rows.map(({ row, index }) => (
                <TableRow key={index}>
                  {!hide_index && (
                    <TableCell className="text-muted-foreground tabular-nums">
                      {index + 1}/{rows.length}
                    </TableCell>
                  )}
                  {columns.map((column) => (
                    <TableCell key={column.header} className={column.numeric ? "text-right tabular-nums" : "whitespace-normal"}>
                      {column.cell(row)}
                    </TableCell>
                  ))}
                </TableRow>
              ))}
            </TableBody>
          </Table>
          {visible_rows.length === 0 && (
            <p className="p-6 text-center text-sm text-muted-foreground">{t("Aucun élément ne correspond à « {{search}} ».", { search })}</p>
          )}
        </div>
      </DialogContent>
    </Dialog>
  )
}
