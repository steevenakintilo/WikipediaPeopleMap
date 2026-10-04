import { Avatar, AvatarFallback, AvatarImage, cn } from "@steevenakintilo/ui"

function initials_of(name: string) {
  return name
    .split(/[\s-]+/)
    .filter((word) => word !== "" && !word.startsWith("("))
    .slice(0, 2)
    .map((word) => word[0])
    .join("")
    .toUpperCase()
}

// Photo Wikipédia d'une personne, carrée comme avant (recadrée en gardant le haut : le visage),
// avec ses initiales si l'image manque ou ne charge pas
// whole = image entière dans le carré (sans recadrage) ; stretch = étirée au carré comme l'ancienne <img>
export function PersonPicture({ src, name, className, whole = false, stretch = false }: { src: string, name: string, className?: string, whole?: boolean, stretch?: boolean }) {
  return (
    <Avatar className={cn("rounded-none after:rounded-none", className)}>
      <AvatarImage src={src} alt="" className={cn("rounded-none object-top", whole && "object-contain object-center", stretch && "object-fill")} />
      <AvatarFallback delayMs={600} className="rounded-none text-base font-medium">
        {initials_of(name ?? "")}
      </AvatarFallback>
    </Avatar>
  )
}
