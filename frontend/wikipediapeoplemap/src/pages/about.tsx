import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@steevenakintilo/ui";

import { PageHeader } from "../components/page.tsx";

const link_class = "font-medium text-primary underline-offset-4 hover:underline"

const About = () => {

   return (

    <main className="mx-auto w-full max-w-3xl flex-1 space-y-6 px-4 py-10">
        <PageHeader
            title="À propos"
        />

        <Accordion type="multiple" className="[&_p]:leading-relaxed [&_p+p]:mt-3">
            <AccordionItem value="site">
                <AccordionTrigger className="text-base">Explication du site</AccordionTrigger>

                <AccordionContent>
                    <p>
                        L’idée m’est venue après avoir vu sur Twitter un site qui
                        répertoriait les lieux de naissance de tous les joueurs
                        participant à la Coupe du monde 2026 en juillet 2026. Je me suis alors dit :
                        pourquoi ne pas faire la même chose pour toutes les personnes
                        réelles ayant une page Wikipédia en français ?
                    </p>

                    <p>
                        Il y a quatre pages principales sur le site :
                    </p>

                    <p>
                        <strong>La page Carte :</strong> elle permet d’accéder à une
                        carte interactive présentant les lieux de naissance et de décès
                        des personnes répertoriées, avec un système de filtres.
                    </p>

                    <p>
                        <strong>La page Statistiques :</strong> elle permet d’obtenir
                        différentes statistiques sur les résultats d’une recherche
                        effectuée à l’aide des filtres, notamment sous forme de
                        graphiques.
                    </p>

                    <p>
                        <strong>La page QGIS :</strong> disponible uniquement sur PC,
                        elle permet de générer un fichier csv utilisable sur QGIS à partir des filtres
                        sélectionnés.
                    </p>

                    <p> <strong>La page Autres Statistiques :</strong> elle permet d’obtenir d’autres statistiques liées au classement des noms/villes/pays, etc.
                        par rapport à un score, et d’avoir le ratio hommes/femmes par ville/pays/âge, etc. </p>


                    <p>
                        Le site a été conçu et développé pour être utilisé sur PC.
                        Il est donc préférable de l’utiliser sur ordinateur, même s’il
                        reste fonctionnel sur téléphone.
                    </p>
                </AccordionContent>
            </AccordionItem>

            <AccordionItem value="ranking">
                <AccordionTrigger className="text-base">Comment marche le calcul du classement ?</AccordionTrigger>

                <AccordionContent>
                    <p>
                        Pour classer un utilisateur, j'utilise 3 métriques :
                    </p>

                    <p>
                        <strong>Le nombre de liens sur la page de l'utilisateur :</strong> Selon moi, plus une personne cite de personnes réelles sur sa page, plus elle a de l'importance.
                    </p>

                    <p>
                        <strong>Le nombre de personnes qui ont l'utilisateur en lien sur leur page :</strong> De plus, plus une personne est citée, plus elle est importante.
                    </p>

                    <p>
                        <strong>La taille de la page Wikipédia de l'utilisateur :</strong> Plus la taille de la page est grande, plus cela veut dire que la personne a des choses à dire sur sa vie.
                    </p>

                    <p>
                        Ensuite, pour effectuer le calcul, je prends le résultat des 3 variables que je pondère sur une unité précise pour éviter que la taille de la page soit beaucoup plus grande que le nombre de liens, puis je divise le résultat par 3.
                        Cela explique pourquoi certaines personnes « inconnues » sont très élevées dans le classement, comme le top 3, car elles sont toutes mentionnées par plus de 8 800 personnes.
                    </p>                </AccordionContent>
            </AccordionItem>

            <AccordionItem value="technical">
                <AccordionTrigger className="text-base">Explication technique</AccordionTrigger>

                <AccordionContent>
                    <p>
                        Voici quelques explications techniques pour ceux que ça intéresse.
                        Le site a été codé en React + Vite avec TypeScript, avec une interface UI/UX basée sur shadcn/ui, Radix et Tailwind CSS. Côté backend, il fonctionne avec Django et une base de données PostgreSQL.
                    </p>

                    <p>
                        Pour récupérer les informations des pages Wikipédia, j’ai téléchargé le fichier ZIM de Wikipédia en français du 23 février 2026. J’ai ensuite créé un script Python permettant de récupérer uniquement les personnes ayant réellement existé. Le script fonctionne à 99 %, il est donc possible de trouver, très rarement, des pages qui ne correspondent pas à de vraies personnes.
                    </p>
                    <p>
                        J’ai ensuite développé un script permettant de récupérer les informations de chaque page. Le script fonctionne bien, mais il est impossible de garantir une récupération des informations à 100% pour plus de 700 000 pages.
                    </p>
                    <p>
                        Les informations d'une page sont considérées comme valides lorsqu'un certain nombre de personnes les ont validées grâce au bouton "Valider les informations de la personne" présent sur le profil.
                    </p>
                    <p>
                        En pourcentage, il y a très peu d'utilisateurs avec des données erronées, et la plupart du temps c'est parce que la mise en page d'une page Wikipédia n'est pas uniforme d'une page à l'autre, donc c'est compliqué pour mon code.
                    </p>
                    <p>
                        De même, toutes les nouveautés apportées aux pages après le 23 février 2026 (personnes décédées, nouveaux liens ajoutés sur une page, nouvelles informations, etc.) ne sont pas disponibles sur le site hors signalement individuel.
                        Le projet est opensource et disponible ici : <a className={link_class} href="https://github.com/steevenakintilo/WikipediaPeopleMap" target="_blank" rel="noopener noreferrer">WikipediaPeopleMap</a>
                    </p>
                </AccordionContent>
            </AccordionItem>

            <AccordionItem value="other">
                <AccordionTrigger className="text-base">Autre</AccordionTrigger>

                <AccordionContent>
                    <p>
                        Toutes les informations présentes sur ce site proviennent de Wikipédia et ne m’appartiennent pas.
                    </p>

                    <p>
                        Le logo du site provient de ce <a className={link_class} href="https://helloartsy.com/how-to-draw-an-earth/" target="_blank" rel="noopener noreferrer">site</a>
                    </p>
                </AccordionContent>
            </AccordionItem>
        </Accordion>
    </main>

  );
};

export default About;
