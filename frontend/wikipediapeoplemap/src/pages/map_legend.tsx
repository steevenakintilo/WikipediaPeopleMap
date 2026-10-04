import { useState } from "react";
import { ChevronDownIcon } from "lucide-react";
import { cn } from "@steevenakintilo/ui";

import { gender_to_color, gender_to_color2 } from "../utils/global_variable.tsx";

// Mêmes couleurs que les cercles de la carte (genre + vivant/décédé)
const LEGEND_ITEMS = [
  { color: gender_to_color.ManTrue, label: "Naissance : homme vivant" },
  { color: gender_to_color.ManFalse, label: "Naissance : homme décédé" },
  { color: gender_to_color2.ManFalse, label: "Décès : homme" },
  { color: gender_to_color.WomanTrue, label: "Naissance : femme vivante" },
  { color: gender_to_color.WomanFalse, label: "Naissance : femme décédée" },
  { color: gender_to_color2.WomanFalse, label: "Décès : femme" },
];

const Legend = ({ className }: { className?: string }) => {
  // Repliée par défaut sur mobile pour laisser la place à la carte
  const [open, set_open] = useState(() => window.innerWidth > 768);

  return (
    <div className={cn("w-56 rounded-lg border bg-background/95 text-xs shadow-md backdrop-blur", className)}>
      <button
        type="button"
        aria-expanded={open}
        className="flex w-full items-center justify-between px-3 py-2 font-medium"
        onClick={() => set_open(!open)}
      >
        Légende
        <ChevronDownIcon className={cn("size-4 text-muted-foreground transition-transform", open && "rotate-180")} />
      </button>
      {open && (
        <ul className="space-y-1.5 px-3 pb-3">
          {LEGEND_ITEMS.map((item) => (
            <li key={item.label} className="flex items-center gap-2">
              <span className="size-3 shrink-0 rounded-full ring-1 ring-foreground/25" style={{ backgroundColor: item.color }} />
              {item.label}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Legend;
