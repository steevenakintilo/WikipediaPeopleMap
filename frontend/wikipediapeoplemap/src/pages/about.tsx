import 'bootstrap/dist/css/bootstrap.min.css';

import "../utils/global.css";
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { Accordion } from 'react-bootstrap';

const About = () => {

   return (

    <div className="container">
        <div
            className=""
        >
            <div className="">

                <br></br>
                
                <div className="d-grid gap-2">
                    <a type="button" className="btn btn-secondary btn-xl" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
                </div>
                
                <br></br>
                <br></br>

                <Accordion>
                    <Accordion.Item eventKey="0">
                        <Accordion.Header>
                            <strong style={{ fontSize: "30px" }}>
                                - Explication du site
                            </strong>
                        </Accordion.Header>

                        <Accordion.Body>
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
                        </Accordion.Body>
                    </Accordion.Item>
                </Accordion>
                
                <br></br>
                <Accordion>
                    <Accordion.Item eventKey="0">
                        <Accordion.Header>
                            <strong style={{ fontSize: "30px" }}>
                                - Comment marche le calcule du classement?
                            </strong>
                        </Accordion.Header>

                        <Accordion.Body>
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
                            </p>

                        </Accordion.Body>
                    </Accordion.Item>
                </Accordion>
                
                <br></br>
                <Accordion>
                    <Accordion.Item eventKey="0">
                        <Accordion.Header>
                            <strong style={{ fontSize: "30px" }}>
                                - Explication technique
                            </strong>
                        </Accordion.Header>

                        <Accordion.Body>
                            <p>
                                Voici quelques explications techniques pour ceux que ça intéresse.
                                Le site a été codé en React + Vite avec TypeScript, avec une interface UI/UX basée sur Bootstrap. Côté backend, il fonctionne avec Django et une base de données SQL.
                            </p>

                            <p>    
                                Pour récupérer les informations des pages Wikipédia, j’ai téléchargé le fichier ZIM de Wikipédia en français du 23 février 2026 puis j’ai créé un script python permettant de récupérer uniquement les personnes ayant réellement existé.
                            </p>
                            <p>
                                J’ai ensuite développé un script permettant de récupérer les informations de chaque page. Le script fonctionne bien, mais il est impossible de garantir une récupération des informations à 100% pour plus de 700 000 pages.
                            </p>
                            <p>
                                Pour essayer d'avoir des données de meilleure qualité, je peux essayer de télécharger une version locale de Wikidata, qui fait techniquement exactement ce que je cherche, même si je trouve que du coup ça mâche quasiment tout le travail si tout est fait à ta place.
                                De plus, même Wikidata, pourtant un site officiel, n'a pas non plus toutes les données pour chaque utilisateur.
                                Comme autre solution, je pourrais proposer un système de collaboration comme Wikipédia : sur chaque page, je rajoute un bouton « Signaler un utilisateur » et la personne pourra écrire les infos manquantes/erronées sur l'utilisateur, et moi je pourrai voir les infos pour choisir si oui ou non elles sont pertinentes.
                            </p>
                            <p>
                                En pourcentage, il y a très peu d'utilisateurs avec des données erronées, et la plupart du temps c'est parce que la mise en page d'une page Wikipédia n'est pas uniforme d'une page à l'autre, donc c'est compliqué pour mon code. De toute façon, on peut choisir de filtrer les utilisateurs par rapport au % de précision de la page.
                            </p>
                            <p>
                                De même, toutes les nouveautés apportées aux pages après le 23 février 2026 (personnes décédées, nouveaux liens ajoutés sur une page, nouvelles informations, etc.) ne sont pas disponibles sur le site.
                                Le projet est opensource et disponible ici: <a href="https://github.com/steevenakintilo/WikipediaPeopleMap" target="_blank" rel="noopener noreferrer">WikipediaPeopleMap</a>
                            </p>

                        </Accordion.Body>
                    </Accordion.Item>
                </Accordion>
                
                <br></br>
                <Accordion>
                    <Accordion.Item eventKey="0">
                        <Accordion.Header>
                            <strong style={{ fontSize: "30px" }}>
                                - Autre
                            </strong>
                        </Accordion.Header>

                        <Accordion.Body>
                            <p>
                                Toutes les informations présentes sur ce site proviennent de Wikipédia et ne m’appartiennent pas.
                            </p>
                            
                            <p>
                                Le logo du site provient de ce <a href="https://helloartsy.com/how-to-draw-an-earth/" target="_blank" rel="noopener noreferrer">site</a>
                            </p>

                        </Accordion.Body>
                    </Accordion.Item>
                </Accordion>
                
                <br></br>
                <br></br>
            </div>
        </div>
            
    </div>
    
  );
};

export default About;