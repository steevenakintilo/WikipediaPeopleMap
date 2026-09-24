"""A file that contain all global variable"""


AGE_GROUP_DICT: dict[str, str] = {
    "-99": "-999 ans",
    "0": "0 à 9 ans",
    "1": "10 à 19 ans",
    "2": "20 à 29 ans",
    "3": "30 à 39 ans",
    "4": "40 à 49 ans",
    "5": "50 à 59 ans",
    "6": "60 à 69 ans",
    "7": "70 à 79 ans",
    "8": "80 à 89 ans",
    "9": "90 à 99 ans",
    "10": "100 à 109 ans",
    "11": "110 à 119 ans",
    "12": "120 à 129 ans",
}

ARRONDISEMENT_LIST_STRING : str = [
    "arrondissement de",
    "Arrondissement de",
    "arrondissements de",
    "Arrondissements de",
    "arrondissement d'",
    "Arrondissement d'",
    "arrondissements d'",
    "Arrondissements d'",                
]        

MONTH_TO_NUMBER_DICT: dict[str, str] = {
    "janvier": "01",
    "fevrier": "02",
    "février": "02",
    "mars": "03",
    "avril": "04",
    "mai": "05",
    "juin": "06",
    "juillet": "07",
    "aout": "08",
    "août": "08",
    "septembre": "09",
    "octobre": "10",
    "novembre": "11",
    "decembre": "12",
    "décembre": "12",
    "fluriel":"13"
}

NUMBER_TO_MONTH_DICT: dict[str, str] = {
    "01": "janvier",
    "02": "février",
    "03": "mars",
    "04": "avril",
    "05": "mai",
    "06": "juin",
    "07": "juillet",
    "08": "août",
    "09": "septembre",
    "10": "octobre",
    "11": "novembre",
    "12": "décembre",
    "13": "fluriel"
}

LIST_OF_MONTH: list[str] = [
    "janvier",
    "février",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "août",
    "septembre",
    "octobre",
    "novembre",
    "décembre",
    "fluriel"
]

LIST_OF_MONTH_CORRECT: list[str] = [
    "janvier",
    "février",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "août",
    "septembre",
    "octobre",
    "novembre",
    "décembre",
    "fluriel"
]

ABSOLUTE_DATE_VALUE: int = 1000000

AFRICA: list[str] = [
    "afrique du sud",
    "algérie",
    "angola",
    "bénin",
    "botswana",
    "burkina faso",
    "burundi",
    "cameroun",
    "cap-vert",
    "république centrafricaine",
    "comores",
    "république du congo",
    "république démocratique du congo",
    "côte d'ivoire",
    "djibouti",
    "égypte",
    "érythrée",
    "eswatini",
    "éthiopie",
    "gabon",
    "gambie",
    "ghana",
    "guinée",
    "guinée-bissau",
    "guinée équatoriale",
    "kenya",
    "lesotho",
    "liberia",
    "libye",
    "madagascar",
    "malawi",
    "mali",
    "maroc",
    "maurice",
    "mauritanie",
    "mozambique",
    "namibie",
    "niger",
    "nigeria",
    "ouganda",
    "rwanda",
    "são tomé-et-principe",
    "sénégal",
    "seychelles",
    "sierra leone",
    "somalie",
    "soudan",
    "soudan du sud",
    "tanzanie",
    "tchad",
    "togo",
    "tunisie",
    "zambie",
    "zimbabwe"
]

AMERICA: list[str] = [
    "antigua-et-barbuda",
    "argentine",
    "bahamas",
    "barbade",
    "belize",
    "bolivie",
    "brésil",
    "canada",
    "chili",
    "colombie",
    "costa rica",
    "cuba",
    "république dominicaine",
    "dominique",
    "équateur",
    "états-unis",
    "grenade",
    "guatemala",
    "guyana",
    "haïti",
    "honduras",
    "jamaïque",
    "mexique",
    "nicaragua",
    "panama",
    "paraguay",
    "pérou",
    "saint-christophe-et-niévès",
    "saint-vincent-et-les grenadines",
    "sainte-lucie",
    "salvador",
    "suriname",
    "trinité-et-tobago",
    "uruguay",
    "venezuela"
]

ASIA: list[str] = [
    "abkhazie",
    "afghanistan",
    "arabie saoudite",
    "arménie",
    "azerbaïdjan",
    "bahreïn",
    "bangladesh",
    "bhoutan",
    "birmanie",
    "brunei",
    "cambodge",
    "chine",
    "chypre",
    "chypre du nord",
    "corée du nord",
    "corée du sud",
    "émirats arabes unis",
    "géorgie",
    "inde",
    "indonésie",
    "irak",
    "iran",
    "israël",
    "japon",
    "jordanie",
    "kazakhstan",
    "kirghizistan",
    "koweït",
    "laos",
    "liban",
    "malaisie",
    "maldives",
    "mongolie",
    "népal",
    "oman",
    "ossétie du sud-alanie",
    "ouzbékistan",
    "pakistan",
    "palestine",
    "philippines",
    "qatar",
    "russie",
    "singapour",
    "sri lanka",
    "syrie",
    "tadjikistan",
    "taïwan",
    "taiwan"
    "thaïlande",
    "timor oriental",
    "turkménistan",
    "turquie",
    "viêt nam",
    "yémen"
]

EUROPE: list[str] = [
    "albanie",
    "allemagne",
    "andorre",
    "angleterre",
    "autriche",
    "belgique",
    "biélorussie",
    "bosnie-herzégovine",
    "bulgarie",
    "croatie",
    "danemark",
    "écosse",
    "espagne",
    "estonie",
    "finlande",
    "france",
    "grèce",
    "hongrie",
    "irlande",
    "irlande du nord",
    "islande",
    "italie",
    "kosovo",
    "lettonie",
    "liechtenstein",
    "lituanie",
    "luxembourg",
    "macédoine",
    "macédoine du nord",
    "malte",
    "moldavie",
    "monaco",
    "monténégro",
    "norvège",
    "pays-bas",
    "pays de galles",
    "pologne",
    "portugal",
    "roumanie",
    "royaume-uni",
    "saint-marin",
    "serbie",
    "slovaquie",
    "slovénie",
    "suède",
    "suisse",
    "république tchèque",
    "ukraine",
    "vatican"
]

OCEANIA: list[str] = [
    "australie",
    "fidji",
    "îles cook",
    "kiribati",
    "îles marshall",
    "micronésie",
    "nauru",
    "niue",
    "nouvelle-zélande",
    "palaos",
    "papouasie-nouvelle-guinée",
    "îles salomon",
    "samoa",
    "tonga",
    "tuvalu",
    "vanuatu"
]

LIST_OF_REGIONS_NAME = [
    "Europe du Nord",
    "Europe de l'Ouest",
    "Europe du Sud",
    "Europe de l'Est",
    "Afrique du Nord",
    "Afrique de l'Ouest",
    "Afrique centrale",
    "Afrique de l'Est",
    "Afrique australe",
    "Moyen-Orient",
    "Asie centrale",
    "Asie de l'Est",
    "Asie du Sud",
    "Asie du Sud-Est",
    "Caucase",
    "Amérique anglo-saxonne",
    "Amérique centrale",
    "Caraïbes",
    "Amérique du Sud",
    "Australasie",
    "Mélanésie",
    "Micronésie",
    "Polynésie",
]

LIST_OF_CONTINENTS: list[str] = [AFRICA,AMERICA,ASIA,EUROPE,OCEANIA]

JOBS: list[str] = [
    "Biathlète",
    "Ingénieur",
    "Empereur",
    "Roi",
    "Reine",
    "Général",
    "auteur-compositeur-interprète",
    "Skipper",
    "Surfeur",
    "Résistant",
    "Écrivain",
    "Ministre du culte",
    "Résistante",
    "Empereur romain"
    "Skieur",
    "Géologue",
    "Vicaire",
    "Expert-comptable",
    "Escrimeuse",
    "Évêque d'Orléans",
    "Général",
    "Golfeur",
    "Skieuse",
    "Tireuse",
    "Pharmacologue",
    "Fondeuse"
    "Écrivain",
    "Auteur",
    "Romancier",
    "Poète",
    "Essayiste",
    "Musicien",
    "Journaliste",
    "Réalisateur",
    "Producteur de cinéma",
    "Scénariste",
    "Acteur",
    "Actrice",
    "Chanteur",
    "Chanteuse",
    "Musicien",
    "Compositeur",
    "Parolier",
    "Producteur musical",
    "Artiste",
    "Peintre",
    "Sculpteur",
    "Photographe",
    "Architecte",
    "Designer",
    "Illustrateur",
    "Dessinateur",
    "Humoriste",
    "Comédien",
    "Présentateur de télévision",
    "Animateur de radio",
    "Animateur de télévision",
    "Mannequin",
    "Danseur",
    "Chorégraphe",
    "Acteur de théâtre",
    "Metteur en scène",
    "Dramaturge",
    "Historien",
    "Philosophe",
    "Sociologue",
    "Anthropologue",
    "Linguiste",
    "Chercheur",
    "Scientifique",
    "Physicien",
    "Chimiste",
    "Mathématicien",
    "Biologiste",
    "Médecin",
    "Psychiatre",
    "Inventeur",
    "Ingénieur",
    "Informaticien",
    "Développeur",
    "Entrepreneur",
    "Homme d'affaires",
    "Femme d'affaires",
    "Industriel",
    "Banquier",
    "Économiste",
    "Juriste",
    "Avocat",
    "Magistrat",
    "Diplomate",
    "Militaire",
    "Officier",
    "Explorateur",
    "Aventurier",
    "Athlète",
    "Footballeur",
    "Basketteur",
    "Tennisman",
    "Pilote automobile",
    "Pilote d'avion",
    "Sportif",
    "Entraîneur sportif",
    "Joueur d'échecs",
    "Chef cuisinier",
    "Cuisinier",
    "Architecte paysagiste",
    "Religieux",
    "Théologien",
    "Prêtre",
    "Moine",
    "Activiste",
    "Militant",
    "Homme politique",
    "Femme politique",
    "Homme d'État"
    "Femme d'État"
    "Député",
    "Président",
    "Premier ministre",
    "Roi",
    "Reine",
    "Prince",
    "Professeur",
    "Enseignant",
    "Universitaire",
    "Critique littéraire",
    "Critique d'art",
    "Éditeur",
    "Souverain",
    "Prêtre catholique",
    "Claveciniste",
    "Auteur de jeux de société",
    "Prêtre orthodoxe",
    "Ayatollah",
    "Conteur",
    "Pianiste",
    "violoniste et compositeur",
    "pianiste et compositeur",
    "guitariste et compositeur"
    "Personnalité politique",
    "Infirmier",
    "Saxophoniste",
    "Cadi",
    "Personnalité du monde des affaires",
    "Pilote (aviation)",
    "Charpentier",
    "Rabbin",
    "Artiste peintre",
    "Ingénieur civil",
    "Lama (bouddhisme)",
    "Astronome",
    "Maître spirituel",
    "Botaniste",
    "Violoncelliste",
    "Maréchal",
    "Commissaire aux comptes",
    "Groupie",
    "Amateur",
    "Artiste lyrique",
    "Défenseur des droits de l'homme",
    "Arbitre (football)",
    "Haute fonction publique",
    "Potier (métier)",
    "Vizir",
    "Auteur-compositeur",
    "Syndicaliste",
    "Guitariste",
    "Évêque catholique",
    "Troubadour",
    "Mangaka",
    "Psychologue",
    "Altiste",
    "Illusionniste",
    "Instituteur",
    "Avocat (métier)",
    "Pasteur (christianisme)",
    "Producteur de télévision",
    "Directeur de la photographie",
    "Financier",
    "Urgentiste",
    "Barde (poète gael)",
    "Graphiste",
    "Homme politique",
    "Femme politique"
    "Disc jockey",
    "Chef d'orchestre",
    "Maître écrivain",
    "Consultant",
    "Caricaturiste",
    "Peintre de cour",
    "Corsaire",
    "Styliste",
    "Harpiste",
    "Metteur en scène",
    "Créateur de caractères",
    "Sculpteur",
    "Influenceur web",
    "Marchand d'art",
    "Vitrailliste",
    "Administrateur colonial",
    "Homme d'État",
    "Attachée de presse",
    "Policier",
    "Entomologiste",
    "Marchand (commerce)",
    "Mannequin",
    "Musicien électronique",
    "Plasticien",
    "Sage-femme",
    "Artiste contemporain",
    "Capitaine de navire",
    "Réalisateur de télévision",
    "Chroniqueur (littéraire)",
    "Abbesse",
    "Violoniste",
    "Publiciste",
    "Sexologue",
    "Trompettiste",
    "Ingénieur du son",
    "Critique de cinéma",
    "Patineur artistique",
    "Artiste plasticienne",
    "Acteur de doublage",
    "Cascadeur",
    "Journaliste sportif",
    "Torero",
    "Fleuriste",
    "Archiviste",
    "Bassiste",
    "Chercheur universitaire",
    "Chercheur en",
    "Président",
    "Présidente"
    "Chercheuse en",  
    "Restaurateur d'art",
    "Dessinateur humoristique",
    "Librettiste",
    "Dialoguiste",
    "Cryptographe",
    "Musicologue",
    "Parasitologue",
    "Anthropologue",
    "Reporter",
    "Conquistador",
    "Producteur de radio",
    "Paysagiste",
    "Chirurgien",
    "Agriculteur",
    "Heilpraktiker",
    "Vigneron",
    "Pilote (profession maritime)",
    "Directeur de casting",
    "Modiste",
    "Naturaliste",
    "Cow-boy",
    "Sommelier",
    "Monteur son",
    "Luthier",
    "Éleveur équin",
    "Historien",
    "Historien de la philosophie",
    "Humoriste",
    "Pharmacien",
    "Pâtissier",
    "Parfumeur",
    "Jardinier",
    "Guide de haute montagne",
    "Narrateur",
    "Horloger",
    "Navigateur (marine)",
    "Architecte naval",
    "Seigneur de guerre",
    "Juge",
    "Conservateur de musée",
    "Conservateur du patrimoine",
    "Relieur",
    "Photographe",
    "Orfèvre",
    "Notaire",
    "Entrepreneur",
    "Directeur des ressources humaines",
    "Commissaire d'exposition",
    "Bassoniste",
    "Tromboniste",
    "Tailleur de pierre",
    "Viticulteur",
    "Écuyer",
    "Libraire",
    "Fonctionnaire impérial",
    "Zoologiste",
    "Photographe plasticien",
    "Agent de renseignement",
    "Maquilleur",
    "Conducteur de train",
    "Vacher",
    "Instrumentiste",
    "Ingénieur logiciel",
    "Radioamateur",
    "Espion",
    "Maître à danser",
    "Facteur d'orgues",
    "Affichiste",
    "Éditeur (métier)",
    "Armateur",
    "Corniste",
    "Sénéchal",
    "Microbiologiste",
    "Facteur de pianos",
    "Barrister",
    "Reporter-photographe",
    "Statisticien",
    "Monteur",
    "Coiffeur",
    "Skipper",
    "Professeur documentaliste",
    "Sommelier",
    "Coiffeur",
    "Professeur (enseignant)",
    "Investisseur",
    "Docteur en médecine",
    "Vidéaste web",
    "Artiste de rue",
    "Géographe",
    "Tueur à gages",
    "Intelligence artificielle (chercheur)",
    "Busshi",
    "Chaman",
    "Boulanger",
    "Écrivain voyageur",
    "Dessinateur de bande dessinée",
    "Scénariste de bande dessinée",
    "Président-directeur général",
    "Scribe",
    "Youtubeur virtuel",
    "Directeur littéraire",
    "Producteur de cinéma",
    "Chef militaire",
    "Illustrateur botanique",
    "Lexicographe",
    "Fondeur de cloches",
    "Productrice de cinéma",
    "Directeur artistique",
    "Correspondant local de presse",
    "Tatoueur",
    "Modèle (art)",
    "Pathologiste",
    "Écrivain public",
    "Critique de vin",
    "Promoteur immobilier",
    "Dirigeant",
    "Sommelier",
    "Lissier",
    "Professeur documentaliste",
    "Chocolatier",
    "Horloger",
    "Architecte",
    "Marin (profession)",
    "Assistant réalisateur",
    "Typographe",
    "Écrivaine",
    "Reporter",
    "Conquistador",
    "Griot",
    "Photographe de mode",
    "Monteur",
    "Dramaturge",
    "Professeur",
    "Superviseur des effets visuels",
    "Producteur de jeux vidéo",
    "Maquilleur",
    "Paysagiste",
    "Chocolatier",
    "Tailleur de pierre",
    "Chef de chœur",
    "Correspondant de guerre",
    "Chef opérateur",
    "Directeur de théâtre",
    "Marin",
    "Skipper",
    "Viticulteur",
    "Conseiller d'État",
    "Trésorier",
    "Agent de change",
    "Forgeron",
    "Art numérique (artiste)",
    "Fondeur",
    "Ingénieur militaire",
    "Ingénieur agronome",
    "Urbaniste",
    "Spin doctor",
    "Chef de produit",
    "Trésorier (comptabilité)",
    "Directeur",
    "Chef d'entreprise",
    "Restaurateur",
    "Banquier d'affaires",
    "Conservateur du patrimoine",
    "Relieur",
    "Pharmacien",
    "Marchand mercier",
    "Jardinier",
    "Capitaine",
    "Docteur",
    "Scientifique",
    "Programmeur",
    "Développeur",
    "Ingénieur",
    "Autrice",
    "Romancière",
    "Poétesse",
    "Essayiste",  # épicène
    "Musicienne",
    "Journaliste",  # épicène
    "Réalisatrice",
    "Productrice musicale",
    "Compositrice",
    "Parolière",
    "Peintre",  # épicène
    "Sculptrice",
    "Photographe",  # épicène
    "Architecte",  # épicène
    "Designeuse",
    "Illustratrice",
    "Dessinatrice",
    "Humoriste",  # épicène
    "Comédienne",
    "Présentatrice de télévision",
    "Animatrice de radio",
    "Animatrice de télévision",
    "Danseuse",
    "Chorégraphe",  # épicène
    "Actrice de théâtre",
    "Metteuse en scène",
    "Historienne",
    "Philosophe",  # épicène
    "Sociologue",  # épicène
    "Anthropologue",  # épicène
    "Linguiste",  # épicène
    "Chercheuse",
    "Scientifique",  # épicène
    "Physicienne",
    "Chimiste",
    "Mathématicienne",
    "Biologiste",
    "Médecin",  # épicène
    "Psychiatre",  # épicène
    "Inventrice",
    "Ingénieure",
    "Informaticienne",
    "Développeuse",
    "Entrepreneuse",
    "Industrielle",
    "Banquière",
    "Économiste",  # épicène
    "Juriste",  # épicène
    "Avocate",
    "Magistrate",
    "Diplomate",  # épicène
    "Militaire",  # épicène
    "Officière",
    "Exploratrice",
    "Aventurière",
    "Athlète",  # épicène
    "Footballeuse",
    "Basketteuse",
    "Joueuse de tennis",
    "Pilote automobile",  # épicène
    "Pilote d'avion",  # épicène
    "Sportive",
    "Entraîneuse sportive",
    "Joueuse d'échecs",
    "Cheffe cuisinière",
    "Cuisinière",
    "Religieuse",
    "Théologienne",
    "Prêtresse",
    "Moniale",
    "Activiste",  # épicène
    "Militante",
    "Députée",
    "Présidente",
    "Première ministre",
    "Princesse",
    "Professeure",
    "Enseignante",
    "Universitaire",  # épicène
    "Critique littéraire",  # épicène
    "Critique d'art",  # épicène
    "Éditrice",
    "Souveraine",
    "Claveciniste",  # épicène
    "Autrice de jeux de société",
    "Conteuse",
    "Pianiste",  # épicène
    "Personnalité politique",  # épicène
    "Infirmière",
    "Saxophoniste",  # épicène
    "Cadie",
    "Charpentière",
    "Rabbine",
    "Astronome",  # épicène
    "Botaniste",  # épicène
    "Violoncelliste",  # épicène
    "Commissaire aux comptes",  # épicène
    "Artiste lyrique",  # épicène
    "Défenseuse des droits de l'homme",
    "Arbitre",
    "Potière",
    "Autrice-compositrice",
    "Syndicaliste",  # épicène
    "Guitariste",  # épicène
    "Mangaka",  # épicène
    "Psychologue",  # épicène
    "Altiste",  # épicène
    "Illusionniste",  # épicène
    "Institutrice",
    "Productrice de télévision",
    "Directrice de la photographie",
    "Financière",
    "Urgentiste",  # épicène
    "Graphiste",  # épicène
    "Disc-jockey",
    "Cheffe d'orchestre",
    "Consultante",
    "Caricaturiste",  # épicène
    "Peintre de cour",  # épicène
    "Corsaire",  # épicène
    "Créatrice de caractères",
    "Influenceuse web",
    "Marchande d'art",
    "Vitrailliste",  # épicène
    "Administratrice coloniale",
    "Policière",
    "Entomologiste",  # épicène
    "Marchande",
    "Musicienne électronique",
    "Plasticienne",
    "Capitaine de navire",  # épicène
    "Réalisatrice de télévision",
    "Chroniqueuse",
    "Publicitaire",
    "Sexologue",  # épicène
    "Trompettiste",  # épicène
    "Ingénieure du son",
    "Critique de cinéma",  # épicène
    "Patineuse artistique",
    "Actrice de doublage",
    "Cascadeuse",
    "Journaliste sportive",
    "Fleuriste",  # épicène
    "Archiviste",  # épicène
    "Bassiste",  # épicène
    "Chercheuse universitaire",
    "Restauratrice d'art",
    "Dessinatrice humoristique",
    "Librettiste",  # épicène
    "Directrice générale",
    "Dialoguiste",  # épicène
    "Cryptographe",  # épicène
    "Musicologue",  # épicène
    "Parasitologue",  # épicène
    "Reporteuse",
    "Chirurgienne",
    "Agricultrice",
    "Vigneronne",
    "Directrice de casting",
    "Naturaliste",  # épicène
    "Cow-girl",
    "Sommelière",
    "Monteuse son",
    "Luthière",
    "Éleveuse équine",
    "Pharmacienne",
    "Pâtissière",
    "Parfumeuse",
    "Jardinière",
    "Guide de haute montagne",  # épicène
    "Narratrice",
    "Horlogère",
    "Navigatrice",
    "Juge",  # épicène
    "Conservatrice de musée",
    "Conservatrice du patrimoine",
    "Relieuse",
    "Orfèvre",  # Orfévesse est très rare
    "Notaire",  # épicène
    "Directrice des ressources humaines",
    "Commissaire d'exposition",  # épicène
    "Bassoniste",  # épicène
    "Tromboniste",  # épicène
    "Tailleuse de pierre",
    "Viticultrice",
    "Écuyère",
    "Libraire",  # épicène
    "Zoologiste",  # épicène
    "Photographe plasticienne",
    "Agente de renseignement",
    "Maquilleuse",
    "Conductrice de train",
    "Vachère",
    "Instrumentiste",  # épicène
    "Ingénieure logiciel",
    "Espionne",
    "Affichiste",  # épicène
    "Éditrice",
    "Armatrice",
    "Corniste",  # épicène
    "Microbiologiste",  # épicène
    "Factrice de pianos",
    "Statisticienne",
    "Monteuse",
    "Coiffeuse",
    "Skipeuse",
    "Professeure documentaliste",
    "Investisseuse",
    "Docteure en médecine",
    "Vidéaste web",  # épicène
    "Boulangère",
    "Écrivaine voyageuse",
    "Dessinatrice de bande dessinée",
    "Scénariste de bande dessinée",  # épicène
    "Présidente-directrice générale",
    "Scribe",  # épicène
    "Youtubeuse virtuelle",
    "Directrice littéraire",
    "Cheffe militaire",
    "Illustratrice botanique",
    "Lexicographe",  # épicène
    "Directrice artistique",
    "Correspondante locale de presse",
    "Tatoueuse",
    "Pathologiste",  # épicène
    "Écrivaine publique",
    "Critique de vin",  # épicène
    "Promotrice immobilière",
    "Dirigeante",
    "Lissière",
    "Assistante réalisatrice",
    "Typographe",  # épicène
    "Griotte",
    "Photographe de mode",  # épicène
    "Superviseuse des effets visuels",
    "Productrice de jeux vidéo",
    "Cheffe de chœur",
    "Correspondante de guerre",
    "Cheffe opératrice",
    "Directrice de théâtre",
    "Marinière",
    "Conseillère d'État",
    "Trésorière",
    "Agente de change",
    "Forgeronne",
    "Fondeuse",
    "Ingénieure militaire",
    "Ingénieure agronome",
    "Urbaniste",  # épicène
    "Cheffe de produit",
    "Trésorière (comptabilité)",
    "Directrice",
    "Cheffe d'entreprise",
    "Restauratrice",
    "Banquière d'affaires",
    "Programmeuse",
     "Antiquaire",
    "Apiculteur",
    "Apicultrice",
    "Archer",
    "Archère",
    "Archevêque",
    "Artiste-peintre",
    "Armurier",
    "Armurière",
    "Auteur de littérature pour la jeunesse",
    "Autrice de littérature pour la jeunesse",
    "Auteur-compositeur-interprète",
    "Autrice-compositrice-interprète",
    "Autrice-compositrice-interprète",
    "Banderillero",
    "Banderillera",
    "Bandit",
    "Bandite",
    "Berger",
    "Bergère",
    "Bienheureux",
    "Bienheureuse",
    "Bushi",
    "Calligraphe",
    "Chapelain",
    "Chapelaine",
    "Chanoinesse",
    "Chorévêque",
    "Choriste",
    "Colonel",
    "Collectionneur",
    "Collectionneuse",
    "Concepteur de jeu",
    "Conceptrice de jeu",
    "Conseiller Pôle emploi",
    "Conseillère Pôle emploi",
    "Contrebandier",
    "Contrebandière",
    "Courtisan",
    "Courtisane",
    "Cyberdissident",
    "Cyberdissidente",
    "Diariste",
    "Doge",
    "Drogman",
    "Duc",
    "Duchesse",
    "Escroc",
    "Escroque",
    "Évêque",
    "Fonctionnaire",
    "Folkloriste",
    "Généticien",
    "Généticienne",
    "Gentilhomme",
    "Gentilfemme",
    "Gladiateur",
    "Gladiatrice",
    "Graveur sur cuivre",
    "Graveuse sur cuivre",
    "Haut fonctionnaire",
    "Haute fonctionnaire",
    "Horticulteur",
    "Horticultrice",
    "Hydrographe",
    "Imprimeur",
    "Imprimeuse",
    "Interprète",
    "Lama",
    "Lobbyiste",
    "Manhwaga",
    "Margrave",
    "Menuisier",
    "Menuisière",
    "Ministre",
    "Modéliste",
    "Ninja",
    "Nourrice",
    "Orateur",
    "Oratrice",
    "Pasteur",
    "Pasteure",
    "Plâtrier",
    "Plâtrière",
    "Prélat",
    "Prêtresse catholique",
    "Professeur d'université",
    "Professeure d'université",
    "Rappeur",
    "Rappeuse",
    "Réalisateur de cinéma",
    "Réalisatrice de cinéma",
    "Réalisateur artistique",
    "Réalisatrice artistique",
    "Rosh yeshiva",
    "Scalde",
    "Serrurier",
    "Serrurière",
    "Soldat",
    "Soldate",
    "Solliciteur",
    "Sollicitrice",
    "Soudeur",
    "Soudeuse",
    "Sophiste",
    "Sous-diacre",
    "Sultan",
    "Sultane",
    "Tailleur",
    "Tailleuse",
    "Tlatoani",
    "Trouvère",
    "Trouveresse",
    "Vétérinaire",
    "Vogt",
    "Volcanologue",
    "Bhikkhuni"
]

CITIES: list[str] = [
    "Houston",
    "Marseille",
    "Alger",
    "Ouagadougou",
    "Dakar",
    "Bamberg",
    "Vérone",
    "Norrköping",
    "Orléans",
    "Netzschkau",
    "Sandnes",
    "Šibenik",
    "Vismes",
    "Amerongen",
    "Somerset",
    "Tiel",
    "Issy-les-Moulineaux",
    "Villepreux",
    "Soultz-Haut-Rhin",
    "Tchiprovtsi",
    "Tezpur",
    "Tychy",
    "Ghaziabad",
    "Visby",
    "Schneidemühl",
    "Indore",
    "Bethania",
    "Belgrade",
    "Cheltenham",
    "Nagercoil",
    "Ascain",
    "Apt",
    "Pau",
    "Wilchingen"
    "Abidjan",
    "Auxerre",
    "Onitsha",
    "Brisbane",
    "Dwikozy",
    "Southsea",
    "Ulm",
    "Marles-les-Mines"
    "Cebreros",
    "Montoire-sur-le-Loir",
    "Pulsnitz",
    "Villeurbanne",
    "Noranda"
    "Bongouanou",
    "Meilen",
    "Potsdam",
    "Yaté",
    "Hollerich",
    "Ribeauvillé",
    "Bogota",
    "Rome",
    "Paris",
    "Rosières",
    "Montréal",
    "Chicoutimi",
    "Roura",
    "Aoste",
    "Munich",
    "Lille",
    "Namur",
    "Meknès",
    "Tanger",
    "Tizi Ouzou",
    "Tan-Tan",
    "Nzérékoré",
    "Philadelphie",
    "Vesoul",
    "Nîmes",
    "Bourg-en-Bresse",
    "Lannion",
    "Saïgon",
    "Douala",
    "Nanterre",
    "Schaerbeek",
    "Tivoli",
    "Hambourg",
    "Männedorf",
    "Bordeaux",
    "Garnsee",
    "Reims",
    "Meißen",
    "Zurich",
    "Coppet",
    "Bône",
    "Salmaise",
    "Genève",
    "Budapest",
    "Francfort-sur-le-Main",
    "Wurtzbourg",
    "Eichstätt",
    "Näples",
    "Barranquilla",
    "Königsberg",
    "Berlin",
    "Berlin-Spandau",
    "Aberdeen",
    "Lausanne",
    "Drummondville",
    "Annemasse",
    "Moscou",
    "Saint-Pierre-en-Val",
    "Port-au-Prince",
    "Vincennes",
    "Colmar",
    "Chartres",
    "Anduze",
    "Weimar",
    "Sydney",
    "Nazareth",
    "Zanzibar",
    "Shanghai",
    "Charquemont",
    "Fatick",
    "Meyrin",
    "Aix-en-Provence",
    "Kaunas",
    "Montemor-o-Novo",
    "Ploudalmézeau",
    "Amiens",
    "Néfiach",
    "Saint-Jean",
    "Linguère",
    "Bolton",
    "Louga",
    "Naplouse",
    "Zacatecas",
    "Stendal",
    "Saint-Pierre-de-Sorel",
    "Libreville",
    "Bignona",
    "Tournai",
    "Santos",
    "Avallon",
    "Aarhus",
    "Bologne",
    "Belluno",
    "Santiago",
    "Venise",
    "Amberg",
    "Aalen",
    "Lviv",
    "Chełm Śląski",
    "Gourdinne",
    "Rivesaltes",
    "Victoriaville",
    "Marnes-la-Coquette",
    "Tchortkiv",
    "Saint-Julien-en-Born",
    "Wamba",
    "Fréjus",
    "Commercy",
    "Yzeure",
    "Lunel",
    "Maastricht",
    "Rhyl",
    "Chicago",
    "Greifswald",
    "Calvi",
    "Crémone",
    "Londres",
    "Frederiksberg",
    "Asciano",
    "Dubăsari",
    "Saint-Mihiel",
    "Denain",
    "Lyon",
    "Saint-Avold",
    "Puylaurens",
    "Poperinge",
    "Helsinki",
    "Cambrai",
    "Lübeck",
    "Mantes-la-Ville",
    "Holwierde",
    "Saint-Étienne",
    "Boma",
    "Boston",
    "Kiel",
    "Strasbourg",
    "Bruxelles",
    "Charleroi",
    "Lunéville",
    "Vienne",
    "Salzbourg",
    "Copenhague",
    "Salon-de-Provence",
    "Milan",
    "Campobasso",
    "Montevideo",
    "Messine",
    "Antananarivo",
    "Cyrène",
    "Angers",
    "Saint-Nicolas-d'Aliermont",
    "Durango",
    "Perpignan",
    "Nevers",
    "Vichy",
    "Dresde",
    "Brünn",
    "Prague",
    "Beyrouth",
    "Kyoustendil",
    "Téhéran",
    "Culhuacan",
    "Wetzlar",
    "Stargard",
    "Champsecret",
    "Neuchâtel",
    "Quimper",
    "Nyon",
    "Ensival",
    "Besançon",
    "Darmstadt",
    "Vilvorde",
    "Rotterdam",
    "Conques",
    "Orange",
    "Las Palmas de Gran Canaria",
    "Ankara",
    "Marsan",
    "Istanbul",
    "Bambey",
    "Épinay-sur-Seine",
    "Caracas",
    "Kinshasa",
    "Goma",
    "Bellinzone",
    "Porto-Novo",
    "Ostende",
    "Szamocin",
    "Morges",
    "Yamoussoukro",
    "Dunmurry",
    "Tacoma",
    "Pontevedra",
    "Galați",
    "Dunkerque",
    "Metz",
    "Kilkenny",
    "Tunis",
    "Toulouse",
    "Comè",
    "Biarritz",
    "Chantilly",
    "Wavre",
    "Saint-Paul-en-Jarez",
    "Firminy",
    "Macenta",
    "Orgerus",
    "Hof-sur-Saale",
    "Stralsund",
    "Vence",
    "Lorient",
    "Newark",
    "Yankton",
    "Linz",
    "Varsovie",
    "Bălți",
    "Saint",
    "Lecce",
    "Fredericton",
    "Dubrovnik",
    "Zagreb",
    "Winnipeg",
    "Mazamet",
    "Toronto",
    "Sieradz",
    "Livourne",
    "Boulogne-Billancourt",
    "Tallinn",
    "Oslo",
    "Springfield",
    "Essex",
    "Gassin",
    "Stockton-on-Tees",
    "Tournan-en-Brie",
    "Lassy",
    "Voujeaucourt",
    "Givors",
    "Maui",
    "Rheine",
    "Brême",
    "Trostberg",
    "Gransee",
    "Barcelone",
    "Florence",
    "Catanzaro",
    "Bissen",
    "Albacete",
    "Neuilly-sur-Seine",
    "Mexico",
    "Cles",
    "Gand",
    "Nice",
    "Ixelles",
    "Auffay",
    "Purmerland",
    "Douarnenez",
    "Uccle",
    "Frasnes-lez-Buissenal",
    "Sedan",
    "Iași",
    "Saint-Louis",
    "Brazzaville",
    "Saint-Nicolas",
    "Colombes",
    "Krefeld",
    "Leuze-en-Hainaut",
    "Rodez",
    "Carhaix-Plouguer",
    "Bronx",
    "Alost",
    "Épinal",
    "Hanoï",
    "Saint-Raymond",
    "Genlis",
    "Bondy",
    "Dole",
    "Burzaco",
    "Cúcuta",
    "Aubervilliers",
    "Bienne",
    "Brissago",
    "Antigonish",
    "Dortmund",
    "Lignol",
    "London",
    "Bucarest",
    "Burgos",
    "Sarreguemines",
    "Amsterdam",
    "Détroit",
    "Delémont",
    "Belfort",
    "Whitehorse",
    "Skopje",
    "Saint-Yrieix-la-Perche",
    "Gatineau",
    "Medellín",
    "Mont-Joli",
    "Kaolack",
    "Souleimaniye",
    "Boise",
    "Trois-Pistoles",
    "Hollywood",
    "Avranches",
    "Kangu",
    "Vinchio",
    "Il-Furjana",
    "Gijón",
    "Benghazi",
    "Saint-Denis",
    "Muralto",
    "Stuttgart",
    "Mayence",
    "Bocaiúva",
    "Addis-Abeba",
    "Cologne",
    "Villemoisson-sur-Orge",
    "Blois",
    "Reus",
    "Chișinău",
    "Kielce",
    "Richmond",
    "Bougouni",
    "Casablanca",
    "Fès",
    "Zhengzhou",
    "Bombay",
    "Sacramento",
    "Wiesbaden",
    "Pointe-à-Pitre",
    "Bamenda",
    "Vevey",
    "Berne",
    "Geseke",
    "Rio de Janeiro",
    "Halifax",
    "Dublin",
    "Elora",
    "Saint-Pétersbourg",
    "Lipcani",
    "Gênes",
    "Turin",
    "Gołdap",
    "Clervaux",
    "Bridgend",
    "Guéret",
    "Rougé",
    "Curitiba",
    "Pont-en-Royans",
    "LaSalle",
    "Leeds",
    "Remscheid",
    "Zwickau",
    "Brno",
    "Ramnäs",
    "Yaoundé",
    "Nancy",
    "Villarzel",
    "Frouard",
    "Lisbonne",
    "Leipzig",
    "Snowidza",
    "Schlieben",
    "Cassel",
    "Kleinobringen",
    "Vendenheim",
    "Anvers",
    "Nevele",
    "Casalmaggiore",
    "Crissier",
    "Malansac",
    "Laval",
    "Mbujimayi",
    "Carcassonne",
    "Alençon",
    "Rouen",
    "Ludwigshafen",
    "Béziers",
    "Fortaleza",
    "Gävle",
    "Grenoble",
    "Ladimirevci",
    "Gaziantep",
    "Tshikapa",
    "Parme",
    "Písek",
    "Craon",
    "Bytów",
    "Wessin",
    "Magdebourg",
    "Aplahoué",
    "Cholet",
    "Arleuf",
    "Garessio",
    "Ternitz",
    "Presbourg",
    "Évry-Courcouronnes",
    "Velika Kladuša",
    "Molfetta",
    "Butembo",
    "Dijon",
    "Sarrebourg",
    "São Paulo",
    "Cagnes-sur-Mer",
    "La Haye",
    "Crotone",
    "Charlesbourg",
    "Cognac",
    "León",
    "Zamora",
    "Valladolid",
    "Ivano-Frankivsk",
    "Limoges",
    "Lazise",
    "Brooklyn",
    "Dorsten",
    "Aix-la-Chapelle",
    "Achern",
    "Vallorbe",
    "Asmara",
    "Mirande",
    "Rennes",
    "Sète",
    "Brest",
    "Cap-Chat",
    "Luc-la-Primaube",
    "Douai",
    "Cuarny",
    "Ébreuil",
    "Clarmont",
    "Cracovie",
    "Olmütz",
    "Brugg",
    "Graz",
    "Hanovre",
    "Mannheim",
    "Wiltz",
    "Bobo-Dioulasso",
    "Villecresnes",
    "Brive-la-Gaillarde",
    "Pontedeume",
    "Bourg-Saint-Andéol",
    "Dambach-la-Ville",
    "Haine-Saint-Paul",
    "Lessines",
    "Oakland",
    "Pérouse",
    "Goilberdingen",
    "Vergt",
    "Bora-Bora",
    "Coire",
    "Baltimore",
    "Pasadena",
    "Indianapolis",
    "Kroppenstedt",
    "Abbeville",
    "Recife",
    "Erfurt",
    "Tianjin",
    "Amélie-les-Bains",
    "Cincinnati",
    "Lugano",
    "Merano",
    "Agde",
    "Athènes",
    "Brescia",
    "Corridonia",
    "Imola",
    "Gubbio",
    "Kyoto",
    "Jodhpur",
    "Bruges",
    "Vicence",
    "Roubaix",
    "Mascouche",
    "Stockholm",
    "Cossonay",
    "Fontainebleau",
    "Thoune",
    "Rimouski",
    "Trois-Rivières",
    "Sainte-Marie",
    "Val-d'Or",
    "Lagnieu",
    "Ennery",
    "Melun",
    "Suresnes",
    "Yogyakarta",
    "Taza",
    "Wörgl",
    "Carthage",
    "Bonn",
    "Raeren",
    "Versmold",
    "Malmö",
    "Bâle",
    "Appenzell",
    "Geisenheim",
    "Dallas",
    "Pula",
    "Sprottau",
    "Oranienbourg",
    "Glaris",
    "Kremsmünster",
    "Berlin-Siemensstadt",
    "Chester",
    "Neu-Ulm",
    "Bünde",
    "Longuefuye",
    "Luxeuil-les-Bains",
    "Valjouffrey",
    "Datteln",
    "Narbonne",
    "Bonchamp-lès-Laval",
    "Saint-André-les-Alpes",
    "Grimma",
    "Mauron",
    "Massachusetts",
    "Mauterndorf",
    "Wels",
    "Gnoien",
    "Kukës",
    "Limbourg-sur-la-Lahn",
    "Brwice",
    "Drożyna",
    "Strépy-Bracquegnies",
    "Thiers",
    "Tochigi",
    "Île des Pins",
    "Romans-sur-Isère",
    "Rusutsu",
    "Séoul",
    "Imintanoute",
    "Atlanta",
    "Pékin",
    "Longwy",
    "Bachhagel",
    "Akureyri",
    "Stettin",
    "Bielefeld",
    "Bissau",
    "Gdańsk",
    "Fanjeaux",
    "Arras",
    "Matanzas",
    "Omsk",
    "Yokohama",
    "Novohrad-Volynskyï",
    "Banja Luka",
    "Raubach",
    "Berlin-Schöneberg",
    "Tchernivtsi",
    "Passau",
    "Parakou",
    "Montpellier",
    "Maubeuge",
    "Kalocsa",
    "Reggio de Calabre",
    "Dnipropetrovsk",
    "Yverdon-les-Bains",
    "Cambrils",
    "Montargis",
    "Estagel",
    "Carmaux",
    "Chusclan",
    "Lutry",
    "Granville",
    "Cannes",
    "Saint-Maur-des-Fossés",
    "Aurillac",
    "Saint-Marcellin",
    "Hasparren",
    "Kapurthala",
    "Guayaquil",
    "Sofia",
    "Madrid",
    "Glasgow",
    "Hanna",
    "Saskatoon",
    "Rimini",
    "Palenque",
    "Soleure",
    "Saint-Jérôme",
    "Louny",
    "Cap de Trafalgar",
    "Loubressac",
    "Bonoua",
    "Sartène",
    "Porto-Vecchio",
    "Nantes",
    "Briançon",
    "Loos-en-Gohelle",
    "Civray",
    "Verdun",
    "Mulhouse",
    "Tirlemont",
    "Bapaume",
    "Sud-Kivu",
    "Niort",
    "Galéria",
    "Aignan",
    "Saint-Gilles",
    "Vernon",
    "Souchez",
    "Guengat",
    "Saint-Lô",
    "Warmeriville",
    "Valenciennes",
    "Louviers",
    "Kedgwick",
    "Quaregnon",
    "Fontoy",
    "Flacey-en-Bresse",
    "Périgueux",
    "Angoulême",
    "Poitiers",
    "Forbach",
    "Krattigen",
    "Beaune",
    "Frampton",
    "Berles-au-Bois",
    "Champniers-et-Reilhac",
    "Tours",
    "Bourges",
    "Astaffort",
    "Sainte-Eulalie-en-Born",
    "Rabat",
    "Nouméa",
    "Lapeyrouse",
    "Saint-Isidore",
    "Beauzac",
    "Saint-Sardos",
    "Coarraze",
    "Montivilliers",
    "Vittel",
    "Bastia",
    "Laon",
    "Pistoia",
    "Maisons-Laffitte",
    "Deshaies",
    "Riom",
    "Freetown",
    "Vejle",
    "Incheon",
    "Lima",
    "Eindhoven",
    "Pisco",
    "Dundee",
    "New York",
    "Liverpool",
    "Saint-Jean-sur-Richelieu",
    "Syracuse",
    "Berlin-Charlottenbourg",
    "Wilmington",
    "Saint Catharines",
    "Canterbury",
    "Alderley Edge",
    "Dukinfield",
    "Perwez",
    "Manizales",
    "Witten",
    "Forges-sur-Meuse",
    "Welschenrohr",
    "Berthier-sur-Mer",
    "Bukavu",
    "Neuville-sous-Montreuil",
    "Manhattan",
    "Bayonne",
    "Carnac",
    "Etterbeek",
    "Queens",
    "Beaumont",
    "Melbourne",
    "Offenbach-sur-le-Main",
    "Groix",
    "Bristol",
    "Marbella",
    "Itumbiara",
    "Séville",
    "Alicante",
    "Asuncion",
    "Lokeren",
    "Maceió",
    "Hautmont",
    "Bilbao",
    "Lérida",
    "Pereira",
    "Liège",
    "Saverne",
    "Allouagne",
    "Marvejols",
    "Clermont-Ferrand",
    "Chênée",
    "Rouyn",
    "Nauen",
    "Berlin-Wedding",
    "Klagenfurt",
    "Teplice",
    "Darłowo",
    "Kołobrzeg",
    "Jepara",
    "Gitega",
    "Bunnik",
    "Kashiwa",
    "Montana",
    "Beaconsfield",
    "Shizuoka",
    "Pétion-Ville",
    "Brockton",
    "Cobourg",
    "Sderot",
    "Wendake",
    "Wriezen",
    "Calcutta",
    "Manacor",
    "Cesena",
    "Korhogo",
    "Aalborg",
    "Udine",
    "Caen",
    "Kikwit",
    "Clamart",
    "Saint-Nazaire",
    "Cervia",
    "Raqqa",
    "Yuncheng",
    "Hořovice",
    "Alphen-sur-le-Rhin",
    "Valkenswaard",
    "Sheffield",
    "Tassin-la-Demi-Lune",
    "Narvik",
    "Québec",
    "Karlsruhe",
    "Sukabumi",
    "Valence",
    "Heilly",
    "Suze-la-Rousse",
    "Orbe",
    "La Brévine",
    "Alban",
    "Binche",
    "Rouyn-Noranda",
    "Pointe-Noire",
    "Pernes-les-Fontaines",
    "Nonville",
    "Quéven",
    "Molenbeek-Saint-Jean",
    "Senlis",
    "Frameries",
    "Vire",
    "Louvain",
    "Papeete",
    "Bois-d'Haine",
    "Saint-Amand-les-Eaux",
    "Uppsala",
    "Lynden",
    "Roverbella",
    "Constantine",
    "Vaison-la-Romaine",
    "Mayenne",
    "Ratisbonne",
    "Weinberg",
    "Tübingen",
    "Pittsburgh",
    "Baie-Saint-Paul",
    "Saint-Imier",
    "Saint-Martin-de-Seignanx",
    "Piré-sur-Seiche",
    "Saumur",
    "Thessalonique",
    "Cheyres",
    "Iriba",
    "Ljubljana",
    "Corbeil-Essonnes",
    "Sulzbach-Rosenberg",
    "Sangerhausen",
    "Asnières-sur-Seine",
    "São João da Madeira",
    "Terrebonne",
    "Vierzon",
    "Arlon",
    "Jumet",
    "Pontcey",
    "Murici",
    "Valens",
    "Wieruszów",
    "Inowrocław",
    "Canelones",
    "Buenos Aires",
    "Estamira",
    "Telfes im Stubai",
    "Pont-l'Abbé",
    "Andorre-la-Vieille",
    "Sanok",
    "Göteborg",
    "Meung-sur-Loire",
    "Sherbrooke",
    "Allonville",
    "Fribourg-en-Brisgau",
    "Montluçon",
    "Londerzeel",
    "Healdsburg",
    "Jakarta",
    "Saint-Quentin",
    "Sainte-Anne-de-la-Pocatière",
    "Langolen",
    "Sant'Angelo Lodigiano",
    "Bénévent",
    "Sinaloa",
    "Cosenza",
    "Düren",
    "Vintimille",
    "Souvret",
    "Ouidah",
    "Rybany",
    "Milton",
    "Flobecq",
    "Birmingham",
    "Berlin-Est",
    "Liesek",
    "Withypool",
    "Padoue",
    "Ferrare",
    "Versailles",
    "Mazy",
    "Oucques",
    "Mostaganem",
    "Sienne",
    "Talence",
    "Calgary",
    "Toulon",
    "Chepetivka",
    "Héraklion",
    "Coinches",
    "Estaires",
    "Oujda",
    "Chabanais",
    "Hirson",
    "Avenches",
    "Béguey",
    "Roanne",
    "Genk",
    "Pančevo",
    "Bratislava",
    "Moyeuvre-Grande",
    "Munakata",
    "Hachiōji",
    "Laghouat",
    "Bizerte",
    "Gouda",
    "Baden-Baden",
    "Bergen",
    "Tiaret",
    "Ourossogui",
    "Chêne-Bougeries",
    "Verviers",
    "El Ksiba",
    "Beuvry",
    "Anápolis",
    "Riec-sur-Bélon",
    "Harrisburg",
    "Little Rock",
    "Mississauga",
    "San Salvador",
    "Dassa-Zoumè",
    "Mons",
    "Allemagne-en-Provence",
    "Niedernai",
    "Soissons",
    "Hilversum",
    "Viazma",
    "Yopougon",
    "Bangkok",
    "Opole",
    "Thunder Bay",
    "Phnom-Penh",
    "Lifou",
    "Hartola",
    "Constantinople",
    "Kharkiv",
    "Iéna",
    "Berlaimont",
    "Saint-Julien-en-Genevois",
    "Woluwe-Saint-Lambert",
    "Saint-Jean-de-Luz",
    "Ouahigouya",
    "Milev",
    "Offenbourg",
    "Bandung",
    "Catane",
    "Coblence",
    "Riga",
    "Rufisque",
    "Nantucket",
    "Ludhiana",
    "Bad Kösen",
    "Chiavenna",
    "Vendôme",
    "Loudima",
    "Ninove",
    "Louiseville",
    "Chihuahua",
    "Saint-Joseph",
    "Mantes-la-Jolie",
    "Camphin-en-Carembault",
    "Anglès",
    "Avignon",
    "Montmerle-sur-Saône",
    "Biedermannsdorf",
    "Cottbus",
    "Hachy",
    "Bohicon",
    "Asbestos",
    "Mossoul",
    "Amstetten",
    "Ivanovo",
    "Anorí",
    "Saragosse",
    "Vänersborg",
    "Wellington",
    "Portsmouth",
    "Tenterden",
    "Altenbourg",
    "Rumilly",
    "Bourg-la-Reine",
    "Loches-sur-Ource",
    "Grigny",
    "Zwolle",
    "Palerme",
    "Vipiteno",
    "Colorno",
    "Cahors",
    "Bouchemaine",
    "Guingamp",
    "Champigny-sur-Marne",
    "Queyrac",
    "Noale",
    "Joigny",
    "Hódmezővásárhely",
    "Torrelavega",
    "Wettingen",
    "Malgaches",
    "Gelsenkirchen",
    "Farmville",
    "Cuxac-Cabardès",
    "Joué-lès-Tours",
    "Fort-de-France",
    "Santiago du Chili",
    "Saint-Gall",
    "Quedlinburg",
    "Oelsnitz",
    "Innsbruck",
    "Fauquemont-sur-Gueule",
    "Ebolowa",
    "Castres",
    "Albi",
    "Marcinelle",
    "Beauvais",
    "Chambéry",
    "Aalter",
    "Ajaccio",
    "Iowa",
    "Ath",
    "Schwendi",
    "Saint-Drézéry",
    "Buffalo",
    "Tirana",
    "Milwaukee",
    "Gagnoa",
    "Ostrava",
    "Moudon",
    "Tacaná",
    "Martigny",
    "Bex",
    "Provins",
    "Saint-Jorioz",
    "Nuremberg",
    "Sotchi",
    "Tarragone",
    "Porto",
    "Réghaïa",
    "Labé",
    "Foumban",
    "Bougainville",
    "Praia",
    "Ushuaïa",
    "Kengtung",
    "Cleveland",
    "Salquenen",
    "Aveiro",
    "Puttaparthi",
    "Višegrad",
    "Koszalin",
    "Xalapa",
    "Hopa",
    "Pristina",
    "Saitama",
    "Kankan",
    "Dielsdorf",
    "Kehra",
    "Diegem",
    "Bratsigovo",
    "Duffel",
    "Tbilissi",
    "Port-Gentil",
    "Kikinda",
    "Zehdenick",
    "Talkeetna",
    "Trondheim",
    "Mechhed",
    "Vanves",
    "Kiev",
    "Lisieux",
    "Asti",
    "Elbląg",
    "Rzeszów",
    "Abéché",
    "Vancouver",
    "Hobart",
    "Agadir",
    "Les Cayes",
    "Cowansville",
    "Virton",
    "Linköping",
    "Seclin",
    "Marconne",
    "Hemmingstedt",
    "Odense",
    "Stratford",
    "Rowley",
    "Greystones",
    "Roskilde",
    "Logroño",
    "Beaugency",
    "Randers",
    "Tokyo",
    "Oulan-Bator",
    "Salerne",
    "Lucerne",
    "Oaxaca",
    "Wattwil",
    "Kaysersberg",
    "La Possession",
    "Rawalpindi",
    "Khartsyzk",
    "Zgierz",
    "Esch-sur-Alzette",
    "Kragujevac",
    "Aire-sur-l'Adour",
    "Granges-près-Marnand",
    "Oneglia",
    "Brie-Comte-Robert",
    "Tchibanga",
    "Schleusingen",
    "Oldenbourg",
    "Seligenstadt",
    "Karachi",
    "Shantou",
    "Jacareí",
    "Barth",
    "Duisbourg",
    "Głogów",
    "Neufelden",
    "Youngstown",
    "Höxter",
    "Bressanone",
    "Osterwieck",
    "Hulan",
    "Silvan",
    "Calakmul",
    "Saint-Martin-de-Ré",
    "Saint-Chamond",
    "Chenu",
    "Perros-Guirec",
    "Pont-à-Mousson",
    "Dinant",
    "Monceau-sur-Sambre",
    "Moûtiers",
    "N'Djaména",
    "Hama",
    "Kandi",
    "Pécs",
    "Pforzheim",
    "Ferrol",
    "Bourbon-Lancy",
    "Monteux",
    "Saint-Laurent-de-la-Salanque",
    "Mirecourt",
    "Auberchicourt",
    "Bafia",
    "Boulogne-sur-Mer",
    "Lambézellec",
    "Differdange",
    "Saint-Affrique",
    "Amagne",
    "Suippes",
    "Litomyšl",
    "Caranceja",
    "Hildesheim",
    "Norroy-lès-Pont-à-Mousson",
    "Remiremont",
    "Pretoria",
    "Portalbera",
    "Gozo",
    "Vilosnes",
    "Manchester",
    "Béguédo",
    "Minden",
    "Cruseilles",
    "Bassorah",
    "Saint-Malo",
    "Valdegeña",
    "Étroussat",
    "Fermo",
    "L'Aquila",
    "Malgrate",
    "Calais",
    "Tréméoc",
    "Nagercoil",
    "Ascain",
    "Marles-les-Mines",
    "Netzschkau",
    "Nagercoil",
    "Pau",
    "Wilchingen",
    "Minsk",
    "Brestot",
    "Stockwell",
    "Troyes",
    "Trieste",
    "Argentan",
    "Vientiane",
    "Città di Castello",
    "Évora",
    "Pise",
    "Thonne-le-Thil",
    "Bonaléa",
    "Bellac",
    "Malmedy",
    "Wettolsheim",
    "Carpentras",
    "Mesnil-Saint-Georges",
    "Marnham",
    "Épernay",
    "Putot-en-Auge",
    "Watsonville",
    "Guanghan",
    "Coudures",
    "Sparte",
    "Braga",
    "Langres",
    "Châlons-sur-Marne",
    "Le Caire",
    "Steenwijkerland",
    "Gonesse",
    "Viviez",
    "Cagliari",
    "Auneuil",
    "Boqueho",
    "Gueugnon",
    "Lobbes",
    "Derbyhaven",
    "Mayrac",
    "Riva Valdobbia",
    "Calanda",
    "Kidal",
    "Châlons-en-Champagne",
    "Pézenas",
    "Morlaix",
    "Isle-Saint-Georges",
    "Vannes",
    "Lomé",
    "Bafoussam",
    "Maniwaki",
    "Radstadt",
    "Conflans-Sainte-Honorine",
    "Eboli",
    "Palafrugell",
    "Chalon-sur-Saône",
    "Kairouan",
    "Ilonse",
    "Damas",
    "Tønder",
    "Zerbst",
    "Lindau",
    "Uffholtz",
    "Flessingue",
    "Alexandrie",
    "Marles-les-Mines",
    "Netzschkau",
    "Nagercoil",
    "Ascain",
    "Apt",
    "Pau",
    "Wilchingen",
    "Hué",
    "Norrköping",
    "Solingen",
    "Djeddah",
    "Malines",
    "Bonikowo",
    "Isleworth",
    "Nördlingen",
    "Denver",
    "Marval",
    "Barenton",
    "Tegelen",
    "Lachine",

]

NORTHERN_EUROPE = [
    "Angleterre",
    "Danemark",
    "Estonie",
    "Écosse",
    "Finlande",
    "Irlande",
    "Irlande du Nord",
    "Islande",
    "Lettonie",
    "Lituanie",
    "Norvège",
    "Pays de Galles",
    "Royaume-Uni",
    "Suède",
]

WESTERN_EUROPE = [
    "Allemagne",
    "Andorre",
    "Autriche",
    "Belgique",
    "France",
    "Liechtenstein",
    "Luxembourg",
    "Monaco",
    "Pays-Bas",
    "Suisse",
]

SOUTHERN_EUROPE = [
    "Albanie",
    "Bosnie-Herzégovine",
    "Chypre",
    "Chypre du Nord",
    "Croatie",
    "Espagne",
    "Grèce",
    "Italie",
    "Kosovo",
    "Macédoine",
    "Macédoine du Nord",
    "Malte",
    "Monténégro",
    "Portugal",
    "Saint-Marin",
    "Serbie",
    "Slovénie",
    "Vatican",
]

EASTERN_EUROPE = [
    "Biélorussie",
    "Moldavie",
    "Pologne",
    "République tchèque",
    "Roumanie",
    "Slovaquie",
    "Ukraine",
    "Russie",
]

NORTH_AFRICA = [
    "Algérie",
    "Égypte",
    "Libye",
    "Maroc",
    "Soudan",
    "Tunisie",
]

WEST_AFRICA = [
    "Bénin",
    "Burkina Faso",
    "Cap-Vert",
    "Côte d'Ivoire",
    "Gambie",
    "Ghana",
    "Guinée",
    "Guinée-Bissau",
    "Liberia",
    "Mali",
    "Mauritanie",
    "Niger",
    "Nigeria",
    "Sénégal",
    "Sierra Leone",
    "Togo",
]

CENTRAL_AFRICA = [
    "Angola",
    "Burundi",
    "Cameroun",
    "République centrafricaine",
    "République du Congo",
    "République démocratique du Congo",
    "Gabon",
    "Guinée équatoriale",
    "Rwanda",
    "São Tomé-et-Principe",
    "Tchad",
]

EAST_AFRICA = [
    "Comores",
    "Djibouti",
    "Érythrée",
    "Éthiopie",
    "Kenya",
    "Madagascar",
    "Malawi",
    "Maurice",
    "Mozambique",
    "Ouganda",
    "Seychelles",
    "Somalie",
    "Soudan du Sud",
    "Tanzanie",
    "Zambie",
    "Zimbabwe",
]

SOUTHERN_AFRICA = [
    "Afrique du Sud",
    "Botswana",
    "Eswatini",
    "Lesotho",
    "Namibie",
]

MIDDLE_EAST = [
    "Arabie saoudite",
    "Bahreïn",
    "Émirats arabes unis",
    "Irak",
    "Iran",
    "Israël",
    "Jordanie",
    "Koweït",
    "Liban",
    "Oman",
    "Palestine",
    "Qatar",
    "Syrie",
    "Turquie",
    "Yémen",
]

CENTRAL_ASIA = [
    "Afghanistan",
    "Kazakhstan",
    "Kirghizistan",
    "Ouzbékistan",
    "Tadjikistan",
    "Turkménistan",
]

EAST_ASIA = [
    "Chine",
    "Corée du Nord",
    "Corée du Sud",
    "Japon",
    "Mongolie",
    "Taïwan",
    "Taiwan"
]

SOUTH_ASIA = [
    "Bangladesh",
    "Bhoutan",
    "Inde",
    "Maldives",
    "Népal",
    "Pakistan",
    "Sri Lanka",
]

SOUTHEAST_ASIA = [
    "Birmanie",
    "Brunei",
    "Cambodge",
    "Indonésie",
    "Laos",
    "Malaisie",
    "Philippines",
    "Singapour",
    "Thaïlande",
    "Timor oriental",
    "Viêt Nam",
]

CAUCASUS = [
    "Abkhazie",
    "Arménie",
    "Azerbaïdjan",
    "Géorgie",
    "Ossétie du Sud-Alanie",
]

ANGLO_AMERICA = [
    "Canada",
    "États-Unis",
]

CENTRAL_AMERICA = [
    "Belize",
    "Costa Rica",
    "Guatemala",
    "Honduras",
    "Mexique",
    "Nicaragua",
    "Panama",
    "Salvador",
]

CARIBBEAN = [
    "Antigua-et-Barbuda",
    "Bahamas",
    "Barbade",
    "Cuba",
    "Dominique",
    "Grenade",
    "Haïti",
    "Jamaïque",
    "République dominicaine",
    "Saint-Christophe-et-Niévès",
    "Sainte-Lucie",
    "Saint-Vincent-et-les Grenadines",
    "Trinité-et-Tobago",
]

SOUTH_AMERICA = [
    "Argentine",
    "Bolivie",
    "Brésil",
    "Chili",
    "Colombie",
    "Équateur",
    "Guyana",
    "Paraguay",
    "Pérou",
    "Suriname",
    "Uruguay",
    "Venezuela",
]

AUSTRALASIA = [
    "Australie",
    "Nouvelle-Zélande",
]

MELANESIA = [
    "Fidji",
    "Papouasie-Nouvelle-Guinée",
    "Îles Salomon",
    "Vanuatu",
]

MICRONESIA = [
    "Kiribati",
    "Îles Marshall",
    "Micronésie",
    "Nauru",
    "Palaos",
]

POLYNESIA = [
    "Îles Cook",
    "Niue",
    "Samoa",
    "Tonga",
    "Tuvalu",
]

LIST_OF_REGIONS = [
    NORTHERN_EUROPE,
    WESTERN_EUROPE,
    SOUTHERN_EUROPE,
    EASTERN_EUROPE,
    NORTH_AFRICA,
    WEST_AFRICA,
    CENTRAL_AFRICA,
    EAST_AFRICA,
    SOUTHERN_AFRICA,
    MIDDLE_EAST,
    CENTRAL_ASIA,
    EAST_ASIA,
    SOUTH_ASIA,
    SOUTHEAST_ASIA,
    CAUCASUS,
    ANGLO_AMERICA,
    CENTRAL_AMERICA,
    CARIBBEAN,
    SOUTH_AMERICA,
    AUSTRALASIA,
    MELANESIA,
    MICRONESIA,
    POLYNESIA,
]


MINIMAL_PRECISSENES_SCORE: int = 650
LIST_OF_REAL_PEOPLE_FILEPATH: str = "list_of_wikipedia_page_of_real_people.txt"

HISTORICAL_PERIODS = [
    "Prehistory",
    "Antiquity",
    "Middle Ages",
    "Renaissance",
    "Contemporary Period",
    "Today Time"
]

HISTORICAL_PERIODS_TIME = [
    "-99999"
    "-3300",
    "476",
    "1492",
    "1789",
    "2000"
]

JOBS_PREFIX = [
    # Chefs d'État et de gouvernement
    "chef",
    "Dirigeant de facto",
    "Dirigeant de facto de",
    "Dirigeant de facto des",
    "Dirigeant de facto du",
    "Dirigeant de facto d'",
    "Dirigeant du",
    "Dirigeant de",
    "Dirigeant des",
    "Dirigeant d'",
    "Dirigeante du",
    "Dirigeante de",
    "Dirigeante des",
    "Dirigeante d'",
    "Député à la",
    "Députée à la",
    "Député à l'",
    "Députée à l'",
    "Député aux",
    "Députée aux",
    "membre de la",
    "membre des",
    "membre du",
    "membre de",
    "membre d'"
        
    
            
    "Roi d'Angleterre et d'"
    "Reine d'",
    "Reine des",
    "Reine du",
    "Reine de"
    "Dirigeante de facto de",
    "Dirigeante de facto des",
    "Dirigeante de facto du",
    "Dirigeante de facto d'",
    "Première dame d'",
    "Première dame du",
    "Première dame de",
    "Première dame des",
    "secrétaire du comité exécutif",
    "secrétaire général",
    "Lord-protecteur du",
    "Lord-protecteur d'",
    "Lord-protecteur des",
    "Lord-protecteur de",
    "secrétaire général du ",
    "secrétaire général des",
    "premier secrétaire du",
    "premier secrétaire des",
    "premier secrétaire de",
    "premier secrétaire d'",
    "premiere secrétaire du",
    "premiere secrétaire des",
    "premiere secrétaire de",
    "premiere secrétaire d'",
    "Chef suprême de la",
    "Chef suprême du",
    "Chef suprême des",
    "Chef suprême d'",
    "Cheffe suprême de la",
    "Cheffe suprême du",
    "Cheffe suprême des",
    "Cheffe suprême d'"
    "chef de",
    "chef d'",
    "chef d'État",
    "chef de gouvernement",
    "chef de l'État",
    "chef de l'opposition",
    "reine du royaume-Uni et des",
    "roi du royaume-Uni et des",
    "président",
    "président du",
    "président des",
    "président de",
    "président d'",
    "président élu",
    "président-directeur général",
    "président directeur général",

    "vice-président",
    "vice-président de",
    "vice-président d'",

    "premier ministre",
    "vice-premier ministre",
    "ministre en chef",
    "chancelier",
    "vice-chancelier",
    "directeur général du"
    "directeur général des"
    "directeur général d'"

    # Ministres
    "ministre",
    "ministre de",
    "ministre d'",
    "ministre des",
    "ministre du",
    "ministre de la",
    "ministre de l'",
    "ministre d'État",
    "ministre délégué",
    "secrétaire d'État",

    "ministre des affaires étrangères",
    "ministre de l'intérieur",
    "ministre de la défense",
    "ministre de l'éducation",
    "ministre de la justice",
    "ministre des finances",
    "ministre de la santé",
    "ministre de l'économie",
    "ministre du travail",
    "ministre des transports",
    "ministre de l'agriculture",
    "ministre du développement",
    "ministre du développement national",
    "ministre du développement national et rural",
    "ministre de la culture",
    "ministre de l'environnement",

    # Parlement
    "député",
    "député à la chambre des représentants",
    "député européen",
    "sénateur",
    "parlementaire",
    "Député du",
    "Député de la",
    "Députée de la",
    "Député des",
    "Député de",
    "Député de l'",
    "Députée du",
    "Députée des",
    "Députée de",
    "Députée de l'",
    "Député au",
    "Députée au",
    # Sénateur

    "Sénateur du",
    "Sénateur des",
    "Sénateur de",
    "Sénateur de l'",
    "Sénatrice du",
    "Sénatrice des",
    "Sénatrice de",
    "Sénatrice de l'",

    # Parlementaire

    "Parlementaire du",
    "Parlementaire des",
    "Parlementaire de",
    "Parlementaire de l'",
    "membre du",
    "membres des",
    "membre de",
    "membre d'"
    "membre du parlement",
    "membre de la chambre des représentants",

    # Exécutif territorial
    "gouverneur",
    "gouverneur de",
    "gouverneur d'",
    "gouverneur général",
    "vice-gouverneur",
    "maire",
    "adjoint au maire",
    "préfet",
    "sous-préfet",

    # Diplomatie
    "ambassadeur",
    "haut-commissaire",
    "commissaire",
    "consul",
    "consul général",
    "représentant permanent",
    "représentant de",
    "représentant d'",
    "envoyé spécial",

    # Administration
    "administrateur",
    "administrateur général",

    "directeur",
    "directeur de",
    "directeur d'",
    "directeur général",
    "directeur général de",
    "directeur exécutif",
    "directeur adjoint",
    "directeur de cabinet",

    "chef de cabinet",

    "secrétaire de",
    "secrétaire d'",
    "secrétaire général",
    "secrétaire général de",
    "secrétaire général de l'"
    "secrétaire exécutif",
    "secrétaire général du",
    "secrétaire général des",
    "coordonnateur",
    "inspecteur",
    "contrôleur",
    "trésorier",

    # Armée
    "général",
    "général de brigade",
    "général de division",
    "général d'armée",
    "maréchal",
    "colonel",
    "lieutenant-colonel",
    "major",
    "capitaine",
    "commandant",
    "commandant de",
    "commandant d'",
    "commandant en chef",
    "chef d'état-major",

    # Justice
    "juge",
    "magistrat",
    "procureur",
    "procureur général",
    "avocat général",
    "avocat",
    "notaire",
    "greffier",
    "juriste",
    "conseiller juridique",
    "Vice-président de l'",
    "Vice-président des l'",
    "Vice-président du l'",
    "Vice-président de ",
    "Vice-président du",
    "Vice-président des'",
    "Vice-présidente de l'",
    "Vice-présidente des l'",
    "Vice-présidente du l'",
    "Vice-présidente de ",
    "Vice-présidente du",
    "Vice-présidente des'",
    "Président général du",
    "Président général des",
    "Président général de",
    "Président général du l'",
    "Président général des l'",
    "Président général de l'",
    "Présidente général du",
    "Présidente général des",
    "Présidente général de",
    "Présidente général du l'",
    "Présidente général des l'",
    "Présidente général de l'",
        
        
    # Université
    "professeur",
    "enseignant",
    "chercheur",
    "recteur",
    "doyen",
    "universitaire",
    "Directeur de l'",
    "Directrice de l'"

    # Économie
    "économiste",
    "entrepreneur",
    "homme d'affaires",
    "banquier",
    "financier",
    "industriel",
    "commerçant",

    # Sport
    "président de la",
    "présidente de la",
        
    "président de la fédération",
    "président de l'association",
    "président de l'",
    "présidente de l",
    "président de club",
    "entraîneur",
    "sélectionneur",
    "arbitre",
    "dirigeant sportif",
    "administrateur de football",

    # Religion
    "évêque",
    "archevêque",
    "cardinal",
    "imam",
    "pasteur",
    "rabbin",
    "moine",

    # Noblesse
    "roi",
    "reine",
    "empereur",
    "impératrice",
    "prince",
    "princesse",
    "sultan",

    # Divers
    "conseiller",
    "conseiller de",
    "conseiller d'",
    "conseiller municipal",
    "conseiller régional",
    "conseiller présidentiel",
    "porte-parole",
    "fonctionnaire",
    "haut fonctionnaire",
    "militant",
    "activiste",
    "syndicaliste",
    "journaliste",
    "écrivain",
    "médecin",
    "ingénieur",
    "chef de guerre",
    "chef rebelle",
    "chef traditionnel",
    "cheffe",
    "chef de l'"
    "cheffe de",
    "cheffe d'",

    "présidente",
    "présidente de",
    "présidente du",
    "présidente des",        
    "présidente d'",
    "vice-présidente",
    "vice-présidente de",
    "vice-présidente d'",

    "première ministre",
    "vice-première ministre",
    "ministre",  # identique au masculin
    "ministre en chef",
    "ministre déléguée",
    "secrétaire d'État",  # identique
    "secrétaire générale",
    "secrétaire générale de",
    "secrétaire exécutive",

    "députée",
    "sénatrice",
    "parlementaire",
    "führer du",
    "gouverneure",
    "vice-gouverneure",
    "gouverneure générale",

    "mairesse",
    "maire",  # certains pays utilisent toujours "maire"
    "adjointe au maire",

    "préfète",
    "sous-préfète",

    "ambassadrice",
    "haute-commissaire",
    "commissaire",  # identique
    "consule",
    "consule générale",
    "représentante permanente",
    "représentante de",
    "représentante d'",
    "envoyée spéciale",

    "administratrice",
    "administratrice générale",

    "directrice",
    "directrice de",
    "directrice d'",
    "directrice générale",
    "directrice générale de",
    "directrice générale du",
    "directrice générale des",
    "directrice générale '",
    "directrice exécutive",
    "directrice adjointe",
    "directrice de cabinet",

    "cheffe de cabinet",

    "coordinatrice",
    "inspectrice",
    "contrôleuse",
    "trésorière",

    "générale",
    "générale de brigade",
    "générale de division",
    "générale d'armée",

    "commandante",
    "commandante de",
    "commandante d'",
    "commandante en chef",

    "juge",  # identique
    "magistrate",
    "procureure",
    "procureure générale",
    "avocate générale",
    "avocate",
    "notaire",  # souvent identique
    "greffière",
    "juriste",  # identique
    "conseillère juridique",

    "professeure",
    "enseignante",
    "chercheuse",
    "rectrice",
    "doyenne",
    "universitaire",

    "économiste",  # identique
    "entrepreneuse",
    "femme d'affaires",
    "banquière",
    "financière",
    "industrielle",
    "commerçante",

    "présidente de la fédération",
    "présidente de l'association",
    "présidente de club",
    "entraîneuse",
    "sélectionneuse",
    "arbitre",  # identique
    "dirigeante sportive",
    "administratrice de football",

    "évêque",  # identique
    "pasteure",
    "rabbin",  # généralement identique
    "religieuse",

    "reine",
    "impératrice",
    "princesse",
    "sultane",

    "conseillère",
    "conseillère de",
    "conseillère d'",
    "conseillère municipale",
    "conseillère régionale",
    "conseillère présidentielle",

    "porte-parole",  # identique
    "fonctionnaire",  # identique
    "haute fonctionnaire",

    "militante",
    "activiste",  # souvent identique
    "syndicaliste",  # identique
    "journaliste",  # identique
    "écrivaine",
    "autrice",
    "auteure",
    "médecin",  # identique
    "ingénieure",

    "cheffe de guerre",
    "cheffe rebelle",
    "cheffe traditionnelle",
    "chercheur en",
    "chercheuse en",  
    "rédactrice à",
    "rédactrice chez",
    "chef d'état major des forces",
    "Président délégué du",
    "Président délégué des",
    "Président délégué de",
    "Président délégué d'",
    "Présidente délégué du",
    "Présidente délégué des",
    "Présidente délégué de",
    "Présidente délégué d'",
        
    
]


LIST_OF_INCOMPLETE_JOB = [
    "Y'en a marre (mouvement)",
    "joueur d'origine",
    "Université Paris-VIII-Vincennes-Saint-Denis",
    "Parti progressiste-conservateur du Canada",
    "Résistance (politique)",
    "Généralité de Catalogne",
    "Prix du Maroc du livre",
    "Liste des présidents du Raja Club Athletic",
    "Préfecture de Casablanca",
    "Union marocaine pour la démocratie",
    "Gouvernement Bouabid II",
    "Technologies de l'information et de la communication pour l'enseignement",
    "Union constitutionnelle",
    "Résistance (politique)",
    "Circonscription de Tozeur",
    "Vienne (Autriche)",
    "Figure"
    "Assemblée nationale constituante",
    "Front de libération nationale (Algérie)",
    "Armée de la république islamique d'Iran",
    "Y'en a marre (mouvement)",
    "West Haven (Connecticut)",
    "Union économique et monétaire ouest-africaine",
    "Parlement de la région de Bruxelles-Capitale",
    "Organisation nationale des Malais unis",
    "Armée de terre bangladaise",
    "Service national de la Sécurité",
    "Coutances et Avranches",
    "Résistance intérieure française",
    "Comptabilité d'entreprise",
    "Ministère (christianisme)",
    "Brigades Izz al-Din al-Qassam",
    "Pâturage (alimentation)",
    "Abu Yusuf Yaqub ben Abd al-Haqq",
    "Commandant (homonymie)",
    "Patinage de vitesse sur piste courte",
    "Assemblée législative du Québec",
    "Congrégation pour les Églises orientales",
    "Centre national de la recherche scientifique",
    "Saint-Méloir-des-Bois",
    "Liste alphabétique des pilotes de rallye",
    "Chambre des représentants",
    "L'Engrenage (film, 1998)",
    "Ordre de Saint-Benoît",
    "Ducs puis princes lombards de Bénévent",
    "Saison 2018-2019 de la LHOu",
    "Position (hockey sur glace)",
    "Assemblée législative de la Colombie-Britannique",
    "1445 en musique classique",
    "Gymnastique rythmique",
    "Parti national fasciste",
    "Brava (municipalité du Cap-Vert)",
    "Parti Communiste de Belgique",
    "Orientalisme (études orientales)",
    "Liste d'as de l'aviation",
    "Chemin de fer de la Jungfrau",
    "Grand Hotel (film, 1932)",
    "Vendredi 13 (film, 1980)",
    "Banshee (série télévisée)",
    "Le Juif Süss (film, 1940)",
    "Faut s'les faire... ces légionnaires !",
    "Hockey sur glace en 1999",
    "ALO docView - Lexikon deutscher Frauen der Feder. Eine Zusammenstellung der seit dem Jahre 1840 erschienenen Werke weiblicher Autoren, nebst",
    "Atlantic City (New Jersey)",
    "Beauvais, Noyon et Senlis",
    "Saint-Jacques-de-Compostelle",
    "Cimetière de l'Est (Boulogne-sur-Mer)",
    "Rodolphe de Rheinfelden",
    "Pierre Legardeur de Repentigny",
    "Guillaume de Nassau-Dillenbourg",
    "Emmanuel Richard Priso Ngom Priso",
    "De Nouvelle-Aquitaine",
    "Conseil constitutionnel",
    "D'agglomération Amiens Métropole",
    "de la Jeunesse d'Allemagne",
    "La Danseuse nue (film, 1952)",
    "Illusions (film, 1930)",
    "Le Portrait de Dorian Grey (film, 1915)",
    "Mare Nostrum (film, 1926)",
    "Viktor und Viktoria (film, 1933)",
    "L'amour ne meurt jamais",
    "2023 en hockey sur glace",
    "1998 en hockey sur glace",
    "Hockey sur glace en 2006",
    "Hockey sur glace en 1999",
    "Hockey sur glace en 1987",
    "Hockey sur glace en 1977",
    "Hockey sur glace en 1971",
    "Première guerre intercoloniale",
    "Siège de Lilybée (250 av. J.-C.-241 av. J.-C.)",
    "Www.pietro-lombardi.com",
    "Www.pieroesteriore.com",
    "For the majority of the congress members, the only essential difference between a republic and the",
    "Activités principales exercées",
    "Arrière-arrière-petit-fils",
    "Jacqueline Scott-Lemoine",
    "Marcus Fulvius Curvus Paetinus",
    "Jean Doukas Kamatéros",
    "Cosmo Edmund Duff Gordon",
    "Joseph (Nouveau Testament)",
    "Joseph Jacques Marest",
    "William Cubitt (1785-1861)",
    "Pierre-Antoine Demachy",
    "Philippe Lacoue-Labarthe",
    "Louis-Gabriel Michaud",
    "François Gracchus Cabrol",
    "Amédée Renault-Morlière",
    "Nelly Marandon de Montyel",
    "Giovanni Francesco Cassana",
    "Karl Friedrich Schinkel",
    "Heinrich Dietrich von Grolman",
    "David Thompson (homme politique canadien)",
    "Henry Oakes (général)",
    "Lucien Boyer (chansonnier)",
    "Susan Thornton Glassell",
    "Liste d'écrivains de langue française par ordre alphabétique",
    "Les Bas-fonds (Gorki)",
    "Gironde (département)",
    "Liste de militants écologistes",
    "Dynastie hachémite",
    "Lucius",
    "Syrie",
    "Poésie",
    "dés",
    "Descendant",
    "Théâtre",
    "Galilée",
    "des",
    " Vienne (Autriche)",
    "Vienne (Autriche)",
    "as",
    "As",
    "Assemblée nationale"

]


HTML_ELEMENT_LIST = [
    "<a href=",
    "</a>",
    "d:q",
    "</div>",
    "<div class=",
    "</td>",
    "<td>",
    "</th>",
    "[",
    "]",
    "{",
    "}",
    ",",
    "<th>",
    "<tr>",
    "</tr>",
    "<tbody>",
    "</tbody>",
    "<table>",
    "</table>",
    "<caption>",
    "</caption>",
    "<span class=",
    "</span>",
    "<sup>",
    "</sup>",
    "<small>",
    "</small>",
    "<p>",
    "</p>",
    "<ul>",
    "</ul>",
    "<li>",
    "</li>",
    "<i>",
    "</i>",
    "<b>",
    "</b>",
    "<br>",
    "<br/>",
    "<time class=",
    "<time datetime=",
    "<abbr class=",
    "<meta name=",
    "<title>",

    # Attributs HTML
    "class=",
    "id=",
    "scope=",
    "colspan=",
    "rowspan=",
    "style=",
    "href=",
    "src=",
    "datetime=",
    "data-sort-value=",
    "data-sort-type=",
    "rel=",

    # Classes / fragments CSS
    "mw-redirect",
    "mw-disambig",
    "cite-bracket",
    "reference",
    # "nowrap",
    # "external",
    # "extiw",
    "skin-theme-clientpref-day",
    "vector-feature-main-menu-pinned-disabled",
    "vector-feature-limited-width-clientpref-1",
    "vector-feature-limited-width-content-enabled",
    "vector-feature-custom-font-size-clientpref-1",
    "vector-feature-appearance-pinned-clientpref-0",
    "vector-sticky-header-enabled",

    # Références Wikipédia
    "#cite note-",
    "#cite ref-",
    "cite note-",
    "cite ref-",
    "Styles:r",
    "BNF",
    "International Standard Book Number",
    "https://www.wikidata.org/",
    "https://en.wikipedia.org/",

    # Morceaux de code HTML
    "</th><td",
    "<td colspan=",
    "<th scope=",
    "<tr class=",
    "<tbody><tr",
    "<span data-sort-value=",
    "<abbr class=",
    "<time class=",
    # Non html elem
    " Décès ",
    "Décès ",
    "Liste des",
    "années 1",
    "années 2",
    "années 3",
    "années 4",
    "années 5",
    "années 6",
    "années 7",
    "années 8",
    "années 9",
]
NON_TOWN_ELEMENT_LIST = [
    # Balises HTML
    # Valeurs parasites
    ",",
    "(",
    ")",
    "?",
    "-",
    "–",
    "...",
    "p.",
    "en:Late Roman Republic",
    "pp.",
    "College d'Eton",
    "des",
    "10ᵉ",
    "antoine",
    "saint-domingue (colonie française)",
    "paul",
    "manoir",
    "neufchâteau",
    "20e",
    "Paris",
    "Position (hockey sur glace)",
    "joseph",
    "jules",
    "philippe",
    "andré",
    "jean-baptiste",
    "claude",
    "michel",
    "département de constantine",
    "georges",
    "beylicat de tunis",
    "hameau",
    "sens",
    "comté du maine"
    "du",
    "à",
    "ou",
    "et",
    "ordination",
    "poids de forme",
    "surrey (comté)",
    "el",
    "!irlande",
    "irlande",
    "professeur",
    "consul",
    "royaume d'italie",
    "trinity college",
    "animateur",
    "chevalier",
    "attaquant",
    "performance",
    "hussein",
    "anglais britannique",
    "prise",
    "virginie (états-unis)",
    "camerounaise",
    "profession",
    "edo",
    "derby",
    "cheshire (comté)",
    "raj britannique",
    "gloucestershire",
    "windsor",
    "couronne de castille",
    "marie",
    "ordre cistercien",
    "persan",
    "science-fiction",
    "région de bruxelles-capitale",
    "musicologie",
    "sankt",
    "northamptonshire",
    "état",
    "colombie-britannique",
    "sur",
    "royaume de portugal",
    "pour",
    "hanyu pinyin",
    "zhejiang",
    "henri",
    "hôtel",
    "fribourg",
    "îles cook",
    "academie americaine des arts et des sciences",
    "monarchie constitutionnelle francaise (1791-1792)",
    "ordre national du quebec",
    "guerre d'independance des etats-unis",
    "premiere guerre mondiale",
    "ordre de saint-michel et saint-georges",
    "baronnet",
    "dernière",
    "victoria (état)",
    "écrivain",
    "noblesse",
    "berkshire",
    "long",
    "mythologie grecque",
    "hawaï"
    "empire byzantin",
    "kent",
    "nouveau-brunswick",
    "pennsylvanie",
    "bristol",
    "essai",
    "état de new york",
    "jean",
    "palais",
    "lewisham",
    "raïon",
    "irlande",
    "west",
    "données",
    "fort",
    "afrique du sud",
    "essex",
    "south",
    "bad",
    "latin",
    "hull (québec)",
    "mais",
    "contre",
    "près",
    "au",
    "dans",
    "[",
    "langue : anglais",
    "langue : allemand",
    "langue : français",
    "langue : espagnol",
    "langue : italien",
    "langue : portugais",
    "langue : néerlandais",
    "langue : russe",
    "langue : chinois",
    "langue : japonais",
    "langue : coréen",
    "langue : arabe",
    "]",
    "surrey (comté)",
    "irlande",
    "afrique du sud",
    "empire russe",
    "hull (québec)",
    "québec",
    "lancashire",
    "charles",
    "press",
    "prédécesseur",
    "professeur",
    "côte d'ivoire",
    "↑",
    "ouïezd",
    "comte",
    "île",
    "sépulture",
    "consul",
    "royaume d'italie",
    "st.",
    "conservatoire royal de La haye",
    "(a)",
    "(à)",
    "à",
    "Alpinisme",
    "Roman (litterature)",
    "Royaume-Uni",
    "Japon",
    "Roman (litterature)",
    "Avocat (metier)",
    "Composition d'une equipe de rugby a XV",
    "Metre",
    "Monaco",
    "Metre",
    "Russie",
    "Cameroun",
    "Etats pontificaux",
    "Autorite (sciences de l'information)",
    "Union des republiques socialistes sovietiques",
    "Irlande (pays)",
    "Singapour",
    "College d'Eton",
    "Samourai",
    "Grande-Bretagne (royaume)",
    "Allemagne",
    "Egypte",
    "Periode professionnelle",
    "Defenseur (football)",
    "Marchand (commerce)",
    "premier",
    "Canadiens de Montreal",
    "Israel",
    "Composition d'une equipe de rugby a XIII",
    "Ordination episcopale de rite romain",
    "Milieu de terrain",
    "Kenya",
    "Attaquant (football)",
    "Ordre national de la Legion d'honneur",
    "Chroniqueur (litteraire)",
    "Algerie",
    "d\\:Q2839628",
    "Medaille d'or (sport)",
    "Pied (unite)",
    "Scenariste",
    "Ethiopie",
    "Organ (music)",
    "Senegal",
    "Nouvelle-Zelande",
    "Jamaique",
    "Bresil",
    "Red Wings de Detroit",
    "Ministere (christianisme)",
    "page(s)",
    "Universite Paris-I-Pantheon-Sorbonne",
    "Theologie",
    "Chevalier (chevalerie)",
    "Pasteur (christianisme)",
    "Universite Harvard",
    "Resistance (politique)",
    "Universite de Cambridge",
    "Royaume de Prusse",
    "Professeur (titre)",
    "Ecole normale superieure (Paris)",
    "Universite de Californie a Berkeley",
    "Universite d'Oxford",
    "Histoire de la photographie au Japon",
    "Haiti",
    "Chanoine",
    "Sharks de San Jose",
    "Universite Columbia",
    "0",
    "Georgie (pays)",
    "Nordiques de Quebec",
    "Universite de Chicago",
    "Trinity College (Dublin)",
    "Venerable (orthodoxie)",
    "Thailande",
    "Hawai",
    "Universite de Louvain (1425-1797)",
    "Alpinisme",
    "Benin",
    "Universite de Leyde",
    "Ordre de Saint-Benoit",
    "Palestine (region)",
    "Italien",
    "Christ Church",
    "Universite de Londres",
    "Organiste",
    "Grece",
    "Universite d'Edimbourg",
    "Universite de Princeton",
    "Gardien de but",
    "Universite Yale",
    "University College de Londres",
    "Ligue americaine de hockey",
    "Matchs",
    "Ordre national du Merite (France)",
    "Gains",
    "Yougoslavie",
    "Nationalite francaise",
    "Orientalisme (etudes orientales)",
    "Equateur (pays)",
    "Daimyo",
    "Royaume de Hongrie",
    "Francais",
    "Ecole des hautes etudes en sciences sociales",
    "Navigateur (marine)",
    "Gardien de but (football)",
    "Cardinal (religion)",
    "SKA Saint-Petersbourg",
    "Protectorat francais de Tunisie",
    "Esclavage",
    "Entraineur (handball)",
    "Allemagne de l'Ouest",
    "Arbitre (football)",
    "Late Roman Republic",
    "Universite Paris-Nanterre",
    "Universite de Montreal",
    "Royaume du Bosphore",
    "Editeur (metier)",
    "Academie des sciences (France)",
    "Universite Stanford",
    "19e siecle",
    "avant Jesus-Christ",
    "Hedvig Eleonora Parish",
    "Gouverneur",
    "Vatican",
    "Grand Chelem",
    "Empire allemand",
    "Perou",
    "Musique baroque",
    "Renaissance",
    "Ordre des Precheurs",
    "King's College de Londres",
    "Anglo-Saxons",
    "Robert",
    "Arrondissement",
    "Tchequie",
    "XVIIe siecle",
    "Duche de Milan",
    "Guinee",
    "Universite du Michigan",
    "New College (Oxford)",
    "numero",
    "18e siecle",
    "Brynas IF",
    "Bourse Guggenheim",
    "Republique du Congo",
    "Peine de mort",
    "Mississippi (Etat)",
    "Hockey Club Fribourg-Gotteron",
    "Premier",
    "Animateur (artiste)",
    "Sorcellerie",
    "Frolunda HC",
    "Allemand",
    "Universite de Pennsylvanie",
    "Batavia (Indes neerlandaises)",
    "metre",
    "Ordre des Palmes academiques",
    "Nouvelle-Ecosse",
    "Koweit",
    "Universite de Tokyo",
    "Ile de Wight",
    "Imperial College London",
    "Universite de New York",
    "Universite de Glasgow",
    "Universite Cornell",
    "Patinage artistique",
    "Producteur de cinema",
    "Gaule",
    "Royal Navy",
    "Ligue nationale de hockey",
    "Centre national de la recherche scientifique",
    "Enluminure",
    "Francais (peuple)",
    "Arizona",
    "Engelbrekt Parish",
    "Kentucky",
    "Tibetain",
    "Portrait",
    "Burin (gravure)",
    "Condottiere",
    "Rouen hockey elite 76",
    "Troisieme Reich",
    "XIVe siecle",
    "Martyr",
    "Baryton (voix)",
    "Antiquite classique",
    "Ordre national du Quebec",
    "Universite Johns-Hopkins",
    "China (region)",
    "Magdalen College (Oxford)",
    "Sinogramme traditionnel",
    "Palestine (Etat)",
    "Maine (Etats-Unis)",
    "London School of Economics",
    "Union sovietique",
    "Republique democratique allemande",
    "Botanique",
    "2007",
    "Chretien",
    "Seconde Republique (Espagne)",
    "Ain",
    "Paroisse de Saint Andrew",
    "Collection (activite)",
    "Ecole pratique des hautes etudes",
    "Oregon",
    "Universite d'Alcala de Henares (1499-1836)",
    "2014",
    "Freguesia",
    "Schlager",
    "Nouvelle-France",
    "Djurgarden Hockey",
    "Sidi",
    "Basse (voix)",
    "Panama",
    "Producteur de musique",
    "Danse",
    "Vermont",
    "2006",
    "Tanka (poesie)",
    "Amiral",
    "URSS",
    "Universite Paris-VIII-Vincennes-Saint-Denis",
    "Dynastie Qing",
    "Alberta",
    "Sichuan",
    "Malaisie",
    "Knight Bachelor",
    "Universite de Californie a Los Angeles",
    "Hedvig Eleonora and Oscar Parish",
    "Compagnie de Jesus",
    "Skelleftea AIK",
    "Republique romaine",
    "Banque",
    "Plon",
    "Mezzo-soprano",
    "16e siecle",
    "Marine royale",
    "Hebreu",
    "Saison 2003 de la NFL",
    "TPS Turku (hockey sur glace)",
    "Puerto",
    "Tanzanie",
    "Benezit",
    "fois",
    "Sussex de l'Est",
    "Marguerite",
    "Parti liberal (Royaume-Uni)",
    "Archeveche d'Arles",
    "Premiere Guerre mondiale",
    "Indonesie",
    "Chris",
    "Gonville and Caius College",
    "College royal militaire de Sandhurst",
    "Royal College of Art",
    "Christianisme",
    "Trinite-et-Tobago",
    "Periode Joseon",
    "Rampage de San Antonio",
    "Salavat Ioulaiev Oufa",
    "Emirats arabes unis",
    "Chantre (christianisme)",
    "Pretre catholique",
    "Ak Bars Kazan",
    "Saison 2004 de la NFL",
    "Pays-Bas espagnols",
    "Troisieme",
    "Serbe",
    "Baviere",
    "Pop",
    "15e siecle",
    "Croix de guerre 1939-1945 (France)",
    "Sculpture",
    "Biographe",
    "Hockey Club de Reims",
    "Angleterre",
    "The Queen's College",
    "Anhui",
    "Mike",
    "Prevot (religion)",
    "Document utilise pour la redaction de l'article",
    "Lexicographie",
    "Geneve-Servette Hockey Club",
    "HK Spartak Moscou",
    "2012",
    "Eissportverein Zoug",
    "Poesie",
    "Bahia",
    "New Hampshire",
    "Sussex de l'Ouest",
    "IceHogs de Rockford",
    "Institut national des langues et civilisations orientales",
    "Maison imperiale du Japon",
    "Rivermen de Peoria",
    "Ayrshire (comte)",
    "Patriarche",
    "Universite Paris-Diderot",
    "m",
    "Grec (langue)",
    "of",
    "Violon",
    "Schloss",
    "Universite McGill",
    "Ville",
    "Tibet (1912-1951)",
    "Dakota du Sud",
    "Ordination episcopale",
    "Piraterie",
    "Section paloise (rugby a XV)",
    "Coyotes de l'Arizona",
    "Femme de lettres",
    "Ordre de Saint-Stanislas (Russie imperiale)",
    "Medaille d'or",
    "Philosophie",
    "Prete a",
    "Marine (peinture)",
    "RSFS de Russie",
    "Metallourg Magnitogorsk",
    "Ordre du Merite de la Republique federale d'Allemagne",
    "Tenor",
    "Augustins",
    "Renaissance (periode historique)",
    "Spectacle vivant",
    "Alexandre III (pape)",
    "Ait",
    "Henri Ier (roi d'Angleterre)",
    "Palestine mandataire",
    "Saison 2007 de la NFL",
    "Domicile",
    "Suffragette",
    "Universite du Quebec a Montreal",
    "Nouvelle-Espagne",
    "Royaume de Sardaigne (1720-1861)",
    "italienne",
    "Durham (comte)",
    "Little",
    "Utah",
    "General",
    "Zaire",
    "Lombardie",
    "Borough",
    "Alexandre le Grand",
    "Grammaire",
    "Bhikshu",
    "Capitaine (grade militaire)",
    "2013",
    "Ecosse",
    "Magdalen College",
    "Catholicisme",
    "Ambassadeur",
    "Institut universitaire de France",
    "Ebeniste",
    "Identifiant",
    "Parlement grec",
    "Anjou",
    "Metteur en scene",
    "Dynastie Tang",
    "Hampshire",
    "Tamil Nadu",
    "Punk rock",
    "Grands carmes",
    "Clement VII (antipape)",
    "Burundi",
    "Musique folk",
    "Opera (musique)",
    ">>",
    "Republique populaire de Chine",
    "Free University of Brussels (1834-1969)",
    "Espagne franquiste",
    "Ordination episcopale de rite romain",
    "Renaissance (periode historique)",
    "Ecole normale superieure (Paris)",
    "Universite de Louvain (1425-1797)",
    "Lieutenant (grade militaire)",
    "Partisan (guerilla)",
    "Composition d'une equipe de rugby a XV",
    "Defenseur (football)",
    "Marie de Bourbon (1428-1448)",
    "Claude de Lorraine (1578-1657)",
    "Thomas Holland (2e comte de Kent)",
    "Jean II de Brienne (mort vers 1296)",
    "Deutsche",
    "Academie des beaux-arts de Dusseldorf",
    "Israel",
    "Palestine (Etat)",
    "Patriarche (christianisme)",
    "Ministere (christianisme)",
    "Collectionneur d'oeuvres d'art",
    "Cardinal (religion)",
    "Maurice de Saxe (1696-1750)",
    "Potier (metier)",
    "Honduras",
    "Costumier",
    "20e siecle",
    "Francesco",
    "Ordre du Carmel",
    "Guillaume",
    "Champagne",
    "The",
    "Couronne d'Aragon",
    "Nepal",
    "Catalan",
    "Rock progressif",
    "Lake",
    "Diacre",
    "Humanisme",
    "Allemands",
    "Khan",
    "Couronne du royaume de Pologne",
    "Batteur",
    "Aviron bayonnais rugby pro",
    "Dumfries and Galloway",
    "Maison de Hohenzollern",
    "Phantoms de Philadelphie",
    "Syriaque",
    "(en)",
    "Moyen Age",
    "British Academy",
    "Premier Empire",
    "Union d'Afrique du Sud",
    "Grand Khorassan",
    "Capitaine (France)",
    "HK Dinamo Minsk",
    "lors",
    "University of Paris",
    "Ile-du-Prince-Edouard",
    "Gouvernement de Moscou (1708-1929)",
    "Universite de Melbourne",
    "Universite Brandeis",
    "Vastra",
    "Rugby club toulonnais",
    "Flames de Saint-Jean",
    "University College (Oxford)",
    "Blazers d'Oklahoma City",
    "XVe siecle",
    "Politologue",
    "Deuxieme",
    "indienne",
    "Vallee d'Aoste",
    "Parlement de Paris",
    "Khimik Voskressensk",
    "Kfar",
    "Queens' College",
    "American Mathematical Society",
    "Black Hawks de Chicago",
    "Musique de la Renaissance",
    "HC Zlin",
    "Hockey sur glace",
    "Reign d'Ontario",
    "Djurgardens IF (hockey sur glace)",
    "Livonie",
    "Lausanne Hockey Club",
    "Union sportive dacquoise",
    "Kolner Haie",
    "TPS (hockey sur glace)",
    "Etat de Sao Paulo",
    "Saison 2000 de la NFL",
    "Hongrois",
    "Parti conservateur du Canada (ancien)",
    "Ailier (rugby a XV)",
    "Goryeo",
    "Hockey Club Amiens Somme",
    "Batteur (cricket)",
    "Guizhou",
    "Hockey Club La Chaux-de-Fonds",
    "Hockey Club Ajoie",
    "Mozambique",
    "Gymnastique artistique aux Jeux olympiques",
    "Devils d'Albany",
    "Shaanxi",
    "9e siecle",
    "Royaume de Saxe",
    "Epistolier (litterature)",
    "Compositeur",
    "d\\:Q10659387",
    "Maison de Savoie",
    "Leopold",
    "Graffiti",
    "Frederic",
    "Collectionneur d'oeuvres d'art",
    "Republique socialiste federative sovietique de Russie",
    "Universite de Strasbourg",
    "Hopital",
    "Sultanat de Roum",
    "Saison 2024 de la NFL",
    "espagnole",
    "Marechal de France",
    "Royaume d'Ecosse",
    "Royaume d'Afghanistan",
    "Glen",
    "Rue du Bac",
    "Censeur",
    "Erythree",
    "Limousin (ancienne region administrative)",
    "Livret (musique)",
    "Protestantisme",
    "Region",
    "Academia Europaea",
    "Islam",
    "australienne",
    "Soufisme",
    "Universite Pierre-et-Marie-Curie",
    "Torpedo Nijni Novgorod",
    "Rogle BK",
    "Paroisse de Saint Mary",
    "Position",
    "Partisan (guerilla)",
    "Monsters du lac Erie",
    "Pelicans Lahti",
    "Chamonix Hockey Club",
    "Diacre (christianisme)",
    "Sodertalje SK",
    "Heilongjiang",
    "HC Sparta Prague",
    "Champion",
    "Prix Edgar-Allan-Poe",
    "Sant",
    "Acre (Israel)",
    "Paroisse de Saint Ann",
    "Jeanne",
    "Hong Kong",
    "2",
    "--",
    "Dramaturge de production",
    "Ordre du Temple",
    "Worcestershire",
    "Maison de Mecklembourg",
    "Astrologie",
    "Bagratides",
    "Universite de Kyoto",
    "Republique des Deux Nations",
    "Poitou",
    "Polonais",
    "Cambodge",
    "Universite de Geneve",
    "d\\:Q821117",
    "d\\:Q10466522",
    "Christ's College",
    "UCLouvain",
    "Le Monde",
    "Gabon",
    "Peinture de paysage",
    "Ecole nationale d'administration (France)",
    "Clavecin",
    "XIIIe siecle",
    "Musique de film",
    "Bahrein",
    "Blog",
    "Royaume de Baviere",
    "Programmation informatique",
    "Arsacides",
    "ivoirienne",
    "Luth",
    "Birman (langue)",
    "12e siecle",
    "EC Klagenfurt AC",
    "Sharks de Worcester",
    "Mouvement LGBT",
    "HC Bienne",
    "AIK IF",
    "Hockey Club Ambri-Piotta",
    "2008",
    "Kraken de Seattle",
    "Rhode Island",
    "Tasmanie",
    "HK Jesenice",
    "Karpat Oulu",
    "Poids",
    "HPK Hameenlinna",
    "Everblades de la Floride",
    "volume",
    "Tennis de table",
    "Eisbaren Berlin",
    "Saison 2002 de la NFL",
    "HC Spartak Moscou",
    "Royaume de Ryukyu",
    "Kiekko-Vantaa",
    "SC Riessersee",
    "Patriarche de Constantinople",
    "Tintin (periodique)",
    "HEC Paris",
    "Beni",
    "Universite de Leipzig",
    "Allegeance",
    "Professeur (enseignant)",
    "Henry",
    "Conservatoire national superieur de musique et de danse de Paris",
    "Consort (monarchie)",
    "(Leveland)",
    "Giovanni",
    "Gross",
    "Fujian",
    "David",
    "11e siecle",
    "Jurisconsulte",
    "Sierra Leone",
    "Benedictin",
    "Royaume de Gwynedd",
    "Centre de formation des journalistes",
    "Yemen",
    "Saison 1994 de la NFL",
    "Harvard College",
    "Ordre du Bain",
    "Aberdeenshire (historique)",
    "St John's College",
    "Syndicalisme",
    "Al",
    "Liberia",
    "Universite Brown",
    "Jets de Winnipeg",
    "Universite de Washington",
    "Niger",
    "Vicomte de Lautrec",
    "Domaine de Satsuma",
    "son",
    "Jiangxi",
    "Saison 1995 de la NFL",
    "Republique socialiste sovietique d'Ukraine",
    "CSKA Moscou (hockey sur glace)",
    "HC Kosice",
    "Athletisme",
    "chinoise",
    "Espoo Blues",
    "Jose",
    "Golden Knights de Vegas",
    "Saison 2001 de la NFL",
    "coll.",
    "Hampshire (comte)",
    "Pseudonymes",
    "Abbaye",
    "Essex (comte)",
    "Merton College (Oxford)",
    "Consort",
    "Indes orientales neerlandaises",
    "Republique de Geneve",
    "Universite Humboldt de Berlin",
    "Lettonie",
    "Achrafieh",
    "Louis XIV",
    "Badgers du Wisconsin",
    "Old",
    "Belges (nationalite)",
    "Peinture",
    "Gap Hockey Club",
    "Royaume d'Irlande",
    "Deuxieme Republique (Pologne)",
    "Colon (personne)",
    "Republique dominicaine",
    "Catholicos d'Armenie",
    "Parti travailliste (Royaume-Uni)",
    "James",
    "Grand Chelem (tennis)",
    "Corpus Christi College",
    "Ordrup",
    "Domaine",
    "Ethnologie",
    "Receptionneuse-attaquante",
    "Costa Rica",
    "Ordre royal de Victoria",
    "Nouvelliste",
    "circa (environ / aux environs de)",
    "Ukrainien",
    "Universite Paris-Sud",
    "Afrique",
    "Lama (bouddhisme)",
    "Christiania",
    "Malmo Redhawks",
    "Stade toulousain",
    "d\\:Q10512441",
    "IceCats de Worcester",
    "Henan",
    "Amherst College",
    "Pontons de Rochefort",
    "Guangxi",
    "Trampoline",
    "Stade francais Paris rugby",
    "Lukko Rauma",
    "EV Landshut",
    "Paroisse de Trelawny",
    "Benoit XIII (antipape)",
    "Modele (art)",
    "Cambridgeshire",
    "Mystique",
    "Universite de Padoue",
    "Clerge",
    "Science du hadith",
    "Ordre du Soleil levant",
    "Inde britannique",
    "Armenien",
    "Clerkenwell",
    "Katanga",
    "Commune",
    "14e siecle",
    "Ordre",
    "Universite Waseda",
    "Somalie",
    "Cumberland (comte)",
    "Universite de Copenhague",
    "Eswatini",
    "Bielorussie",
    "Rugby",
    "Irlandais",
    "Justice (droit)",
    "Installation",
    "Trinity College (Oxford)",
    "algerienne",
    "Xinjiang",
    "L'",
    "Consul (Rome antique)",
    "College Bryn Mawr",
    "Imprimerie",
    "Harvard Business School",
    "Cimetiere de Kensal Green",
    "Ordre royal et militaire de Saint-Louis",
    "13e siecle",
    "Liste de compositeurs italiens de musique classique",
    "Japonais",
    "Chevalier romain",
    "Republique de Chine",
    "Front de l'Est (Seconde Guerre mondiale)",
    "Republique de Venise",
    "Malawi",
    "Timra IK",
    "Odisha",
    "Ecole nationale superieure des mines de Paris",
    "Saison 1997 de la NFL",
    "Indians de Springfield",
    "Qatar",
    "Philanthropie",
    "Farjestads BK",
    "Kikongo",
    "Kungsholm",
    "Sao Tome-et-Principe",
    "Royaume de Sardaigne",
    "EV Fussen",
    "Facteur d'orgue",
    "Yunnan",
    "VIK Vasteras HK",
    "Reds de Providence",
    "Maple Leafs de Saint-Jean",
    "Jackals d'Elmira",
    "Severstal Tcherepovets",
    "Aeros de Houston (LAH)",
    "Hanja",
    "Ilves Tampere",
    "Grasshopper Club Kusnacht Lions",
    "Tappara",
    "1,78 m",
    "Saison 1993 de la NFL",
    "Iulii",
    "Atlant Mytichtchi",
    "Critique (philosophie)",
    "Nicolas",
    "Fidji",
    "Acteur",
    "Trebizonde",
    "Beatification",
    "Imam",
    "Babylone (civilisation)",
    "Dynastie Ming",
    "Chelsea (Londres)",
    "Siegen",
    "Shanxi",
    "Huitieme",
    "Martha's Vineyard",
    "Republique federative socialiste de Yougoslavie",
    "Legat (Rome antique)",
    "Ermite",
    "Britanniques",
    "Universite catholique de Louvain (1835-1968)",
    "Cote",
    "d\\:Q11057477",
    "Alabama",
    "Guerrier",
    "Winchester College",
    "Royal",
    "Buda",
    "Bengale",
    "Choa",
    "Arkansas",
    "Histoire des ordres franciscains",
    "Newham",
    "Universite du Wisconsin a Madison",
    "Djibouti",
    "Khanat de Crimee",
    "Union Bordeaux Begles",
    "d",
    "Australie-Occidentale",
    "Municipalite",
    "Fantasy",
    "Universite d'Aberdeen",
    "Manitoba",
    "Universite Northwestern",
    "Empire espagnol",
    "Voix (instrument)",
    "Empire moghol",
    "Oilers de Tulsa",
    "en\\:Chevy Chase, Maryland",
    "HC Slovan Bratislava",
    "Cornelii Lentuli",
    "Phantoms de l'Adirondack",
    "Italiens",
    "Cyclones de Cincinnati",
    "centimetre",
    "John F. Kennedy School of Government",
    "Personne de merite culturel",
    "Facture instrumentale",
    "en\\:Katarina Parish",
    "Irlande (ile)",
    "Ukiyo-e",
    "Premier cycle universitaire",
    "Neurosciences",
    "Universite de l'Illinois a Urbana-Champaign",
    "Rapperswil-Jona Lakers",
    "Namibie",
    "Stade aurillacois Cantal Auvergne",
    "Nailers de Wheeling",
    "Rallye-raid",
    "Jokerit Helsinki",
    "Hameenlinnan Pallokerho",
    "Ilves (hockey sur glace)",
    "Stars du Texas",
    "Ornithologie",
    "Lower",
    "Camp de Souge",
    "Grece antique",
    "Messe (musique)",
    "2005",
    "Dixieme",
    "Cimetiere du Montparnasse",
    "HC Kladno",
    "Santo",
    "Novo",
    "Prelature",
    "Taiwan",
    "Pilote (aviation)",
    "Republique de Chine (1912-1949)",
    "Service (eglise)",
    "Miniature (portrait)",
    "1",
    "Senateurs d'Ottawa",
    "Regie (spectacle)",
    "Patriarche (christianisme)",
    "Marin (profession)",
    "Sport professionnel",
    "Universite Laval",
    "Universite Paris-Sorbonne",
    "Espagnol",
    "Ecole polytechnique (France)",
    "17e siecle",
    "Realisateur",
    "paris-soir",
    "(consulté)",
    "elledby=",
    "irlande",
    "(à)",
    "professeur",
    "consul",
    "royaume d'italie",
    "animateur",
    "trinity college",
    "corée du nord",
    "chevalier",
    "pape",
    "documentaire",
    "attaquant",
    "philologie",
    "enfield",
    "reading",
    "caroline du nord",
    "saint catholique",
    "wiltshire",
    "cardinal",
    "canton",
    "california institute of technology",
    "cartographie",
    "hebei",
    "autriche-hongrie",
    "hip-hop",
    "performance",
    "rss d'ukraine",
    "abbé",
    "jacques",
    "maryland",
    "grand",
    "rock",
    "romanisation",
    "soprano",
    "hackney",
    "somerset",
    "vila",
    "danse contemporaine",
    "dorset",
    "hangeul",
    "devon (comté)",
    "trinity college",
    "animateur",
    "warwickshire",
    "saint-empire romain germanique",
    "norfolk (comté)",
    "zoologie",
    "dessin humoristique",
    "guangdong",
    "colorado",
    "vietnam",
    "chevalier",
    "lachine",
    "shandong",
    "derbyshire",
    "bas-empire romain",
    "cornouailles",
    "congolaise",
    "fonction publique",
    "saint-louis",
    "avec",
    "missouri (état)",
    "oklahoma",
    "surakarta",
    "joueur",
    "floruit",
    "kansas",
    "ordre des arts et des lettres",
    "pays",
    "tennessee",
    "?",
    "Données",
    # Catégories / métadonnées Wikipédia
    "Biographie",
    "Décès",
    "Naissance",
    "naissance",
    "↑"
    "Nationalité",
    "Religion",
    "Genre",
    "Voix",
    "Labels",
    "Activité",
    "Activités",
    "Fonction",
    "Fonctions",
    "Titre",
    "Lieu",
    "Poste",
    "Prédécesseur",
    "Successeur",
    "Famille",
    "Dynastie",
    "Époque",
    "Ordination",
    "Sépulture",
    "Autre titre",
    "Autres titres",
    "Symphonie",
    "Ville libre d'Empire",
    "Vindex",
    "Lichtental,",
    "par",
    "Gia",
    "Rue Saint-Denis",
    "Hôtel de Condé",
    "mars",
    "France",
    "Inde",
    "Touraine",
    "Antonin le Pieux",
    "Enseignement",
    "Rue de Clichy",
    "Pays-Bas",
    ")",
    "(7",
    "Période Comnène Précédé par Nicéphore III Botaniatès Co-empereur Constantin Doukas (1074-1078 / 1081-1087",
    "Dictionnaire biographique",
    "(à",
    "6e",
    "septembre",
    "New",
    "Plutarque",
    "Nationalité",
    "(~72",
    "George Packer",
    "Bataille d'Asculum",
    "Hypace",
    "4e",
    "Antonins",
    "Égypte antique",
    "Ashfield",
    "et",
    "Rue Saint-Honoré",
    "Château",
    "Monts Khentii",
    "Paroisse",
    "Hôtel Saint-Pol",
    "août",
    "Consul",
    "Cappadoce",
    "Hürth-Hermülheim",
    "[",
    "9e",
    "13e",
    "mai",
    "alive",
    "autre",
    "Rue Saint-Denis (Paris)",
    "Ivoire",
    "15e",
    "Flavius",
    "Royaume de France",
    "condita",
    "Julio-Claudiens",
    "Dauphin",
    "Rue de la Charbonnière",
    "à",
    "Macrin",
    "Calendrier julien",
    "West",
    "Lorette",
    "Mon",
    "El",
    "Riese",
    "Yahdun-Lim",
    "17e",
    "Chase",
    "c.",
    "Comté",
    "Décès",
    "Palais",
    "Constantiniens",
    "Rue du Faubourg-Poissonnière",
    "danubiennes",
    "avril",
    "Bataille de Pavie",
    "À",
    "Lucius Antonius Saturninus",
    "Asie",
    "Jean",
    "décembre",
    "Château du Stuyvenberg",
    "Dictateur",
    "Nationalité Américaine Décès 27 avril 1961 (à 67 ans",
    "Grabtown (Caroline du Nord)",
    "Nine",
    "Atar",
    "Horfield",
    "nouvelle",
    "Obergossen,",
    "Suède",
    "Liste des empereurs byzantins",
    "Dynastie thrace",
    "-450",
    "South Side (Chicago)",
    "Territoire",
    "Nom dans la langue maternelle Marcus Porcius Cato",
    "Ancien",
    "octobre",
    "Liste des rois du Wessex",
    "Italie",
    "Olympios",
    "Constantin V",
    "L'Ermitage",
    "3e",
    "Île",
    "Klein Flottbek",
    "ou",
    "Artabasde",
    "Isaurie",
    "Période Macédonienne Précédé par Zoé Porphyrogénète Michel V Co-empereur Zoé Porphyrogénète (1028-1050",
    "novembre",
    "La",
    "Liste des comtesses de Champagne",
    "Paphlagonie",
    "Australie",
    "Austrasie",
    "Fife (Écosse)",
    "Castello",
    "San",
    "un",
    "Isaac II Ange",
    "Trajan",
    "Store",
    "Barcola",
    "Château de Copenhague",
    "Liste des comtes et ducs de Savoie",
    "Jean IV Lascaris",
    "juillet",
    ",",
    "Ramaputta",
    "Romain II",
    "George",
    "Nijni",
    "Raïon",
    "Sin-muballit",
    "Basile II",
    ", initial-scale=1.0",
    "Royaume de Sicile",
    "Élimée",
    "[ 1 ]",
    "Justinien II",
    "Selichtchi",
    "Anne Ange",
    "Guerre des Deux-Roses",
    "Période Lascaris Précédé par Jean III Doukas Vatatzès Suivi de Jean IV Lascaris Biographie Naissance décembre 1221 /début 1222 Nicée ( empire de Nicée",
    "Karevo",
    "février",
    "Espagne",
    "Liste des comtes de Troyes",
    "(lieu",
    "Élisabeth",
    "Rue Ambroise-Paré",
    "Saint-Empire romain germanique",
    "Jean de Joinville",
    "Buenos",
    "Colonie de la rivière Rouge",
    "Saint-Hippolyte",
    "Hoàng Trù",
    "Empire byzantin",
    "Astronomie",
    "Rhodésie du Sud",
    "Neuwaldegg",
    "Annequin",
    "Nationalité Britannique Décès 24 avril 1956 (à 85 ans",
    "Liste des ducs de Lorraine",
    "janvier",
    "Constance de Bretagne",
    "Hurstville",
    "historien",
    "Rue du Faubourg-Saint-Martin",
    "Latium",
    "Hugues IV de Bourgogne",
    "Amandus",
    "Haut-Empire romain",
    "Geoffroy II de Bretagne",
    "Spitalfields",
    "Manickpur",
    "Bury",
    "Julius Sabinus",
    "Beornred",
    "Sunrise",
    "Près",
    "Liste des comtesses et duchesses d'Anjou",
    "Michel III",
    "pont",
    "Rue Mouton-Duvernet",
    "Duché de Normandie",
    "Château de Genève",
    "Base",
    "Tavistock",
    "Norvège",
    "Staurakios",
    "Guillaume IV de Hesse-Cassel",
    "Maison de Bourbon",
    "16e",
    "Parafianovo",
    "Kensington",
    "Thibaud l'Ancien",
    "Perse",
    "av. J.-C.",
    "Boulevard de Port-Royal",
    "Astor",
    "Province du Qwara",
    "Michel II l'Amorien",
    "Petrolia",
    "Michel IV le Paphlagonien",
    "Pyrohiv",
    "Thierry Ier",
    "Hôtel",
    "Taron",
    "Période Doukas Précédé par Michel VII Doukas Usurpé par Nicéphore Basilakios Nicéphore Mélissène Suivi de Alexis I er Comnène Biographie Naissance vers 1001 Décès 10 décembre",
    "Pokrovskoïe ( Empire russe",
    "Hongrie",
    "Indochine française",
    "-",
    "Conrad de Montferrat",
    "18e",
    "Valentinien Ier",
    "Croydon",
    "Liste des seigneurs de Roannais",
    "Wessex",
    "Springwells",
    "Lead",
    "Maurice",
    "Arrondissement de Man'gyŏngdae",
    "Hong Kong (colonie)",
    "Stone",
    "Huire,",
    "Battle Picture Weekly",
    "Cameron",
    "Karang",
    "Guerre des Despenser",
    "dans",
    "Malte",
    "Quai du Louvre",
    "Chalfont",
    "Julia Caesaris Maior",
    "Ogidi",
    "en",
    "]",
    "Liste des comtes palatins de Bourgogne",
    "Lucius Aurelius Cotta",
    "Morée",
    "Royaume de Valence",
    "Cilicie",
    "Tamayy",
    "Munsieville",
    "Duché de Clèves",
    "Domitien",
    "Fort",
    "Maison de Lusignan",
    "Gambie",
    "Mathilde d'Auvergne",
    "Zhejiang",
    "Rue de l'Arcade (Paris)",
    "Aurelia Cotta",
    "Royaume de Naples",
    "Jean sans Peur",
    "Hugues X de Lusignan",
    "Bosco",
    "Salt",
    "Guillaume II de Craon",
    "Terentius Maximus",
    "Jean",
    "Athanagilde Ier",
    "Cölln",
    "paroisses",
    "Sassanides",
    "Tunisie",
    "Lucius Cornelius Cinna",
    "Guillaume V de Nevers",
    "Henri Ier de Champagne",
    "Caecilii",
    "Iaroslav le Sage",
    "Pedro Manrique de Lara",
    "8e",
    "Molay",
    "succession",
    "Période Macédonienne Précédé par Zoé Porphyrogénète Romain III Argyre Co-empereur Zoé Porphyrogénète (1028-1050",
    "Alden",
    "of=",
    "Sant'Andrea di Barbarana",
    "Palais-musée de Tsarskoïe Selo",
    "Période Macédonienne Précédé par Constantin VIII Co-empereur Romain III Argyre (1028-1034",
    "Jean III de Navarre",
    "Pescennius Niger",
    "Louis le Pieux",
    "Isabelle de Valois",
    "Liste des ducs d'Auvergne",
    "Ballybricken",
    "Iunii",
    "Ofatinți",
    "Rue",
    "Fuente",
    "Clifton",
    "Québec)",
    "Canadiens de Montreal",
    "Union des republiques socialistes sovietiques",
    "Valens",
    "Marlborough",
    "juin",
    "Liste des comtes de Saint-Pol",
    "Grand River",
    "Angelo Sanudo",
    "etit Palais (Avignon)",
    "Quintus Marcius Rex",
    "Othon IV de Bourgogne",
    "Hugues VI de Lusignan",
    "Mendorf,",
    "Idle",
    "Bibliographie",
    "Ecgberht",
    "Titres",
    "Ōhara",
    "Rue Demarquay",
    "Batanée",
    "Elizabethtown",
    "Knut le Grand",
    "2e",
    "Miniambaladougou",
    "Le",
    "Ordre cistercien",
    "Joinville",
    "Rue Jean-Pierre-Timbaud",
    "Mur",
    "Département de Constantine",
    "Gouvernement de Vologda",
    "Période Lascaris Précédé par Théodore I er Lascaris Suivi de Théodore II Lascaris Biographie Naissance vers 1192 Didymotique ( Empire byzantin",
    "p.",
    "Deacon's",
    "Empire d'Autriche",
    "Statuts de l'ordre de Saint-Michel",
    "Simon de Dammartin",
    "Los",
    "12e",
    "Empire romain",
    "Caldwell",
    "Montquin",
    "Arthur III de Bretagne",
    "Hobița",
    "Oulkhou",
    "Saint-Pierre-de-Caravenchel",
    "Felice Varini",
    "Shadwell",
    "Soudan anglo-égyptien",
    "Union",
    "Alain IV de Bretagne",
    "Marie de Bretagne",
    "Marguerite de Bar",
    "Kings",
    "Florent Ier de Frise occidentale",
    "Ordination",
    "Royaume de Macédoine",
    "Northumberland (comté)",
    "Charles II de Lorraine",
    "Duc des Francs",
    "Stinsford,",
    "Maison",
    "Saint-Henri",
    "Ach-Charqiya (Égypte)",
    "Rue Clément",
    "Charny",
    "Liste des comtes et ducs de Touraine",
    "Charles Ier de Bourbon",
    "Rue Louise-Émilie-de-La-Tour-d'Auvergne",
    "Guillaume VIII d'Aquitaine",
    "Suzanne de Bourbon",
    "Jeanne de Navarre",
    "Bad",
    "Maison de Choiseul",
    "Hugues Ier de Vermandois",
    "Lugal-zagesi",
    "Thibaud Ier de Blois",
    "de",
    "Podolie",
    "St.",
    "Plympton",
    "Hünshoven",
    "6ee341124611/Le Berceau de Dieu - Joseph (André Roanne) et Pharaon (Joë Hamman).jpg",
    "Réserve",
    "Arrondissement de Bergedorf",
    "14e",
    "Valerii",
    "Vitrail",
    "Maison de Sponheim",
    "Carignan",
    "Royaume d'Italie (Saint-Empire romain)",
    "Barretina",
    "Sophie",
    "Rue Monge",
    "Valdicastello,",
    "Lye",
    "Saint Pol Aurélien",
    "Califat omeyyade",
    "Adélaïde",
    "Depoy,",
    "Foulques Ier d'Anjou",
    "calendrier musulman",
    "Langage",
    "Durwood,",
    "Canada",
    "Plum",
    "Robert de Bruce",
    "Fenny",
    "Boulevard Saint-Martin (Paris)",
    "Diocèse d'Agen",
    "Liste des comtes d'Albon puis dauphins de Viennois",
    "Carin",
    "Liste des comtes et ducs de Valois",
    "Duché de Saxe",
    "Brady",
    "Mercie",
    "Commanderie",
    "Terre",
    "Liste des comtes et ducs de Chartres",
    "Danemark",
    "Andastan",
    "Faubourg",
    "Hugues V de Lusignan",
    "Années 1560",
    "Alcazar",
    "Liste des ducs et duchesses de Brabant",
    "South",
    "Jaloudok",
    "Fordstown",
    "Carpates",
    "Liste des souverains de Kiev#Grands-princes de Kiev",
    "Espagne wisigothique",
    "Jean-Louis de Savoie",
    "Holloway,",
    "Couronne de Castille",
    "Maison de Nevers",
    "Rue des Petits-Champs",
    "rue",
    "Mirza",
    "Liste des souverains de Brandebourg",
    "Famille Neville",
    "Denkhok",
    "West Kensington",
    "S:t",
    "Andronic Doukas",
    "Allegheny",
    "Great",
    "Gui de Dampierre",
    "Marguerite d'York",
    "Killaloe, Comté de Clare",
    "Liste des comtes de Soissons",
    "Ray",
    "Craon",
    "Liste des comtes de Rennes",
    "Comte",
    "Caecilii Metelli",
    "Tsarskoïe",
    "Maison de Dunkeld",
    "Terre sainte",
    "Gouvernement de Vladimir",
    "Philippe d'Alsace",
    "5e",
    "11e",
    "Louise de Savoie",
    "Westerham",
    "Alexandre",
    "Père",
    "Robert III de Flandre",
    "Kirkcudbrightshire",
    "Liste des dauphins d'Auvergne",
    "Royaume d'Italie (1861-1946)",
    "Hugues XII de Lusignan",
    "République de Weimar",
    "Vernon",
    "Duché d'Aquitaine",
    "Hamburg-Finkenwerder",
    "Norfolk",
    "desktopArticleTarget-targetContainer",
    "Nationalité Américaine Décès 2 juin 1981 (à 78 ans",
    "Palazzo",
    "Liste des conjoints des souverains de Naples",
    "Aurum",
    "Fullersburg",
    "Liste des comtes de Pardiac",
    "Croatie",
    "District",
    "Clovis Ier",
    "Herennius Etruscus",
    "Lieu",
    "Isabelle de Luxembourg",
    "Khamag Mongol",
    "Kayâ,",
    "Marguerite Aldobrandini",
    "Rue de Chaillot",
    "Rue du Faubourg-Saint-Honoré",
    "Assam",
    "Raj",
    "Province d'Afrique",
    "Raymond II de Tripoli",
    "Middelburg",
    "Eadwulf",
    ".",
    "Liste des comtes de Flandre",
    "Décès 28 juin 1385 (à 37 ans",
    "Maison de Barcelone",
    "Pape",
    "Liste des comtes puis ducs de Rethel",
    "Carlton",
    "Seconde maison de Bourbon-Montpensier",
    "Maurice V de Craon",
    "Paroisse de Saint James",
    "certain",
    "Odoacre",
    "Adams",
    "Julianus",
    "Wöhrd",
    "Liste des ducs de Schleswig",
    "Wiltshire",
    "Beeston",
    "Nouveau-Brunswick",
    "Rococo",
    "Abeadzi",
    "Rio",
    "Ville-Marie (ancien nom de Montréal)",
    "Marie de Juliers-Berg",
    "(~",
    "Raj britannique",
    "Paroisse de Sainte-Catherine",
    "Wolanka",
    "Wayne",
    "Sigismond",
    "Titus Quinctius Capitolinus Barbatus",
    "June Pointer",
    "Famille de Beaumont",
    "Catherine Woodville",
    "Calvinisme",
    "Vicomte",
    "Belgique",
    "Guatemala",
    "Pannonie",
    "Black Hills",
    "Cass",
    "Serguievka",
    "Empire russe",
    "Jean de Brienne",
    "Données clés Prédécesseur Isabelle le Despenser Successeur Élisabeth de Bohun Comtesse de Surrey 30 juin 1347 – 11 janvier",
    "Rottluff,",
    "Rue Sainte-Anne (Paris)",
    "Liste des comtes de Rodez",
    "Renfrew (Ontario)",
    "Maison d'York",
    "Aholičy",
    "Nottinghamshire",
    "Louis de Valois",
    "Algérie française",
    "Charles III de Bourbon",
    "Maison de la Cerda",
    "Bab",
    "Isabelle de Savoie",
    "Liste des monarques de France",
    "Maison de Wessex",
    "Cavalerie",
    "Perticara",
    "Valmont",
    "Albert Ier de Hainaut",
    "Herbert Ier de Vermandois",
    "Empire perse",
    "Derbyshire",
    "Ewodi",
    "Romagne",
    "Mayfield",
    "RSSA du Nakhitchevan",
    "Liste des comtesses de Flandre",
    "Užpaliai,",
    "Vieux",
    "voïvodie",
    "Comté de Hainaut",
    "Rue des Bourdonnais",
    "Deer",
    "Alix de Bretagne",
    "Château de Dillenbourg",
    "Smbat VIII Bagratouni",
    "Hale's",
    "Philippe d'Artois",
    "Glengormley",
    "Colonie du Cap",
    "Maroc",
    "Isaac",
    "Ozeriany",
    "Palace",
    "Alphonse Jourdain",
    "Vienne",
    "Santarcangelo",
    "–",
    "Fairfield,",
    "Schmiedefeld",
    "Maison de Habsbourg",
    "Bivinides",
    "Lucceius Albinus",
    "Charles V d'Anjou",
    "Newton",
    "Lucius Quinctius Cincinnatus",
    "Jeanne de Marle",
    "Ciudad",
    "Charles de Valois",
    "Bon-Secours",
    "Liste des comtes d'Armagnac",
    "Liste des comtes de Toulouse",
    "Grec ancien",
    "Valash",
    "Malye",
    "Place Charles-Dullin",
    "Ceolred",
    "Nassarao",
    "Monobaze Ier",
    "Raoul IV de Vexin",
    "Giarre-Riposto",
    "Kondol",
    "Constance Doukas",
    "Manor",
    "Liste des rois de Chypre",
    "Sri",
    "Chicora",
    "Tower Hill (Londres)",
    "Avitus",
    "Rue de Grenelle",
    "Hampstead",
    "Royaume de l'Aurès",
    "Coumanie",
    "Noms chinois",
    "Teutendorf",
    "Slezská",
    "Guillaume Ier de Craon",
    "Tour",
    "Dame de compagnie",
    "Ville libre d'Empire de Besançon",
    "Rebbelberga",
    "Philippe de Saint-Pol",
    "La Nuit du carrefour",
    "Toscane",
    "Maison de Chalon-Arlay",
    "Del",
    "Royaume de Cordoue",
    "Maison d'Anjou-Sicile",
    "Turquie",
    "Heyshott",
    "Enguerrand VII de Coucy",
    "Casimir Ier de Cujavie",
    "Arthur II de Bretagne",
    "Landgrave",
    "Lech le Blanc",
    "Paw",
    "château",
    "Liste des comtes de Champagne",
    "Mix",
    "Chypre (pays)",
    "Henri III de Brabant",
    "Östra",
    "Royaume de Castille",
    "Rue de Seine",
    "Sardaigne",
    "Duché de Châteauvillain",
    "Jean Ier de Namur",
    "Dynastie Han",
    "Catherine de France",
    "statue",
    "Rovine",
    "Charles II d'Albret",
    "Norfolk (comté)",
    "Louis Ier",
    "Syrie",
    "Kent",
    "Jean Ier de Choiseul",
    "Sainte-Rose (Laval)",
    "Yolande de Bourgogne",
    "Royaume de Navarre",
    "Sépulture",
    "Freidorf",
    "Jeanne Ire",
    "Conan IV de Bretagne",
    "Louis Ier de Chiny",
    "Empire",
    "Edenburg",
    "Magnus Ier de Saxe",
    "Constantin",
    "Stirlingshire",
    "Jean Ier de Craon",
    "Valentinien II",
    "Geoffroi Ier de Bretagne",
    "Louis-Alexandre",
    "Simon de Joinville",
    "Maison de Bourgogne au Portugal",
    "Province de Hamedan",
    "Green",
    "Henri II le Pieux",
    "Owain",
    "Pagus Bracbatensis",
    "Green's",
    "Liste des comtes de Hainaut",
    "Beorhtric",
    "Empire mongol",
    "von",
    "Frogmore",
    "Cheshire (comté)",
    "Fédération de <br",
    "Acton",
    "Période Macédonienne Précédé par Zoé Porphyrogénète Michel IV le Paphlagonien Co-empereur Zoé Porphyrogénète (1028-1050",
    "Conflits",
    "Henri Ier de Brandebourg",
    "Charles d'Artois",
    "Cullercoats",
    "Maison de Haro",
    "Knut d'York",
    "Liste des reines de Navarre",
    "Thomas Montagu",
    "Pascweten",
    "Liste des comtes de Namur",
    "Royaume d'Aragon",
    "Robert II de Dreux",
    "Szetejnie",
    "Maison d'Albret",
    "Barnesboro",
    "Julie Taymor",
    "Origine",
    "Bourgogne",
    "Lucius Furius Medullinus",
    "Pologne",
    "Henri Ier de Vianden",
    "Provinces-Unies",
    "Hannah",
    "Nevill",
    "Jeanne de Ponthieu",
    "Athaulf",
    "Taras",
    "Marino",
    "Neufchâteau",
    "est",
    "Alexis Ier Comnène",
    "Virginio Orsini",
    "Seigneur",
    "Sancha de Castille",
    "Fenenna de Cujavie",
    "Currie,",
    "Castledawson",
    "Rocky",
    "Henri Ier de Brabant",
    "Liste des ducs de Nemours",
    "Sibodal",
    "Essex",
    "Maire du palais",
    "Toxteth",
    "Héricourt",
    "Piémont",
    ";",
    "Jaunpils",
    "Jean Arthur",
    "Ferry IV de Lorraine",
    "Penza Nationalité Empire russe Décès 2 février 1940 (à 65 ans",
    "Jean Ier de Chalon",
    "Liste des souverains de Provence",
    "Boson de Provence",
    "Thessalie",
    "Maple Leafs de Toronto",
    "Latin",
    "Kirkwood",
    "Rangers de New York",
    "Blackhawks de Chicago",
    "Bruins de Boston",
    "Liban",
    "Ordre national de la Legion d'honneur",
    "Scenariste",
    "page",
    "Nigeria",
    "Bresil",
    "Ethiopie",
    "Senegal",
    "Flyers de Philadelphie",
    "Mexique",
    "Jamaique",
    "Penguins de Pittsburgh",
    "Argentine",
    "Red Wings de Detroit",
    "Kings de Los Angeles",
    "Nouvelle-Zelande",
    "Universite Paris-I-Pantheon-Sorbonne",
    "Canucks de Vancouver",
    "Sabres de Buffalo",
    "Islanders de New York",
    "Chine",
    "Oilers d'Edmonton",
    "Ghana",
    "Iran",
    "Roumanie",
    "Devils du New Jersey",
    "Blues de Saint-Louis",
    "pages",
    "Harrow School",
    "Theologie",
    "Trinity College (Cambridge)",
    "Ouganda",
    "Haiti",
    "d:Q10710237",
    "Flames de Calgary",
    "Saison 2018 de la NFL",
    "Saison 2017 de la NFL",
    "Saison 2016 de la NFL",
    "Universite de Californie a Berkeley",
    "Universite Harvard",
    "Fief",
    "Cuba",
    "Saison 2015 de la NFL",
    "Islande",
    "Universite Columbia",
    "Ordre de l'Empire britannique",
    "Autriche",
    "d:Q6106068",
    "Sharks de San Jose",
    "Chili",
    "Universite de Cambridge",
    "en:China (region)",
    "Panthers de la Floride",
    "King's College (Cambridge)",
    "Capitals de Washington",
    "en:Hedvig Eleonora Parish",
    "Avalanche du Colorado",
    "Madagascar",
    "Saison 2014 de la NFL",
    "Thailande",
    "Universite d'Oxford",
    "Institut d'etudes politiques de Paris",
    "Taiwan",
    "Catholicos",
    "Grece",
    "Americans de Rochester",
    "Arabie saoudite",
    "Universite de Chicago",
    "Nordiques de Quebec",
    "Ecole normale superieure (Paris)",
    "Universite Paris-Sorbonne",
    "HK CSKA Moscou",
    "Sri Lanka",
    "Senateurs d'Ottawa",
    "Saison 2020 de la NFL",
    "Saison 2013 de la NFL",
    "Saison 2019 de la NFL",
    "Maurice (pays)",
    "Realisateur",
    "Pretre catholique",
    "Bears de Hershey",
    "Finlande",
    "Seconde Guerre mondiale",
    "Benin",
    "Rwanda",
    "Ordre national du Merite (France)",
    "Lokomotiv Iaroslavl",
    "Hampshire (Angleterre)",
    "Irak",
    "d:Q10546040",
    "Luxembourg",
    "Venezuela",
    "Hurricanes de la Caroline",
    "Ordre de Saint-Michel",
    "Universite Yale",
    "Barbade",
    "Lightning de Tampa Bay",
    "Universite de Princeton",
    "2010",
    "Pakistan",
    "Philippines",
    "Universite Laval",
    "2011",
    "Ducks d'Anaheim",
    "Ecole des hautes etudes en sciences sociales",
    "Ligue americaine de hockey",
    "Wolves de Chicago",
    "Christ Church (Oxford)",
    "d:Q39297398",
    "Ukraine",
    "d:Q10570835",
    "Predators de Nashville",
    "HK Dinamo Moscou",
    "Blue Jackets de Columbus",
    "Admirals de Milwaukee",
    "St John's College (Cambridge)",
    "Saison 2021 de la NFL",
    "Producteur de cinema",
    "Soudan",
    "Mali",
    "Universite Stanford",
    "Lituanie",
    "Ordre du Canada",
    "Middlesex (Angleterre)",
    "Languedoc",
    "Guinee",
    "Stars de Dallas",
    "en:Engelbrekt Parish",
    "Republique du Congo",
    "Universite de Londres",
    "Bulgarie",
    "Guerre de Succession d'Espagne",
    "d:Q54006791",
    "Bulldogs de Hamilton",
    "Saison 2009 de la NFL",
    "SKA Saint-Petersbourg",
    "Perou",
    "Entraineur (handball)",
    "Westminster School",
    "Crunch de Syracuse",
    "North Stars du Minnesota",
    "Universite Paris-Nanterre",
    "Tchad",
    "Shropshire",
    "Koweit",
    "HIFK",
    "Ville de Bruxelles",
    "Tchequie",
    "Saison 2022 de la NFL",
    "Congo belge",
    "en:Hedvig Eleonora and Oscar Parish",
    "Afghanistan",
    "Jets de Winnipeg (1972-1996)",
    "Saison 2012 de la NFL",
    "Saison 2005 de la NFL",
    "Mississippi (Etat)",
    "Wolf Pack de Hartford",
    "d:Q3433770",
    "Ordre des Palmes academiques",
    "Mer",
    "Thrashers d'Atlanta",
    "Saison 2011 de la NFL",
    "Genes",
    "Japonais class=lang-ja lang=ja",
    "Zimbabwe",
    "Kloten Flyers",
    "Saison 2006 de la NFL",
    "Universite de Montreal",
    "Bruins de Providence",
    "d:Q10550317",
    "Falcons de Springfield",
    "Universite de Pennsylvanie",
    "Sound Tigers de Bridgeport",
    "Krylia Sovetov",
    "Hockey Club Fribourg-Gotteron",
    "Brynas IF",
    "Ile de Wight",
    "Queensland",
    "Club des patineurs de Berne",
    "Whalers de Hartford",
    "Griffins de Grand Rapids",
    "Chanteur",
    "Guerre de Sept Ans",
    "d:Q210787",
    "Nouvelle-Ecosse",
    "Staffordshire",
    "Georgie (pays)",
    "Frolunda HC",
    "Colombie",
    "2009",
    "Universite d'Edimbourg",
    "Pirates de Portland",
    "Penguins de Wilkes-Barre/Scranton",
    "Saison 2010 de la NFL",
    "Guerre de la Ligue d'Augsbourg",
    "Wild du Minnesota",
    "en:Gentofte",
    "Togo",
    "Hockey Club Davos",
    "Adler Mannheim",
    "Traktor Tcheliabinsk",
    "Francais",
    "Universite Johns-Hopkins",
    "Burkina Faso",
    "Universite du Michigan",
    "Universite Cornell",
    "Avangard Omsk",
    "Tibetain",
    "Prete a",
    "Lada Togliatti",
    "Charterhouse School",
    "Ecole pratique des hautes etudes",
    "Universite Paris-VIII-Vincennes-Saint-Denis",
    "Rouen hockey elite 76",
    "Universite de New York",
    "Liaoning",
    "Empire chinois",
    "Uruguay",
    "Saison 2008 de la NFL",
    "Hockey Club Bienne",
    "Ecosse",
    "Libye",
    "Admirals de Norfolk (LAH)",
    "Republique romaine",
    "Peinture (art)",
    "d:Q43549106",
    "Bolivie",
    "Coyotes de Phoenix",
    "Herefordshire",
    "Paroisse de Clarendon",
    "Senators de Binghamton",
    "Schlittschuh Club Langnau Tigers",
    "River Rats d'Albany",
    "Kerala",
    "Tanganyika (territoire)",
    "Monarchs de Manchester (LAH)",
    "Baroque",
    "Croix de guerre 1914-1918 (France)",
    "Maroons de Montreal",
    "Washington (district de Columbia)",
    "Society of Antiquaries of London",
    "Biarritz olympique Pays basque",
    "Djurgarden Hockey",
    "Saison 2023 de la NFL",
    "MODO Hockey",
    "Personnalite politique",
    "Palestine (region)",
    "Moose du Manitoba",
    "East Lothian",
    "Graveur",
    "Indonesie",
    "Manly (Sydney)",
    "College royal militaire de Sandhurst",
    "Sillery (Quebec)",
    "Universite de Californie a Los Angeles",
    "Zambie",
    "Batavia (Indes neerlandaises)",
    "Marlies de Toronto",
    "Birmanie",
    "Leksands IF",
    "Emirats arabes unis",
    "Paraguay",
    "Skelleftea AIK",
    "Guillaume V de Juliers",
    "hypothèse",
    "Kona Nord",
    "Maredudd ap Gruffydd",
    "Jomei",
    "Charles",
    "Saad al-Dawla",
    "Henri Ier",
    "Maison de Bourbon-La Marche",
    "Raoul II de Brienne",
    "Yolande d'Aragon",
    "Guy de Luxembourg-Ligny",
    "Vienne",
    "Coldirodi",
    "Guillaume Ier de Hainaut",
    "Guerre de Cent Ans",
    "Louise",
    "Lewisham",
    "Rollonides",
    "Daniel Mesguich",
    "Coffeen",
    "Hawarden",
    "Podgórze (Cracovie)",
    "Charles IV du Maine",
    "Richard Ier de Normandie",
    "Dobbs",
    "Dompierre",
    "Seigneurie d'Ibelin",
    "Pont-l'Évêque",
    "Saint-Omer",
    "Hunan",
    "Bertrade de Montfort",
    "Jean-Guillaume de Clèves",
    "Guillaume Ier de Bourgogne",
    "Temple",
    "Daniel de Galicie",
    "Taraise de Constantinople",
    "Hallebardier",
    "Comté de Brunswick (Basse-Saxe)",
    "Londres,",
    "Données clés Prédécesseur Création du titre Successeur Confiscation du titre Fonctions militaires Commandement Lord lieutenant d'Irlande Faits d’armes Bataille de Bosworth Bataille de Stoke Conflits Guerre des Deux-Roses Biographie Dynastie Famille de la Pole Distinctions Ordre du Bain Naissance 1462 ou 1464 Décès 16 juin",
    "Belmonte",
    "Mathilde de Brabant",
    "Liste des comtes de Ligny",
    "Väversunda",
    "Ville libre de Cracovie",
    "Wuxing",
    "Iaroslavl Décès 1 er mars 1936 (à 63 ans",
    "Charles Ier d'Anjou",
    "Shannonbridge",
    "Royaume de Géorgie",
    "Voisenon",
    "Bosonides",
    "Alain d'Albret",
    "New York%2C N.Y.%2C ca. Aug. 1947) (LOC) (4843140781).jpg",
    "Warwickshire",
    "Sheen",
    "Schöneberg",
    "Constance de Portugal",
    "Gaule romaine",
    "lagune et au sud la baie de Carthagène",
    "Rue de la Verrerie (Paris)",
    "Al-Jamāliyah",
    "Tyrone",
    "Royaume de Portugal",
    "Élisabeth de Clèves (1378-1430)",
    "São",
    "Paul de Constantinople",
    "Glenlohan",
    "Grenade (pays)",
    "Raymond V de Toulouse",
    "anecdote",
    "Gravelly",
    "Bernicie",
    "Herman de Hainaut",
    "Mathilde de Carinthie",
    "Geoffroy Ier de Lusignan (seigneur de Vouvant)",
    "Chatham",
    "Marian-glas",
    "ourceLoaderDynamicStyles",
    "Mongolie",
    "Nutahigashi,",
    "Aquitaine",
    "Ivarr de Waterford",
    "Tchijovo",
    "Liste des comtesses de Hollande",
    "Guy XII de Laval",
    "Robert Ier de Flandre",
    "Anne",
    "Liste des monarques de Danemark",
    "photographe",
    "Sinuessa",
    "Portugal",
    "Abdon",
    "Afrique du Sud",
    "Gilbert de Montpensier",
    "Empire romain d'Occident",
    "Ouïezd",
    "Ivy",
    "Le facteur sonne toujours deux fois (film, 1946)",
    "Antigonides",
    "Liste des comtes puis ducs de Montpensier",
    "Famille de Bueil",
    "Charlesbourg",
    "Pierre Ier",
    "Clytemnestre",
    "Thibaut VI de Blois",
    "Maximin Ier le Thrace",
    "Sophie de Rheineck",
    "Garden",
    "Kirkharle",
    "Liste des seigneurs de Ravensberg",
    "Usurpateur romain",
    "Marie Stuart",
    "Raoul Ier de Soissons",
    "Elpidius",
    "Sant Gervasi de Cassoles",
    "Califat abbasside",
    "Berkswell",
    "Chypre",
    "Comté d'Édesse",
    "Duché de Bavière-Ingolstadt",
    "Époque",
    "Tabarestan",
    "Jean II de Bourgogne",
    "Galba",
    "Tinta,",
    "Seigneurie de Naplouse",
    "Eloxochitlán",
    "Isabelle de Brienne",
    "Concession française de Shanghai",
    "Juan",
    "Journal",
    "Nolde",
    "Waccho",
    "Guy XVI de Laval",
    ". (la",
    "Saint-Louis",
    "Collégiale Saint Georges",
    "Center",
    "Royaume d'Est-Anglie",
    "Lorette",
    "Bowden",
    "Jean de Bourgogne",
    "Capitaine",
    "Lancashire",
    "Abbaye Sainte-Madeleine de Geneston",
    "Traduction",
    "Lužki",
    "Kunzendorf,",
    "lieu",
    "fils,",
    "Louis II de Chalon-Arlay",
    "Géjé",
    "Constance de France",
    "Paul II",
    "Conan Ier de Bretagne",
    "Asie centrale",
    "Isabelle de Meulan",
    "Liste des comtes de Barcelone",
    "Geoffroy Ier de Marseille",
    "Philippe II de Bourgogne",
    "Saint",
    "États-Unis",
    "Henri III de Louvain",
    "Louis-Philippe Ier",
    "Claude Catherine de Clermont",
    "Casimir II le Juste",
    "Comminges",
    "Jeanne d'Armagnac",
    "1er",
    "Flandre",
    "Bohême",
    "Royaume des Massyles",
    "Gerberge de Provence",
    "Agdjibedi,",
    "Hollingworth",
    "Famille Sanudo",
    "palmarès",
    "taille (anthropométrie)",
    "nom",
    "française",
    "taille",
    "alive",
    "taille 1",
    "(consulté",
    "québec",
    "canadienne",
    "américaine",
    "doctorat",
    "nationalités",
    "formation",
    "club",
    "press",
    "parlement d'angleterre",
    "royaume-uni de grande-bretagne et d'irlande",
    "arts visuels",
    "arabe",
    "natation sportive",
    "préfecture",
    "ontario",
    "britannique",
    "empire ottoman",
    "hong",
    "il",
    "elle",
    "hong kong (colonie)",
    "corée du sud",
    "parcours",
    "prpoids de formeess",
    "surrey (comté)",
    "pseudonyme",
    "or",
    "militantisme",
    "les",
    "catégorie",
    "histoire de l'art",
    "surnom",
    ":",
    "yorkshire",
    "essaie",
    "carrière",
    "tibet",
    "ohio",
    "nouvelle",
    "texas",
    "anthropologie",
    "disc jockey",
    "linguistique",
    "irlande",
    "st",
    "corée",
    "floride",
    "afrique du sud",
    "grec moderne",
    "records",
    "massachusetts",
    "michigan",
    "illinois",
    "las",
    "belge",
    "roman policier",
    "période",
    "exploration",
    "art contemporain",
    "gravure",
    "mannequinat",
    "john",
    "louis",
    "hertfordshire",
    "tel",
    "villa",
    "saison",
    "hull (québec)",
    "massachusetts institute of technology",
    "football",
    "port",
    "kingston",
    "xian",
    "langues chinoises",
    "jonquière",
    "française",
    "professeur",
    "russe",
    "pierre",
    "north",
    "françois",
    "tripoli",
    "wisconsin",
    "connecticut",
    "côte d'ivoire",
    "république",
    "caractéristiques",
    "suisse",
    "province",
    "jazz",
    "nouvelle-galles du sud",
    "royaume d'angleterre",
    "east",
    "bachelor of arts",
    "laval",
    "entraîneur",
    "tchécoslovaquie",
    "jeux olympiques antiques",
    "guitare",
    "liste de peintres italiens",
    "minnesota",
    "consul",
    "allemande",
    "royaume d'italie",
    "indiana",
    "anglais",
    "bachelor of science",
    "william",
    "sussex",
    "beaux-arts de paris",
    "7e",
    "japonaise",
    "sicile",
    "iowa",
    "trinity college",
    "lincolnshire",
    "devon (comté)",
    "animateur",
    "astronomie amateur",
    "kham",
    "autres",
    "mount",
    "louisiane",
    "piano",
    "situation",
    "rallye automobile",
    "république démocratique du congo",
    "saskatchewan",
    "chef tribal",
    "chevalier",
    "musique classique",
    "libanaise",
    "suffolk",
    "royaume",
    "rap",
    "reggae",
    "jiangsu",
    "calligraphie",
    "oxfordshire",
    "nationalité",
    "décès",
    "activité",
    "ancien",
    "new",
    "alive",
    "enseignement",
    "poste",
    "san",
    "paroisse",
    "los",
    "biographie",
    "saint",
    "royaume de france",
    "californie",
    "genre",
    "activités",
    "traduction",
    "grec ancien",
    "empire russe",
    "comté",
    "new jersey",
    "são",
    "empire romain",
    "buenos",
    "haut-empire romain",
    "district",
    "chicoutimi",
    "croydon",
    "père",
    "rio",
    "↑ (en)"

]

BAD_WIKI_PAGE = [
    "Art and Language",
    "Saïan Supa Crew",
    "G-Unit",
    "D-Block Europe",
    "Vitor Hublot",
    "5.5 designers",
    "Le Klub des 7",
    "Chocolate Genius Inc.",
    "83 (collectif)",
    "Spoke Orkestra",
    "Maison d'édition",
    "Histoire de la médecine dentaire",
    "Histoire de ma vie (Casanova)",
    "Histoire de vie",
    "Histoire des fonctions trigonométriques",
    "L'Histoire est une littérature contemporaine",
    "L'Incroyable Histoire du facteur Cheval",
    "Société africaine de plantations d'hévéas",
    "Société d'accélération du transfert de technologies",
    "Société d'études de l'histoire régionale du pays de l'Ems",
    "Société patriotique du Luxembourg",
    "Prix Alfred-Kordelin",
    "Prix Costa",
    "Prix Watson Davis et Helen Miles Davis",
    "Prix d'histoire André-Castelot",
    "Benedetta (film)",
    "Dangal (film),"
    "Frida (film)",
    "William Stage Boyd",
    "Wardell Poochie Fouse",
    "Al TNT Braggs",
    "Benjamin Pap Singleton",
    "Carlton Santa Davis",
    "Demetrius Hook Mitchell",
    "Edmund Trotsky Davies",
    "Floyd Candy Johnson",
    "Frances Franco Stevens",
    "Freddie Fingers Lee",
    "Gene Bowlegs Miller",
    "Greg Cadillac Anderson",
    "Jacques-Antoine Cassiodore Demonchaux",
    "Jacques Kako Bessot",
    "John Charlie Whitney",
    "Johnny Man Young",
    "Leon Ndugu Chancler",
    "Mohibullah Mo Khan",
    "Peter Cool Man Steiner",
    "Richard Humpty Vission",
    "Royce da 5'9",
    "Sergio Pipian Martinez",
    "Sidney Big Sid Catlett",
    "Thomas Tom Flanagan",
    "Maison d'Este",
    "Maison de Fürstenberg",
    "Maison de Gonzague",
    "Maison de Hohenlohe",
    "Maison de Joyeuse",
    "Maison de Montefeltro",
    "Maison de Nicéphore Niépce",
    "Maison de Salm",
    "Maison de Trazegnies",
    "Maison de Wavrin",
    "Maison de Zähringen",
    "Maison de la poésie de Montréal",
    "Maison de naissance d'Isaac Newton",
    "Maison de naissance de Tchaïkovski",

]


TOWN_TO_LOCALISATION_DICT = {
    "berlin":"52° 31′ N, 13° 23′ E",
    "bruxelles":"50° 51′ 01″ N, 4° 21′ 00″ E",
    "hambourg":"53° 33′ N, 10° 00′ E",
    "königsberg":"54° 44′ N, 20° 29′ E",
    "edo (ville)":"35° 41′ 22″ N, 139° 41′ 30″ E",
    "chicoutimi":"48° 25′ 00″ N, 71° 04′ 00″ W",
    "santa":"43° 09′ 57.30″ N, 4° 02′ 49.41″ W",
    "berlin-est":"52° 31′ N, 13° 23′ E",
    "berlin-ouest":"52° 31′ N, 13° 23′ E",
    "berlin est":"52° 31′ N, 13° 23′ E",
    "berlin ouest":"52° 31′ N, 13° 23′ E",
    "valence":"39° 28′ 13″ N, 0° 22′ 36″ W",
    "washington":"38° 53′ 42″ N, 77° 02′ 12″ W",
    "vienne":"48° 12′ 30″ N, 16° 22′ 21″ E",
    "buda (ville)":"47° 28′ N, 19° 03′ E",
    "new york":"40° 42′ 46″ N, 74° 00′ 22″ W",
    "saint-petersbourg":"59° 57′ N, 30° 19′ E",
    "paris":"48° 51′ 24″ N, 2° 21′ 07″ E",
    "woodland hills":"34° 10′ 06″ N, 118° 36′ 18″ O",
    "château de versailles":"48° 48′ 17,26″ N, 2° 07′ 13,34″ E",
    "lichtental":"48° 44′ 38″ N, 8° 15′ 39″ E",
    "aix-la-chapelle":"50° 46′ 00″ N, 6° 06′ 00″ E",
    "tyburn (village)":"51° 30′ 46,3″ N, 0° 09′ 50,4″ W",
    "rome":"41° 53′ 19″ N, 12° 29′ 12″ E",
    "rome antique":"41° 53′ 19″ N, 12° 29′ 12″ E",
    "san francisco (californie)":"48° 12′ 30″ N, 16° 22′ 21″ E",
    "vienne (autriche)":"48° 12′ 30″ N, 16° 22′ 21″ E",
    "hôtel de la reine hortense":"48° 51′ 24″ N, 2° 21′ 07″ E",
    "pella (cité antique)":"40° 45′ 36″ N, 22° 31′ 32″ E",
    "saint-denis":"48° 56′ 08″ N, 2° 21′ 14″ E",
    "surabaya":"7°15′40.71″S 112°44′59.13″E",
    "saint-léger-de-foucheret":"47° 01′ 20″ N, 3° 53′ 55″ E",
    "chateau de versailles":"48° 48′ 17,26″ N, 2° 07′ 13,34″ E",
    "los angeles":"34° 03′ 08″ N, 118° 14′ 37″ W",
    "varsovie":"52° 13′ 47″ N, 21° 00′ 44″ E",
    "madrid":"40° 26′ 00″ N, 3° 41′ 00″ W",
    "montreal":"45° 30′ 32″ N, 73° 33′ 42″ W",
    "constantinople":"41° 00′ 30″ N, 28° 58′ 42″ E",
    "lyon":"45° 45′ 50″ N, 4° 50′ 09″ E",
    "anvers":"51° 13′ 00″ N, 4° 24′ 00″ E",
    "milan":"45° 28′ 00″ N, 9° 10′ 00″ E",
    "prague":"50° 05′ 16″ N, 14° 25′ 14″ E",
    "oslo":"59° 54′ 50″ N, 10° 45′ 08″ E",
    "venise":"45° 26′ 23″ N, 12° 19′ 55″ E",
    "naples":"40° 50′ 00″ N, 14° 15′ 00″ E",
    "dublin":"53° 20′ 36″ N, 6° 16′ 03″ W",
    "florence":"43° 46′ 11″ N, 11° 15′ 21″ E",
    "le caire":"30° 02′ 40″ N, 31° 14′ 09″ E",
    "tokyo":"35° 41′ 22″ N, 139° 41′ 30″ E",
    "munich":"48° 08′ 15″ N, 11° 34′ 32″ E",
    "chicago":"41° 53′ 01″ N, 87° 37′ 44″ W",
    "nice":"43° 42′ 03″ N, 7° 16′ 06″ E",
    "avignon":"43° 56′ 57″ N, 4° 48′ 20″ E",
    "buda (hongrie)":"47° 29′ 52″ N, 19° 02′ 25″ E",
    "alger":"36° 45′ 14″ N, 3° 03′ 32″ E",
    "athenes":"37° 59′ 02″ N, 23° 43′ 39″ E",
    "verdun (montreal)":"45° 27′ 30″ N, 73° 34′ 07″ W",
    "kiev":"50° 27′ 00″ N, 30° 31′ 24″ E",
    "buenos aires":"34° 36′ 13″ S, 58° 22′ 54″ W",
    "cologne":"50° 56′ 15″ N, 6° 57′ 37″ E",
    "amsterdam":"52° 22′ 03″ N, 4° 54′ 15″ E",
    "turin":"45° 04′ 13″ N, 7° 41′ 13″ E",
    "liege":"50° 37′ 57″ N, 5° 34′ 47″ E",
    "nantes":"47° 13′ 06″ N, 1° 33′ 13″ W",
    "cracovie":"50° 03′ 53″ N, 19° 56′ 42″ E",
    "goa":"15° 17′ 57″ N, 74° 07′ 26″ E",
    "lisbonne":"38° 43′ 20″ N, 9° 08′ 21″ W",
    "tbilissi":"41° 42′ 54″ N, 44° 49′ 38″ E",
    "zurich":"47° 22′ 37″ N, 8° 32′ 30″ E",
    "chang'an":"34° 20′ 30″ N, 108° 56′ 23″ E",
    "beauport":"46° 51′ 29″ N, 71° 11′ 42″ W",
    "toronto":"43° 39′ 12″ N, 79° 23′ 00″ W",
    "bologne":"44° 29′ 42″ N, 11° 20′ 33″ E",
    "marseille":"43° 17′ 47″ N, 5° 22′ 11″ E",
    "bagdad":"33° 18′ 55″ N, 44° 21′ 58″ E",
    "rouen":"49° 26′ 36″ N, 1° 05′ 57″ E",
    "jerusalem":"31° 46′ 06″ N, 35° 12′ 49″ E",
    "tours":"47° 23′ 39″ N, 0° 41′ 05″ E",
    "pekin":"39° 54′ 15″ N, 116° 24′ 27″ E",
    "geneve":"46° 12′ 16″ N, 6° 08′ 36″ E",
    "mexico":"19° 25′ 57″ N, 99° 08′ 00″ W",
    "stockholm":"59° 19′ 45″ N, 18° 04′ 07″ E",
    "gand":"51° 03′ 15″ N, 3° 43′ 03″ E",
    "edimbourg":"55° 57′ 12″ N, 3° 11′ 18″ W",
    "lausanne":"46° 31′ 11″ N, 6° 37′ 56″ E",
    "tunis":"36° 48′ 23″ N, 10° 10′ 53″ E",
    "kinshasa":"4° 26′ 31″ S, 15° 15′ 59″ E",
    "leyde":"52° 09′ 36″ N, 4° 29′ 49″ E",
    "barcelone":"41° 23′ 15″ N, 2° 10′ 07″ E",
    "versailles":"48° 48′ 05″ N, 2° 07′ 48″ E",
    "istanbul":"41° 00′ 30″ N, 28° 58′ 42″ E",
    "bordeaux":"44° 50′ 16″ N, 0° 34′ 45″ W",
    "strasbourg":"48° 34′ 24″ N, 7° 45′ 08″ E",
    "toulouse":"43° 36′ 17″ N, 1° 26′ 39″ E",
    "aoste":"45° 44′ 13″ N, 7° 19′ 12″ E",
    "copenhague":"55° 40′ 34″ N, 12° 34′ 06″ E",
    "suva":"18° 07′ 29″ S, 178° 27′ 00″ E",
    "ottawa":"45° 25′ 17″ N, 75° 41′ 50″ W",
    "riga":"56° 56′ 59″ N, 24° 06′ 19″ E",
    "bruges":"51° 12′ 33″ N, 3° 13′ 29″ E",
    "nancy":"48° 41′ 32″ N, 6° 11′ 04″ E",
    "rio de janeiro":"22° 54′ 24″ S, 43° 10′ 22″ W",
    "teheran":"35° 41′ 21″ N, 51° 23′ 20″ E",
    "oxford":"51° 45′ 07″ N, 1° 15′ 28″ W",
    "palais de placentia":"51° 28′ 56″ N, 0° 00′ 24″ O",
    "quebec (ville)": "46° 48′ 50″ N, 71° 12′ 29″ W",
    "scottsdale": "33° 29′ 35″ N, 111° 55′ 34″ W",
    "sillery (quebec)": "46° 46′ 48″ N, 71° 15′ 11″ W",
    "detroit": "42° 19′ 53″ N, 83° 02′ 45″ W",
    "willesden": "51° 32′ 48″ N, 0° 13′ 46″ W",
    "jilin": "43° 51′ 00″ N, 126° 33′ 00″ E",
    "leon": "42° 35′ 00″ N, 5° 34′ 00″ W",
    "semarang": "6° 58′ 00″ S, 110° 25′ 00″ E",
    "nacka": "59° 18′ 60″ N, 18° 10′ 00″ E",
    "etobicoke": "43° 36′ 58″ N, 79° 30′ 45″ W",
    "salvador": "12° 58′ 29″ S, 38° 28′ 36″ W",
    "san francisco": "37° 46′ 39″ N, 122° 25′ 09″ W",
    "woodland hills (los angeles)": "34° 10′ 06″ N, 118° 36′ 18″ W",
    "hollywood": "34° 06′ 06″ N, 118° 19′ 36″ W",
    "guadalajara": "20° 40′ 00″ N, 103° 21′ 00″ W",
    "novi": "42° 28′ 49″ N, 83° 28′ 39″ W",
    "halle": "51° 28′ 00″ N, 11° 58′ 00″ E",
    "shuri": "26° 13′ 01″ N, 127° 43′ 10″ E",
    "north vancouver": "49° 19′ 00″ N, 123° 04′ 00″ W",
    "munster (irlande)": "52° 15′ 00″ N, 9° 00′ 00″ W",
    "halifax": "44° 38′ 51″ N, 63° 35′ 26″ W",
    "reggio": "38° 06′ 52″ N, 15° 39′ 00″ E",
    "ville de tokyo": "35° 41′ 22″ N, 139° 41′ 30″ E",
    "perth": "32° 00′ 00″ S, 115° 54′ 00″ E",
    "salto": "31° 23′ 00″ S, 57° 57′ 00″ W",
    "moulins": "46° 33′ 00″ N, 3° 20′ 00″ E",
    "richmond": "49° 10′ 00″ N, 123° 08′ 00″ W",
    "hull": "53° 45′ 00″ N, 0° 19′ 48″ W",
    "salisbury": "51° 04′ 12″ N, 1° 47′ 24″ W",
    "wilmette": "42° 04′ 38″ N, 87° 42′ 33″ W",
    "chester": "53° 12′ 00″ N, 2° 54′ 36″ W",
    "pointe-noire": "4° 47′ 51″ S, 11° 51′ 01″ E",
    "tolede": "39° 51′ 00″ N, 4° 01′ 00″ W",
    "hastings": "50° 51′ 00″ N, 0° 34′ 00″ E",
    "bergen": "60° 23′ 00″ N, 5° 20′ 00″ E",
    "bath": "51° 22′ 53″ N, 2° 21′ 31″ W",
    "saint-laurent (montreal)": "45° 30′ 26″ N, 73° 40′ 58″ W",
    "newport": "51° 35′ 00″ N, 2° 59′ 00″ W",
    "boston": "42° 21′ 29″ N, 71° 03′ 49″ W",
    "giessen": "50° 35′ 02″ N, 8° 40′ 47″ E",
    "dieppe": "49° 55′ 00″ N, 1° 04′ 00″ E",
    "greenwich": "51° 28′ 40″ N, 0° 00′ 00″ E",
    "achrafieh": "33° 53′ 00″ N, 35° 31′ 00″ E",
    "north york": "43° 45′ 00″ N, 79° 25′ 00″ W",
    "portland": "45° 31′ 12″ N, 122° 40′ 55″ W",
    "durham": "54° 46′ 00″ N, 1° 34′ 00″ W",
    "winchester": "51° 03′ 00″ N, 1° 19′ 00″ W",
    "milton": "43° 31′ 00″ N, 79° 53′ 00″ W",
    "brighton": "50° 49′ 00″ N, 0° 08′ 00″ W",
    "brunswick": "52° 15′ 00″ N, 10° 31′ 00″ E",
    "phoenix": "33° 26′ 00″ N, 112° 04′ 00″ W",
    "montegnee": "50° 38′ 00″ N, 5° 31′ 00″ E",
    "poligny": "46° 50′ 00″ N, 5° 42′ 00″ E",
    "plaisance": "45° 24′ 00″ N, 9° 10′ 00″ E",
    "la havane": "23° 08′ 00″ N, 82° 22′ 00″ W",
    "genes": "44° 24′ 00″ N, 8° 56′ 00″ E",
    "truro": "50° 15′ 00″ N, 5° 03′ 00″ W",
    "dacca": "23° 45′ 00″ N, 90° 24′ 00″ E",
    "auckland": "36° 51′ 00″ S, 174° 46′ 00″ E",
    "grenade (espagne)": "37° 11′ 00″ N, 3° 36′ 00″ W",
    "denpasar": "8° 39′ 00″ S, 115° 13′ 00″ E",
    "dundas (ontario)": "43° 16′ 00″ N, 79° 57′ 00″ W",
    "memphis": "35° 07′ 00″ N, 90° 01′ 00″ W",
    "la haye": "52° 05′ 00″ N, 4° 18′ 00″ E",
    "york": "53° 57′ 00″ N, 1° 05′ 00″ W",
    "palerme": "38° 07′ 00″ N, 13° 21′ 00″ E",
    "manhattan": "40° 47′ 00″ N, 73° 59′ 00″ W",
    "spandau": "52° 32′ 00″ N, 13° 12′ 00″ E",
    "loretteville": "46° 51′ 00″ N, 71° 21′ 00″ W",
    "montreuil": "48° 51′ 00″ N, 2° 26′ 00″ E",
    "dole": "47° 05′ 00″ N, 5° 29′ 00″ E",
    "subiaco": "31° 57′ 00″ S, 115° 48′ 00″ E",
    "belo": "7° 13′ 00″ S, 35° 53′ 00″ W",
    "aylmer (quebec)": "45° 23′ 00″ N, 75° 51′ 00″ W",
    "philadelphie": "39° 57′ 00″ N, 75° 10′ 00″ W",
    "ordrup": "55° 48′ 00″ N, 12° 34′ 00″ E",
    "christiania": "59° 55′ 00″ N, 10° 45′ 00″ E",
    "seoul": "37° 33′ 00″ N, 126° 59′ 00″ E",
    "charlotte": "35° 13′ 38″ N, 80° 50′ 35″ W",
    "cambridge": "52° 12′ 18″ N, 0° 07′ 08″ E",
    "hove": "50° 50′ 00″ N, 0° 10′ 00″ W",
    "chandigarh": "30° 44′ 00″ N, 76° 47′ 00″ E",
    "spa": "50° 29′ 00″ N, 5° 52′ 00″ E",
    "victoria": "48° 25′ 43″ N, 123° 21′ 56″ W",
    "clerkenwell": "51° 31′ 00″ N, 0° 06′ 00″ W",
    "buffalo": "42° 53′ 00″ N, 78° 52′ 00″ W",
    "arlington": "38° 52′ 00″ N, 77° 06′ 00″ W",
    "takapuna": "36° 47′ 00″ S, 174° 46′ 00″ E",
    "westminster": "51° 30′ 50″ N, 0° 07′ 39″ W",
    "kungsholm": "59° 19′ 00″ N, 18° 02′ 00″ E",
    "cassel": "50° 48′ 00″ N, 2° 29′ 00″ E",
    "detroit (michigan)": "42° 19′ 53″ N, 83° 02′ 45″ W",
    "trebizonde": "41° 00′ 00″ N, 39° 43′ 00″ E",
    "camden": "51° 32′ 00″ N, 0° 08′ 00″ W",
    "siegen": "50° 52′ 00″ N, 8° 01′ 00″ E",
    "cordoba": "37° 53′ 00″ N, 4° 46′ 00″ W",
    "hamilton": "43° 15′ 00″ N, 79° 52′ 00″ W",
    "saint-omer (pas-de-calais)": "50° 45′ 00″ N, 2° 15′ 00″ E",
    "falmouth": "50° 09′ 00″ N, 5° 04′ 00″ W",
    "buda": "47° 28′ 00″ N, 19° 03′ 00″ E",
    "newham": "51° 31′ 00″ N, 0° 01′ 00″ E",
    "rochester": "51° 23′ 00″ N, 0° 30′ 00″ E",
    "san pedro": "33° 44′ 00″ N, 118° 17′ 00″ W",
    "larissa": "39° 38′ 00″ N, 22° 25′ 00″ E",
}

WIKIJOB_TO_JOB_DICT_MAN = {
    "bande dessinée":"Scénariste de bande dessinée",
    "natation":"Nageur",
    "judo":"Judoka",
    "roman":"Romancier",
    "histoire de l'art:":"Historien de l’art",
    "hockey sur gazon":"Joueur de hockey sur gazon",
    "exploration":"Explorateur",
    "haute fonction publique":"Haut fonctionnaire",
    "lutte":"Lutteur",
    "ski alpin":"Skieur alpin",
    "fief":"Feudataire",
    "ski de fond":"	Skieur de fond",
    "femmes et salons litteraires en france":"Salonnière",
    "gravure":"Graveur",
    "pop":"chanteur",
    "banque": "Banquier",
    "major général": "Major général",
    "jazz": "Musicien de jazz",
    "bobeur": "Bobeur",
    "rugby à xv": "Joueur de rugby à XV",
    "schlager": "Chanteur de schlager",
    "mannequinat": "Mannequin",
    "water-polo": "Joueur de water-polo",
    "taekwondo": "Taekwondoïste",
    "syndicalisme": "Syndicaliste",
    "saut à ski": "Sauteur à ski",
    "traduction": "Traducteur",
    "pair": "Pair",
    "université": "Universitaire",
    "tir sportif": "Tireur sportif",
    "pédagogie": "Pédagogue",
    "industrie": "Industriel",
    "rameur d'": "Rameur",
    "canoë": "Céiste",
    "cricket": "Joueur de cricket",
    "arts visuels": "Artiste visuel",
    "nautisme (voile)": "Navigateur",
    "escrime": "Escrimeur",
    "chanoine": "Chanoine",
    "course à pied": "Coureur",
    "handball": "Handballeur",
    "musicologie": "Musicologue",
    "féminisme": "Féministe",
    "patinage de vitesse": "Patineur de vitesse",
    "chorégraphie": "Chorégraphe",
    "canoë-kayak": "Céiste",
    "art contemporain": "Artiste contemporain",
    "knesset": "Député de la Knesset",
    "golf": "Golfeur",
    "tir à l'arc": "Archer",
    "graveur sur cuivre": "Graveur sur cuivre",
    "ornithologie": "Ornithologue",
    "rap": "Rappeur",
    "plongeon": "Plongeur",
    "snowboard": "Snowboardeur",
    "alpinisme": "Alpiniste",
    "roman (littérature)":"Romancier",
    "Roman (littérature)":"Romancière"
}

WIKIJOB_TO_JOB_DICT_WOMAN = {
    "Bande dessinée": "Scénariste de bande dessinée",
    "Natation": "Nageuse",
    "Judo": "Judokate",
    "Roman": "Romancière",
    "Histoire de l'art": "Historienne de l’art",
    "hockey sur gazon": "Joueuse de hockey sur gazon",
    "exploration": "Exploratrice",
    "haute fonction publique": "Haute fonctionnaire",
    "lutte": "Lutteuse",
    "ski alpin": "Skieuse alpine",
    "fief": "Feudataire",
    "ski de fond": "Skieuse de fond",
    "gravure": "Graveuse",
    "pop": "Chanteuse",
    "banque": "Banquière",
    "major général": "Major générale",
    "jazz": "Musicienne de jazz",
    "bobeur": "Bobeuse",
    "rugby à xv": "Joueuse de rugby à XV",
    "schlager": "Chanteuse de schlager",
    "mannequinat": "Mannequin",
    "water-polo": "Joueuse de water-polo",
    "taekwondo": "Taekwondoïste",
    "syndicalisme": "Syndicaliste",
    "saut à ski": "Sauteuse à ski",
    "traduction": "Traductrice",
    "pair": "Paire",
    "université": "Universitaire",
    "tir sportif": "Tireuse sportive",
    "pédagogie": "Pédagogue",
    "industrie": "Industrielle",
    "rameur d'": "Rameuse",
    "canoë": "Céiste",
    "cricket": "Joueuse de cricket",
    "arts visuels": "Artiste visuelle",
    "nautisme (voile)": "Navigatrice",
    "escrime": "Escrimeuse",
    "chanoine": "Chanoinesse",
    "course à pied": "Coureuse",
    "handball": "Handballeuse",
    "musicologie": "Musicologue",
    "féminisme": "Féministe",
    "patinage de vitesse": "Patineuse de vitesse",
    "chorégraphie": "Chorégraphe",
    "canoë-kayak": "Céiste",
    "art contemporain": "Artiste contemporaine",
    "knesset": "Députée de la Knesset",
    "golf": "Golfeuse",
    "tir à l'arc": "Archère",
    "graveur sur cuivre": "Graveuse sur cuivre",
    "ornithologie": "Ornithologue",
    "rap": "Rappeuse",
    "plongeon": "Plongeuse",
    "snowboard": "Snowboardeuse",
    "alpinisme": "Alpiniste",
    "roman (littérature)":"Romancière"
}


NON_COUNTRY_ELEMENTS = [
    "premier",
    "pilote automobile",
    "2011 11 26",
    "lee jae myung",
    "mètre",
    "hangeul",
    "coréen",
    "mouvement national congolais lumumba",
    "baviere",
    "bristol (royaume uni)",
    "kinshasa",
    "cook",
    "man ile",
    "roman empire",
    "congo kinshasa",
    "congo brazzaville",
]

COUNTRY_NORMALIZATION_DICT = {
    "états  unis": "états unis",
    "royaume  uni": "royaume uni",
    "pays  bas": "pays bas",
    "nouvelle  zélande": "nouvelle zélande",
    "cap  vert": "cap vert",
    "république  démocratique  du  congo": "république démocratique du congo",
    "congo kinshasa": "république démocratique du congo",
    "kinshasa": "république démocratique du congo",
    "congo brazzaville": "république du congo",
    "saint  marin": "saint marin",
    "grece": "grèce",
    "haiti": "haïti",
    "nepal": "népal",
    "perou": "pérou",
    "sainte  lucie": "sainte lucie",
    "vietnam": "viêt nam",
    "tchéquie": "république tchèque",
    "guinée  bissau": "guinée-bissau",
    "antigua  et  barbuda": "antigua et barbuda",
    "papouasie  nouvelle  guinée": "papouasie nouvelle guinée",
    "salomon": "îles salomon",
    "trinite et tobago": "trinité et tobago",
    "trinité  et  tobago": "trinité et tobago",
    "dominicaine république": "république dominicaine",
    "bosnie herzégovine": "bosnie-herzégovine",
    "côte divoire": "côte d'ivoire",
    "centrafricaine république": "république centrafricaine",
    "man ile": "île de man",
    "bielorussie": "biélorussie",
    "azerbaidjan": "azerbaïdjan",
    "montenegro": "monténégro",
    "burkina  faso": "burkina faso",
    "indonesie": "indonésie",
    "norvege": "norvège",
    "guinee": "guinée",
    "abkhazie":"géorgie"
}

country_to_flag_dict = {
    "abkhazie": "🏳️",
    "afghanistan": "🇦🇫",
    "afrique du sud": "🇿🇦",
    "albanie": "🇦🇱",
    "algérie": "🇩🇿",
    "allemagne": "🇩🇪",
    "andorre": "🇦🇩",
    "angola": "🇦🇴",
    "antigua et barbuda": "🇦🇬",
    "arabie saoudite": "🇸🇦",
    "argentine": "🇦🇷",
    "arménie": "🇦🇲",
    "australie": "🇦🇺",
    "autriche": "🇦🇹",
    "azerbaïdjan": "🇦🇿",
    "bahamas": "🇧🇸",
    "bahreïn": "🇧🇭",
    "bangladesh": "🇧🇩",
    "barbade": "🇧🇧",
    "belgique": "🇧🇪",
    "belize": "🇧🇿",
    "bénin": "🇧🇯",
    "bhoutan": "🇧🇹",
    "biélorussie": "🇧🇾",
    "birmanie": "🇲🇲",
    "bolivie": "🇧🇴",
    "bosnie herzégovine": "🇧🇦",
    "botswana": "🇧🇼",
    "brésil": "🇧🇷",
    "brunei": "🇧🇳",
    "bulgarie": "🇧🇬",
    "burkina faso": "🇧🇫",
    "burundi": "🇧🇮",
    "cambodge": "🇰🇭",
    "cameroun": "🇨🇲",
    "canada": "🇨🇦",
    "cap vert": "🇨🇻",
    "république centrafricaine": "🇨🇫",
    "chili": "🇨🇱",
    "chine": "🇨🇳",
    "chypre": "🇨🇾",
    "chypre du nord": "🏳️",
    "colombie": "🇨🇴",
    "comores": "🇰🇲",
    "république du congo": "🇨🇬",
    "république démocratique du congo": "🇨🇩",
    "îles cook": "🇨🇰",
    "corée du nord": "🇰🇵",
    "corée du sud": "🇰🇷",
    "costa rica": "🇨🇷",
    "côte d'ivoire": "🇨🇮",
    "croatie": "🇭🇷",
    "cuba": "🇨🇺",
    "danemark": "🇩🇰",
    "djibouti": "🇩🇯",
    "république dominicaine": "🇩🇴",
    "dominique": "🇩🇲",
    "égypte": "🇪🇬",
    "émirats arabes unis": "🇦🇪",
    "équateur": "🇪🇨",
    "érythrée": "🇪🇷",
    "espagne": "🇪🇸",
    "estonie": "🇪🇪",
    "eswatini": "🇸🇿",
    "états unis": "🇺🇸",
    "éthiopie": "🇪🇹",
    "fidji": "🇫🇯",
    "finlande": "🇫🇮",
    "france": "🇫🇷",
    "gabon": "🇬🇦",
    "gambie": "🇬🇲",
    "géorgie": "🇬🇪",
    "ghana": "🇬🇭",
    "grèce": "🇬🇷",
    "grenade": "🇬🇩",
    "guatemala": "🇬🇹",
    "guinée": "🇬🇳",
    "guinée bissau": "🇬🇼",
    "guinée équatoriale": "🇬🇶",
    "guyana": "🇬🇾",
    "haïti": "🇭🇹",
    "honduras": "🇭🇳",
    "hongrie": "🇭🇺",
    "inde": "🇮🇳",
    "indonésie": "🇮🇩",
    "irak": "🇮🇶",
    "iran": "🇮🇷",
    "irlande": "🇮🇪",
    "islande": "🇮🇸",
    "israël": "🇮🇱",
    "italie": "🇮🇹",
    "jamaïque": "🇯🇲",
    "japon": "🇯🇵",
    "jordanie": "🇯🇴",
    "kazakhstan": "🇰🇿",
    "kenya": "🇰🇪",
    "kirghizistan": "🇰🇬",
    "kiribati": "🇰🇮",
    "kosovo": "🇽🇰",
    "koweït": "🇰🇼",
    "laos": "🇱🇦",
    "lesotho": "🇱🇸",
    "lettonie": "🇱🇻",
    "liban": "🇱🇧",
    "liberia": "🇱🇷",
    "libye": "🇱🇾",
    "liechtenstein": "🇱🇮",
    "lituanie": "🇱🇹",
    "luxembourg": "🇱🇺",
    "macédoine du nord": "🇲🇰",
    "madagascar": "🇲🇬",
    "malaisie": "🇲🇾",
    "malawi": "🇲🇼",
    "maldives": "🇲🇻",
    "mali": "🇲🇱",
    "malte": "🇲🇹",
    "maroc": "🇲🇦",
    "îles marshall": "🇲🇭",
    "maurice": "🇲🇺",
    "mauritanie": "🇲🇷",
    "mexique": "🇲🇽",
    "micronésie": "🇫🇲",
    "moldavie": "🇲🇩",
    "monaco": "🇲🇨",
    "mongolie": "🇲🇳",
    "monténégro": "🇲🇪",
    "mozambique": "🇲🇿",
    "namibie": "🇳🇦",
    "nauru": "🇳🇷",
    "népal": "🇳🇵",
    "nicaragua": "🇳🇮",
    "niger": "🇳🇪",
    "nigeria": "🇳🇬",
    "niue": "🇳🇺",
    "norvège": "🇳🇴",
    "nouvelle zélande": "🇳🇿",
    "oman": "🇴🇲",
    "ossétie du sud alanie": "🏳️",
    "ouganda": "🇺🇬",
    "ouzbékistan": "🇺🇿",
    "pakistan": "🇵🇰",
    "palaos": "🇵🇼",
    "palestine": "🇵🇸",
    "panama": "🇵🇦",
    "papouasie nouvelle guinée": "🇵🇬",
    "paraguay": "🇵🇾",
    "pays bas": "🇳🇱",
    "pérou": "🇵🇪",
    "philippines": "🇵🇭",
    "pologne": "🇵🇱",
    "portugal": "🇵🇹",
    "qatar": "🇶🇦",
    "roumanie": "🇷🇴",
    "royaume uni": "🇬🇧",
    "russie": "🇷🇺",
    "rwanda": "🇷🇼",
    "sénégal": "🇸🇳",
    "serbie": "🇷🇸",
    "singapour": "🇸🇬",
    "slovaquie": "🇸🇰",
    "slovénie": "🇸🇮",
    "somalie": "🇸🇴",
    "soudan": "🇸🇩",
    "soudan du sud": "🇸🇸",
    "suède": "🇸🇪",
    "suisse": "🇨🇭",
    "syrie": "🇸🇾",
    "taïwan": "🇹🇼",
    "tanzanie": "🇹🇿",
    "tchad": "🇹🇩",
    "république tchèque": "🇨🇿",
    "thaïlande": "🇹🇭",
    "turquie": "🇹🇷",
    "ukraine": "🇺🇦",
    "uruguay": "🇺🇾",
    "vietnam": "🇻🇳",
    "zambie": "🇿🇲",
    "zimbabwe": "🇿🇼",
}


LIST_OF_WEIRD_JOB = [
    "un joueur de d'état",
    "une joueuse de d'état",

    "un joueur de d'église",
    "une joueuse de d'église",

    "un joueur de d'armée",
    "Une joueuse de d'armée",

    "un joueur de d'empire",
    "une joueuse de d'empire",

    "un joueur de d'affaires",
    "une joueuse de d'affaires",
]

WEIRD_JOB_REPLACEMENTS = {
    "un joueur de d'état": "Un homme d'État",
    "une joueuse de d'état": "Une femme d'État",

    "un joueur de d'église": "Un homme d'Église",
    "une joueuse de d'église": "Une femme d'Église",

    "un joueur de d'armée": "Un militaire",
    "une joueuse de d'armée": "Une militaire",

    "un joueur de d'empire": "Un homme d'Empire",
    "une joueuse de d'empire": "Une femme d'Empire",

    "un joueur de d'affaires": "Un homme d'affaires",
    "une joueuse de d'affaires": "Une femme d'affaires",
}


DICT_OF_LOCALISATION_TO_COUNTRY = {
 '48° 51′ 24′′ n, 2° 21′ 07′′ e': 'France',
 '51° 30′ 26′′ n, 0° 07′ 39′′ w': 'Royaume-Uni',
 '40° 42′ 46′′ n, 74° 00′ 22′′ w': 'États-Unis',
 '41° 53′ 19′′ n, 12° 29′ 12′′ e': 'Italie',
 '52° 31′ n, 13° 23′ e': 'Allemagne',
 '45° 30′ 12′′ n, 73° 35′ 13′′ w': 'Canada',
 '48° 12′ 30′′ n, 16° 22′ 21′′ e': 'Autriche',
 '55° 45′ 09′′ n, 37° 37′ 23,11′′ e': 'Russie',
 '43° 17′ 47′′ n, 5° 22′ 12′′ e': 'France',
 '50° 38′ 14′′ n, 3° 03′ 48′′ e': 'France',
 '50° 51′ 01′′ n, 4° 21′ 00′′ e': 'Belgique',
 '41° 52′ 55′′ n, 87° 37′ 40′′ w': 'États-Unis',
 '34° 03′ n, 118° 15′ w': 'États-Unis',
 '40° 26′ 00′′ n, 3° 41′ 00′′ w': 'Espagne',
 '45° 45′ 28′′ n, 4° 49′ 56′′ e': 'France',
 '35° 41′ 22′′ n, 139° 41′ 30′′ e': 'Japon',
 '59° 56′ 02′′ n, 30° 18′ 22′′ e': 'Russie',
 '47° 29′ 54′′ n, 19° 02′ 27′′ e': 'Hongrie',
 '45° 28′ 00′′ n, 9° 10′ 00′′ e': 'Italie',
 '41° 22′ 57′′ n, 2° 10′ 37′′ e': 'Espagne',
 '40° 39′ 03′′ n, 73° 56′ 59′′ w': 'États-Unis',
 '44° 50′ 16′′ n, 0° 34′ 46′′ w': 'France',
 '43° 36′ 16′′ n, 1° 26′ 38′′ e': 'France',
 '34° 36′ 29′′ s, 58° 22′ 13′′ w': 'Argentine',
 '39° 57′ 10′′ n, 75° 09′ 49′′ w': 'États-Unis',
 '52° 22′ n, 4° 53′ e': 'Pays-Bas',
 '51° 13′ n, 4° 24′ e': 'Belgique',
 '43° 46′ 18′′ n, 11° 15′ 13′′ e': 'Italie',
 '48° 34′ 24′′ n, 7° 45′ 08′′ e': 'France',
 '46° 12′ 00′′ n, 6° 09′ 00′′ e': 'Suisse',
 '40° 50′ 00′′ n, 14° 15′ 00′′ e': 'Italie',
 '47° 13′ 05′′ n, 1° 33′ 10′′ w': 'France',
 '52° 13′ 56′′ n, 21° 00′ 30′′ e': 'Pologne',
 '50° 05′ 16′′ n, 14° 25′ 14′′ e': 'République tchèque',
 '48° 09′ 00′′ n, 11° 34′ 30′′ e': 'Allemagne',
 "40° 45′ 36′′ N, 22° 31′ 32′′ E": 'Grèce',
 '55° 41′ 24′′ n, 12° 35′ 09,6′′ e': 'Danemark',
 '43° 40′ 13′′ n, 79° 23′ 12′′ w': 'Canada',
 '53° 20′ 36′′ n, 6° 16′ 03′′ w': 'Irlande',
 '36° 47′ 51′′ n, 10° 09′ 57′′ e': 'Tunisie',
 '50° 38′ 23′′ n, 5° 34′ 14′′ e': 'Belgique',
 '36° 46′ 34′′ n, 3° 03′ 36′′ e': 'Algérie',
 '42° 21′ 37′′ n, 71° 03′ 28′′ w': 'États-Unis',
 '53° 33′ n, 10° 00′ e': 'Allemagne',
 '48° 53′ 17′′ n, 2° 16′ 07′′ e': 'France',
 '59° 19′ 46′′ n, 18° 04′ 07′′ e': 'Suède',
 '49° 26′ 36′′ n, 1° 06′ 00′′ e': 'France',
 '33° 51′ 22′′ s, 151° 11′ 33′′ e': 'Australie',
 '22° 54′ 35′′ s, 43° 10′ 35′′ w': 'Brésil',
 '45° 04′ 00′′ n, 7° 42′ 00′′ e': 'Italie',
 '19° 21′ 14′′ n, 99° 08′ 09′′ w': 'Mexique',
 '43° 41′ 45′′ n, 7° 16′ 17′′ e': 'France',
 '43° 09′ 57.30′′ n, 4° 02′ 49.41′′ w': 'Espagne',
 '33° 26′ 16′′ s, 70° 39′ 02′′ w': 'Chili',
 '38° 53′ 42′′ n, 77° 02′ 12′′ w': 'États-Unis',
 '48° 49′ 59′′ n, 2° 19′ 36′′ e': 'France',
 '43° 36′ 43′′ n, 3° 52′ 38′′ e': 'France',
 '38° 43′ n, 9° 08′ w': 'Portugal',
 '48° 41′ 37′′ n, 6° 11′ 05′′ e': 'France',
 '49° 07′ 13′′ n, 6° 10′ 40′′ e': 'France',
 '48° 06′ 53′′ n, 1° 40′ 46′′ w': 'France',
 '37° 33′ 57′′ n, 126° 58′ 41′′ e': 'Corée du Sud',
 '45° 26′ 23′′ n, 12° 19′ 55′′ e': 'Italie',
 '55° 51′ 29′′ n, 4° 15′ 32′′ w': 'Royaume-Uni',
 '33° 34′ 42,44′′ n, 7° 36′ 23,89′′ w': 'Maroc',
 '51° 03′ n, 3° 44′ e': 'Belgique',
 '48° 51′ 46′′ n, 2° 16′ 34′′ e': 'France',
 '34° 53′ 00′′ s, 56° 10′ 00′′ w': 'Uruguay',
 '44° 24′ 48′′ n, 26° 05′ 52′′ e': 'Roumanie',
 '48° 50′ 07′′ n, 2° 14′ 27′′ e': 'France',
 '37° 46′ 30′′ n, 122° 25′ 10′′ w': 'États-Unis',
 '46° 48′ 58′′ n, 71° 13′ 27′′ w': 'Canada',
 '48° 48′ 19′′ n, 2° 08′ 06′′ e': 'France',
 '44° 30′ 00′′ n, 11° 21′ 00′′ e': 'Italie',
 '46° 31′ 16′′ n, 6° 37′ 52′′ e': 'Suisse',
 '44° 24′ 24′′ n, 8° 56′ 00′′ e': 'Italie',
 '47° 22′ 40′′ n, 8° 32′ 28′′ e': 'Suisse',
 '37° 48′ 51′′ s, 144° 58′ 06′′ e': 'Australie',
 '48° 52′ 19′′ n, 2° 21′ 27′′ e': 'France',
 '23° 32′ 52′′ s, 46° 38′ 11′′ w': 'Brésil',
 '55° 57′ 17′′ n, 3° 12′ 06′′ w': 'Royaume-Uni',
 '37° 58′ 00′′ n, 23° 43′ 00′′ e': 'Grèce',
 '60° 10′ 15′′ n, 24° 56′ 15′′ e': 'Finlande',
 '59° 54′ 48′′ n, 10° 44′ 20′′ e': 'Norvège',
 '47° 19′ 18′′ n, 5° 02′ 29′′ e': 'France',
 '42° 19′ 54′′ n, 83° 02′ 51′′ w': 'États-Unis',
 '45° 11′ 16′′ n, 5° 43′ 37′′ e': 'France',
 '50° 07′ 01′′ n, 8° 40′ 59′′ e': 'Allemagne',
 '12° 02′ 43′′ s, 77° 01′ 52′′ w': 'Pérou',
 '49° 15′ 46′′ n, 4° 02′ 05′′ e': 'France',
 '35° 40′ 51′′ n, 51° 24′ 50′′ e': 'Iran',
 '30° 02′ 40′′ n, 31° 14′ 44′′ e': 'Égypte',
 '39° 28′ 13′′ n, 0° 22′ 36′′ w': 'Espagne',
 '50° 27′ 13′′ n, 30° 30′ 59′′ e': 'Ukraine',
 '44° 49′ n, 20° 28′ e': 'Serbie',
 '43° 07′ 20′′ n, 5° 55′ 48′′ e': 'France',
 '52° 28′ 59′′ n, 1° 53′ 37′′ w': 'Royaume-Uni',
 '47° 14′ 35′′ n, 6° 01′ 19′′ e': 'France',
 '48° 53′ 04′′ n, 2° 19′ 19′′ e': 'France',
 '4° 18′ 23′′ s, 15° 18′ 31′′ e': 'République démocratique du Congo',
 '14° 43′ 55′′ n, 17° 27′ 26′′ w': 'Sénégal',
 '41° 43′ 01′′ n, 44° 46′ 59′′ e': 'Géorgie',
 '38° 38′ 53′′ n, 90° 12′ 44′′ w': 'États-Unis',
 '53° 24′ 33′′ n, 2° 59′ 09′′ w': 'Royaume-Uni',
 '47° 23′ 37′′ n, 0° 41′ 21′′ e': 'France',
 '48° 23′ 27′′ n, 4° 29′ 08′′ w': 'France',
 '40° 23′ 43′′ n, 49° 52′ 56′′ e': 'Azerbaïdjan',
 '41° 00′ 44′′ n, 28° 58′ 34′′ e': 'Turquie',
 '50° 56′ 33′′ n, 6° 57′ 32′′ e': 'Allemagne',
 '43° 50′ 16′′ n, 4° 21′ 39′′ e': 'France',
 '53° n, 1° w': 'Royaume-Uni',
 '43° 57′ 00′′ n, 4° 49′ 01′′ e': 'France',
 '51° 03′ 00′′ n, 13° 44′ 00′′ e': 'Allemagne',
 '47° 28′ 25′′ n, 0° 33′ 15′′ w': 'France',
 '47° 54′ 09′′ n, 1° 54′ 32′′ e': 'France',
 '51° 20′ 25′′ n, 12° 22′ 29′′ e': 'Allemagne',
 '49° 15′ 39′′ n, 123° 06′ 50′′ w': 'Canada',
 '39° 17′ 11′′ n, 76° 36′ 54′′ w': 'États-Unis',
 '38° 07′ 00′′ n, 13° 22′ 00′′ e': 'Italie',
 '45° 46′ 33′′ n, 3° 04′ 56′′ e': 'France',
 '41° 00′ 45′′ n, 28° 58′ 48′′ e': 'Turquie',
 '51° 55′ 00′′ n, 4° 29′ 00′′ e': 'Pays-Bas',
 '56° 56′ 56′′ n, 24° 06′ 23′′ e': 'Lettonie',
 '52° 05′ n, 4° 19′ e': 'Pays-Bas',
 '35° 42′ 10′′ n, 0° 38′ 57′′ w': 'Algérie',
 '45° 26′ 05′′ n, 4° 23′ 25′′ e': 'France',
 '41° 29′ 57′′ n, 81° 41′ 41′′ w': 'États-Unis',
 '48° 50′ 29′′ n, 2° 18′ 01′′ e': 'France',
 '48° 52′ 40′′ n, 2° 19′ 04′′ e': 'France',
 '49° 10′ 56′′ n, 0° 22′ 14′′ w': 'France',
 '53° 29′ 00′′ n, 2° 15′ 00′′ w': 'Royaume-Uni',
 '31° 11′ 53′′ n, 29° 55′ 09′′ e': 'Égypte',
 '48° 46′ 36′′ n, 9° 10′ 40′′ e': 'Allemagne',
 '48° 52′ 21′′ n, 2° 20′ 25′′ e': 'France',
 '48° 52′ 22′′ n, 2° 20′ 26′′ e': 'France',
 '47° 34′ 01′′ n, 7° 34′ 59′′ e': 'Suisse',
 '49° 53′ 39′′ n, 2° 17′ 45′′ e': 'France',
 '29° 45′ 46′′ n, 95° 22′ 59′′ w': 'États-Unis',
 '50° 04′ n, 19° 57′ e': 'Pologne',
 '43° 31′ 52′′ n, 5° 27′ 14′′ e': 'France',
 '48° 51′ 02′′ n, 2° 19′ 58′′ e': 'France',
 '47° 44′ 58′′ n, 7° 20′ 24′′ e': 'France',
 '48° 50′ 28′′ n, 2° 23′ 17′′ e': 'France',
 '40° 26′ 30′′ n, 80° 00′ 00′′ w': 'États-Unis',
 '51° 07′ 00′′ n, 17° 02′ 00′′ e': 'Pologne',
 '42° 41′ 55′′ n, 2° 53′ 44′′ e': 'France',
 '45° 51′ 00′′ n, 1° 15′ 00′′ e': 'France',
 '40° 50′ 14′′ n, 73° 53′ 10′′ w': 'États-Unis',
 '36° 51′ 00′′ s, 174° 47′ 00′′ e': 'Nouvelle-Zélande',
 '51° 12′ n, 3° 13′ e': 'Belgique',
 '42° 41′ 50′′ n, 23° 19′ 00′′ e': 'Bulgarie',
 '43° 29′ 37′′ n, 1° 28′ 30′′ w': 'France',
 '40° 43′ 42′′ n, 73° 59′ 39′′ w': 'États-Unis',
 '45° 48′ 47′′ n, 15° 58′ 38′′ e': 'Croatie',
 '23° 08′ 20′′ n, 82° 21′ 26′′ w': 'Cuba',
 '29° 58′ 34′′ n, 90° 04′ 42′′ w': 'États-Unis',
 '41° 08′ 58′′ n, 8° 36′ 39′′ w': 'Portugal',
 '46° 56′ 57′′ n, 7° 26′ 50′′ e': 'Suisse',
 '51° 13′ 32′′ n, 6° 46′ 58′′ e': 'Allemagne',
 '5° 20′ 11′′ n, 4° 01′ 36′′ w': "Côte d'Ivoire",
 '48° 51′ 10′′ n, 2° 19′ 46′′ e': 'France',
 '48° 52′ 01′′ n, 2° 20′ 26′′ e': 'France',
 '48° 52′ 12′′ n, 2° 19′ 15′′ e': 'France',
 '33° 45′ 16′′ n, 84° 23′ 23′′ w': 'États-Unis',
 '54° 35′ 46′′ n, 5° 54′ 50′′ w': 'Royaume-Uni',
 '49° 29′ 24′′ n, 0° 06′ 00′′ e': 'France',
 '43° 18′ 06′′ n, 0° 22′ 07′′ w': 'France',
 '50° 49′ 58′′ n, 4° 22′ 03′′ e': 'Belgique',
 '52° 22′ 28′′ n, 9° 44′ 19′′ e': 'Allemagne',
 '48° 56′ 08′′ n, 2° 21′ 14′′ e': 'France',
 '59° 26′ 00′′ n, 24° 43′ 50′′ e': 'Estonie',
 '33° 53′ 23′′ n, 35° 30′ 01′′ e': 'Liban',
 '3° 52′ n, 11° 31′ e': 'Cameroun',
 '57° 42′ 00′′ n, 11° 56′ 00′′ e': 'Suède',
 '46° 28′ n, 30° 44′ e': 'Ukraine',
 '48° 51′ 30′′ n, 2° 22′ 47′′ e': 'France',
 '48° 53′ 32′′ n, 2° 20′ 40′′ e': 'France',
 '52° 12′ 29′′ n, 0° 07′ 21′′ e': 'Royaume-Uni',
 '26° 12′ 16′′ s, 28° 02′ 44′′ e': 'Afrique du Sud',
 '47° 36′ 18′′ n, 122° 19′ 48′′ w': 'États-Unis',
 '32° 46′ 45′′ n, 96° 48′ 32′′ w': 'États-Unis',
 '39° 06′ 00′′ n, 84° 30′ 45′′ w': 'États-Unis',
 '34° 01′ 16′′ n, 6° 50′ 29′′ w': 'Maroc',
 '46° 34′ 55′′ n, 0° 20′ 10′′ e': 'France',
 '37° 23′ 00′′ n, 5° 59′ 48′′ w': 'Espagne',
 '34° 41′ 37′′ n, 135° 30′ 07′′ e': 'Japon',
 '45° 25′ 29′′ n, 75° 41′ 42′′ w': 'Canada',
 '48° 51′ 25′′ n, 2° 19′ 12′′ e': 'France',
 '50° 48′ n, 4° 20′ e': 'Belgique',
 '4° 36′ 36′′ n, 74° 04′ 55′′ w': 'Colombie',
 '48° 00′ 15′′ n, 0° 11′ 49′′ e': 'France',
 '50° 28′ n, 4° 52′ e': 'Belgique',
 '4° 03′ n, 9° 42′ e': 'Cameroun',
 '6° 27′ 06′′ n, 3° 23′ 21′′ e': 'Nigeria',
 '10° 29′ 28′′ n, 66° 54′ 07′′ w': 'Venezuela',
 '50° 41′ 24′′ n, 3° 10′ 54′′ e': 'Belgique',
 '50° 53′ n, 4° 42′ e': 'Belgique',
 '18° 55′ 55′′ n, 72° 50′ 10′′ e': 'Inde',
 '49° 51′ n, 24° 01′ e': 'Ukraine',
 '53° 55′ 45′′ n, 27° 29′ 46′′ e': 'Biélorussie',
 '31° 13′ 56′′ n, 121° 28′ 09′′ e': 'Chine',
 '45° 34′ 12′′ n, 5° 54′ 42′′ e': 'France',
 '52° 05′ 00′′ n, 5° 06′ 00′′ e': 'Pays-Bas',
 '49° 27′ 00′′ n, 11° 05′ 00′′ e': 'Allemagne',
 '48° 17′ 51′′ n, 4° 04′ 27′′ e': 'France',
 '27° 28′ 00′′ s, 153° 02′ 00′′ e': 'Australie',
 '48° 51′ 02′′ n, 2° 19′ 57′′ e': 'France',
 '50° 21′ 29′′ n, 3° 31′ 24′′ e': 'Belgique',
 '44° 58′ 55′′ n, 93° 16′ 09′′ w': 'États-Unis',
 '18° 32′ 24′′ n, 72° 20′ 24′′ w': 'Haïti',
 '31° 47′ 00′′ n, 35° 13′ 00′′ e': 'Palestine',
 '35° 01′ n, 135° 46′ e': 'Japon',
 '39° 54′ 13′′ n, 116° 23′ 15′′ e': 'Chine',
 '17° 59′ n, 76° 48′ w': 'Jamaïque',
 '54° 44′ n, 20° 29′ e': 'Russie',
 '12° 38′ 00′′ n, 7° 59′ 00′′ w': 'Mali',
 '32° 42′ 54′′ n, 117° 09′ 45′′ w': 'États-Unis',
 '49° 59′ 33′′ n, 36° 13′ 52′′ e': 'Ukraine',
 '43° 20′ 51′′ n, 3° 13′ 08′′ e': 'France',
 '25° 47′ n, 80° 13′ w': 'États-Unis',
 '33° 55′ 31′′ s, 18° 25′ 26′′ e': 'Afrique du Sud',
 '54° 41′ n, 25° 16′ e': 'Lituanie',
 '54° 58′ 00′′ n, 1° 36′ 00′′ w': 'Royaume-Uni',
 '5° 33′ 29′′ n, 0° 12′ 04′′ w': 'Ghana',
 '46° 03′ 05,13′′ n, 14° 30′ 21,47′′ e': 'Slovénie',
 '51° 45′ 07′′ n, 1° 15′ 28′′ w': 'Royaume-Uni',
 '39° 44′ 21′′ n, 104° 59′ 05′′ w': 'États-Unis',
 '64° 08′ 51′′ n, 21° 56′ 06′′ w': 'Islande',
 '49° 53′ 44′′ n, 97° 08′ 19′′ w': 'Canada',
 '43° 03′ n, 87° 57′ w': 'États-Unis',
 '37° 48′ n, 122° 15′ w': 'États-Unis',
 '40° 44′ 08′′ n, 74° 10′ 20′′ w': 'États-Unis',
 '47° 04′ 14′′ n, 15° 26′ 17′′ e': 'Autriche',
 '40° 09′ 33′′ n, 44° 30′ 33′′ e': 'Arménie',
 '53° 47′ 59′′ n, 1° 32′ 57′′ w': 'Royaume-Uni',
 '50° 27′ 18′′ n, 3° 57′ 07′′ e': 'Belgique',
 '53° 22′ 01′′ n, 1° 30′ 00′′ w': 'Royaume-Uni',
 '51° 27′ 00′′ n, 2° 34′ 59′′ w': 'Royaume-Uni',
 '46° 59′ 25′′ n, 6° 55′ 50′′ e': 'Suisse',
 '48° 08′ 41′′ n, 17° 06′ 46′′ e': 'Slovaquie',
 '45° 26′ 00′′ n, 10° 59′ 00′′ e': 'Italie',
 '45° 25′ 00′′ n, 11° 52′ 00′′ e': 'Italie',
 '45° 31′ 59′′ n, 10° 13′ 59′′ e': 'Italie',
 '45° 54′ 58′′ n, 6° 07′ 59′′ e': 'France',
 '49° 11′ 31′′ n, 16° 36′ 47′′ e': 'République tchèque',
 '39° 03′ n, 94° 35′ w': 'États-Unis',
 '51° 45′ 00′′ n, 19° 28′ 00′′ e': 'Pologne',
 '50° 25′ 00′′ n, 4° 26′ 39′′ e': 'Belgique',
 '51° 03′ n, 114° 04′ w': 'Canada',
 '48° 04′ 54′′ n, 7° 21′ 20′′ e': 'France',
 '54° 21′ 07′′ n, 18° 38′ 48′′ e': 'Pologne',
 '47° 05′ 04′′ n, 2° 23′ 47′′ e': 'France',
 '47° 45′ n, 3° 22′ w': 'France',
 '45° 39′ n, 13° 46′ e': 'Italie',
 '48° 04′ 22′′ n, 0° 46′ 12′′ w': 'France',
 '50° 36′ n, 3° 23′ e': 'Belgique',
 '42° 53′ 11′′ n, 78° 52′ 41′′ w': 'États-Unis',
 '50° 49′ 43′′ n, 4° 23′ 23′′ e': 'Belgique',
 '48° 38′ 50′′ n, 2° 00′ 32′′ w': 'France',
 '48° 30′ 49′′ n, 2° 45′ 55′′ w': 'France',
 '48° 52′ n, 2° 13′ e': 'France',
 '51° 01′ n, 4° 28′ e': 'Belgique',
 '33° 20′ 00′′ n, 44° 26′ 00′′ e': 'Irak',
 '32° 57′ 04′′ s, 60° 39′ 59′′ w': 'Argentine',
 '41° 39′ 00′′ n, 0° 53′ 00′′ w': 'Espagne',
 '57° 09′ 00′′ n, 2° 07′ 23′′ w': 'Royaume-Uni',
 '53° 32′ 00′′ n, 113° 30′ 00′′ w': 'Canada',
 '22° 17′ n, 114° 10′ e': 'Chine',
 '50° 52′ 03′′ n, 4° 22′ 25′′ e': 'Belgique',
 '32° 02′ 43′′ n, 34° 46′ 11′′ e': 'Israël',
 '48° 27′ 21′′ n, 1° 29′ 03′′ e': 'France',
 '50° 43′ 35′′ n, 1° 36′ 53′′ e': 'Royaume-Uni',
 '43° 33′ 05′′ n, 7° 00′ 46′′ e': 'France',
 '49° 47′ 17′′ n, 9° 56′ 10′′ e': 'Allemagne',
 '52° 22′ 49′′ n, 4° 38′ 26′′ e': 'Pays-Bas',
 '48° 53′ 56′′ n, 2° 05′ 38′′ e': 'France',
 '35° 08′ 46′′ n, 90° 03′ 07′′ w': 'États-Unis',
 '50° 35′ 27′′ n, 5° 51′ 42′′ e': 'Belgique',
 '49° 29′ 20′′ n, 8° 28′ 09′′ e': 'Allemagne',
 '44° 48′ 00′′ n, 10° 20′ 00′′ e': 'Italie',
 '45° 31′ n, 122° 40′ w': 'États-Unis',
 '40° 38′ 00′′ n, 22° 57′ 00′′ e': 'Grèce',
 '48° 49′ 56′′ n, 2° 21′ 20′′ e': 'France',
 '50° 22′ 17′′ n, 3° 04′ 48′′ e': 'Belgique',
 '43° 19′ 17′′ n, 1° 59′ 08′′ w': 'France',
 '35° 26′ n, 139° 38′ e': 'Japon',
 '8° 50′ 18′′ s, 13° 14′ 04′′ e': 'Angola',
 '39° 46′ 07′′ n, 86° 09′ 29′′ w': 'États-Unis',
 '36° 17′ 00′′ n, 6° 37′ 00′′ e': 'Algérie',
 '41° 17′ 55′′ s, 174° 46′ 52′′ e': 'Nouvelle-Zélande',
 '46° 09′ 33′′ n, 1° 09′ 06′′ w': 'France',
 '43° 15′ 25′′ n, 2° 55′ 24′′ w': 'France',
 '40° 42′ 49′′ n, 73° 49′ 41′′ w': 'États-Unis',
 '22° 34′ 22′′ n, 88° 21′ 50′′ e': 'Inde',
 '49° 00′ 50′′ n, 8° 24′ 15′′ e': 'Allemagne',
 '43° 30′ 36′′ n, 16° 26′ 24′′ e': 'Croatie',
 '45° 45′ 15′′ n, 4° 49′ 45′′ e': 'France',
 '52° 08′ 00′′ n, 11° 37′ 00′′ e': 'Allemagne',
 '25° 17′ 39′′ s, 57° 38′ 31′′ w': 'Paraguay',
 '52° 24′ 00′′ n, 16° 55′ 00′′ e': 'Pologne',
 '52° 24′ 00′′ n, 13° 04′ 00′′ e': 'Allemagne',
 '41° 18′ 30′′ n, 69° 15′ 35′′ e': 'Ouzbékistan',
 '43° 12′ 47′′ n, 2° 21′ 07′′ e': 'France',
 '44° 50′ 00′′ n, 11° 37′ 00′′ e': 'Italie',
 '13° 45′ 08′′ n, 100° 29′ 38′′ e': 'Thaïlande',
 '48° 50′ 46′′ n, 2° 20′ 41′′ e': 'France',
 '49° 38′ 20′′ n, 1° 37′ 30′′ w': 'France',
 '34° 03′ 00′′ n, 4° 58′ 59′′ w': 'Maroc',
 '47° 35′ 38′′ n, 1° 19′ 41′′ e': 'France',
 '43° 33′ 00′′ n, 10° 19′ 00′′ e': 'Italie',
 '9° 32′ 53′′ n, 13° 40′ 14′′ w': 'Guinée',
 '52° 57′ 12′′ n, 1° 08′ 51′′ w': 'Royaume-Uni',
 '43° 50′ 51′′ n, 18° 21′ 23′′ e': 'Bosnie-Herzégovine',
 '34° 55′ 48′′ s, 138° 35′ 59′′ e': 'Australie',
 '50° 17′ 23′′ n, 2° 46′ 51′′ e': 'France',
 '48° 51′ 22′′ n, 2° 21′ 20′′ e': 'France',
 '49° 50′ 55′′ n, 3° 17′ 11′′ e': 'France',
 '49° 52′ 00′′ n, 8° 39′ 00′′ e': 'Allemagne',
 '33° 30′ 44′′ n, 36° 17′ 54′′ e': 'Syrie',
 '47° 59′ 48′′ n, 4° 05′ 47′′ w': 'France',
 '51° 29′ 07′′ n, 3° 11′ 12′′ w': 'Royaume-Uni',
 '48° 51′ 57′′ n, 2° 21′ 50′′ e': 'France',
 '44° 12′ 18′′ n, 0° 37′ 16′′ e': 'France',
 '45° 38′ 56′′ n, 0° 09′ 39′′ e': 'France',
 '38° 15′ 22′′ n, 85° 45′ 05′′ w': 'États-Unis',
 '51° 02′ 18′′ n, 2° 22′ 39′′ e': 'Belgique',
 '44° 01′ 05′′ n, 1° 21′ 21′′ e': 'France',
 '53° 04′ 59′′ n, 8° 48′ 00′′ e': 'Allemagne',
 '50° 00′ 00′′ n, 8° 16′ 16′′ e': 'Allemagne',
 '50° 44′ n, 7° 06′ e': 'Allemagne',
 '48° 51′ 54′′ n, 2° 23′ 57′′ e': 'France',
 '49° 24′ 39′′ n, 8° 42′ 07′′ e': 'Allemagne',
 '51° 27′ 00′′ n, 7° 01′ 00′′ e': 'Allemagne',
 '47° 38′ 17′′ n, 6° 51′ 46′′ e': 'France',
 '47° 39′ 21′′ n, 2° 45′ 37′′ w': 'France',
 '42° 42′ 03′′ n, 9° 27′ 01′′ e': 'France',
 '51° 19′ 11′′ n, 9° 29′ 52′′ e': 'Allemagne',
 '60° 22′ 57′′ n, 5° 20′ 41′′ e': 'Norvège',
 '46° 19′ 33′′ n, 0° 27′ 38′′ w': 'France',
 '4° 16′ 04′′ s, 15° 16′ 31′′ e': 'République démocratique du Congo',
 '48° 22′ 08′′ n, 10° 53′ 52′′ e': 'Allemagne',
 '14° 36′ 48′′ n, 61° 03′ 52′′ w': 'Martinique',
 '50° 49′ n, 3° 16′ e': 'Belgique',
 '52° 09′ 00′′ n, 4° 29′ 00′′ e': 'Pays-Bas',
 '45° 42′ 00′′ n, 9° 39′ 58′′ e': 'Italie',
 '46° 59′ 34′′ n, 3° 09′ 42′′ e': 'France',
 '47° 16′ 00′′ n, 11° 23′ 00′′ e': 'Autriche',
 '45° 46′ 18′′ n, 4° 51′ 17′′ e': 'France',
 '43° 20′ 00′′ n, 11° 20′ 00′′ e': 'Italie',
 '52° 38′ 03′′ n, 1° 08′ 19′′ w': 'Royaume-Uni',
 '57° n, 5° w': 'Royaume-Uni',
 '55° 35′ 00′′ n, 13° 02′ 00′′ e': 'Suède',
 '50° 49′ 00′′ n, 1° 05′ 00′′ w': 'Royaume-Uni',
 '53° 25′ n, 14° 35′ e': 'Pologne',
 '40° 45′ 00′′ n, 111° 53′ 00′′ w': 'États-Unis',
 '43° 13′ 51′′ n, 0° 04′ 21′′ e': 'France',
 '29° 53′ 00′′ s, 31° 03′ 00′′ e': 'Afrique du Sud',
 '38° 34′ 31′′ n, 121° 29′ 10′′ w': 'États-Unis',
 '21° 18′ 17′′ n, 157° 51′ 26′′ w': 'États-Unis',
 '48° 10′ 28′′ n, 6° 27′ 04′′ e': 'France',
 '43° 55′ 44′′ n, 2° 08′ 47′′ e': 'France',
 '48° 50′ 46′′ n, 2° 20′ 40′′ e': 'France',
 '43° 24′ 19′′ n, 3° 41′ 51′′ e': 'France',
 '43° 43′ 00′′ n, 10° 24′ 00′′ e': 'Italie',
 '31° 57′ s, 115° 52′ e': 'Australie',
 '43° 09′ 56′′ n, 77° 36′ 58′′ w': 'États-Unis',
 '46° 12′ 20′′ n, 5° 13′ 44′′ e': 'France',
 '47° 00′ 00′′ n, 28° 55′ 00′′ e': 'Moldavie',
 '53° 57′ n, 1° 05′ w': 'Royaume-Uni',
 '43° 31′ 54′′ s, 172° 38′ 12′′ e': 'Nouvelle-Zélande',
 '34° 44′ n, 10° 46′ e': 'Tunisie',
 '52° 37′ 42′′ n, 1° 17′ 48′′ e': 'Royaume-Uni',
 '25° 44′ 42′′ s, 28° 11′ 25′′ e': 'Afrique du Sud',
 '33° 46′ 05′′ n, 118° 11′ 44′′ w': 'États-Unis',
 '6° 10′ 31′′ s, 106° 49′ 37′′ e': 'Indonésie',
 '41° 18′ 30′′ n, 72° 55′ 30′′ w': 'États-Unis',
 '47° 06′ 05′′ n, 6° 49′ 30′′ e': 'France',
 '37° 30′ 58′′ n, 15° 03′ 58′′ e': 'Italie',
 '35° 26′ 52′′ n, 139° 38′ 33′′ e': 'Japon',
 '48° 51′ 37′′ n, 2° 26′ 35′′ e': 'France',
 '45° 11′ 02′′ n, 0° 42′ 57′′ e': 'France',
 '42° 49′ 00′′ n, 1° 39′ 00′′ w': 'France',
 '41° 39′ 07′′ n, 4° 43′ 43′′ w': 'Espagne',
 '41° 55′ 36′′ n, 8° 44′ 13′′ e': 'France',
 '50° 49′ 42′′ n, 0° 08′ 22′′ w': 'Royaume-Uni',
 '48° 51′ 50′′ n, 2° 21′ 42′′ e': 'France',
 '49° 09′ 39′′ n, 5° 23′ 18′′ e': 'France',
 '45° 45′ 31′′ n, 4° 51′ 21′′ e': 'France',
 '49° 25′ 49′′ n, 2° 05′ 43′′ e': 'France',
 '51° 29′ 58′′ n, 0° 08′ 00′′ w': 'Royaume-Uni',
 '48° 57′ 27′′ n, 4° 21′ 54′′ e': 'France',
 '50° 46′ 00′′ n, 6° 06′ 00′′ e': 'Allemagne',
 '39° 57′ 44′′ n, 83° 00′ 02′′ w': 'États-Unis',
 '6° 08′ 14′′ n, 1° 12′ 45′′ e': 'Ghana',
 '43° 11′ 01′′ n, 3° 00′ 15′′ e': 'France',
 '51° 28′ 00′′ n, 11° 58′ 00′′ e': 'Allemagne',
 '50° 56′ 53′′ n, 1° 51′ 23′′ e': 'Royaume-Uni',
 '43° 40′ 36′′ n, 4° 37′ 40′′ e': 'France',
 '51° 53′ 49′′ n, 8° 28′ 41′′ w': 'Irlande',
 '50° 43′ 30′′ n, 3° 09′ 43′′ e': 'Belgique',
 '48° 50′ 32′′ n, 2° 25′ 07′′ e': 'France',
 '49° 11′ 24′′ n, 2° 06′ 36′′ w': 'Royaume-Uni',
 '36° 09′ 44′′ n, 86° 46′ 28′′ w': 'États-Unis',
 '16° 14′ 30′′ n, 61° 32′ 09′′ w': 'Guadeloupe',
 '20° 40′ 35′′ n, 103° 20′ 32′′ w': 'Mexique',
 '50° 10′ 36′′ n, 3° 14′ 08′′ e': 'Belgique',
 '43° 42′ 26′′ n, 1° 03′ 19′′ w': 'France',
 '56° 08′ 59′′ n, 10° 13′ 27′′ e': 'Danemark',
 '44° 39′ 00′′ n, 10° 56′ 00′′ e': 'Italie',
 '46° 33′ 55′′ n, 3° 20′ 00′′ e': 'France',
 '46° 48′ 22′′ n, 7° 09′ 46′′ e': 'Suisse',
 '47° 48′ 09′′ n, 13° 02′ 45′′ e': 'Autriche',
 '46° 46′ 50′′ n, 4° 51′ 10′′ e': 'France',
 '46° 02′ 12′′ n, 4° 04′ 08′′ e': 'France',
 '48° 51′ 35′′ n, 2° 20′ 40′′ e': 'France',
 '47° 47′ 55′′ n, 3° 34′ 02′′ e': 'France',
 '52° 16′ 01′′ n, 10° 31′ 59′′ e': 'Allemagne',
 '48° 18′ 11′′ n, 14° 17′ 26′′ e': 'Autriche',
 '41° 49′ n, 71° 25′ w': 'États-Unis',
 '47° 59′ 44′′ n, 7° 51′ 08′′ e': 'France',
 '6° 14′ 00′′ n, 75° 34′ 00′′ w': 'Colombie',
 '48° 51′ 29′′ n, 2° 21′ 23′′ e': 'France',
 '48° 24′ 35′′ n, 2° 42′ 09′′ e': 'France',
 '44° 21′ 02′′ n, 2° 34′ 30′′ e': 'France',
 '48° 51′ 20′′ n, 2° 21′ 59′′ e': 'France',
 '49° 55′ 20′′ n, 1° 04′ 43′′ e': 'France',
 '58° 22′ 44′′ n, 26° 43′ 12′′ e': 'Estonie',
 '48° 25′ 47′′ n, 0° 05′ 31′′ e': 'France',
 '33° 26′ 54′′ n, 112° 04′ 26′′ w': 'États-Unis',
 '46° 48′ 37′′ n, 1° 41′ 28′′ e': 'France',
 '51° 57′ 47′′ n, 7° 37′ 43′′ e': 'Allemagne',
 '44° 07′ 41′′ n, 4° 04′ 54′′ e': 'France',
 '43° 36′ 19′′ n, 2° 14′ 27′′ e': 'France',
 '39° 34′ 00′′ n, 2° 39′ 00′′ e': 'Espagne',
 '31° 37′ 46′′ n, 7° 58′ 52′′ w': 'Maroc',
 '46° 21′ n, 72° 33′ w': 'Canada',
 '47° 15′ 36′′ n, 0° 04′ 37′′ w': 'France',
 '51° 13′ 33′′ n, 2° 55′ 10′′ e': 'Belgique',
 '39° 55′ 38′′ n, 32° 51′ 52′′ e': 'Turquie',
 '54° 54′ n, 23° 56′ e': 'Lituanie',
 '14° 35′ n, 120° 58′ e': 'Philippines',
 '48° 54′ 16′′ n, 2° 18′ 23′′ e': 'France',
 '52° 11′ 28′′ n, 2° 13′ 20′′ w': 'Royaume-Uni',
 '50° 06′ 21′′ n, 1° 50′ 03′′ e': 'France',
 '46° 18′ 22′′ n, 4° 49′ 53′′ e': 'France',
 '29° 25′ 30′′ n, 98° 29′ 38′′ w': 'États-Unis',
 '45° 09′ 23′′ n, 10° 47′ 28′′ e': 'Italie',
 '56° 27′ 51′′ n, 2° 58′ 13′′ w': 'Royaume-Uni',
 '41° 45′ 48′′ n, 72° 41′ 06′′ w': 'États-Unis',
 '37° 05′ 00′′ n, 15° 17′ 00′′ e': 'Italie',
 '54° 20′ 00′′ n, 10° 08′ 00′′ e': 'Allemagne',
 '43° 51′ 00′′ n, 10° 31′ 00′′ e': 'Italie',
 '44° 56′ 39′′ n, 93° 05′ 37′′ w': 'États-Unis',
 '35° 10′ 52′′ n, 136° 54′ 23′′ e': 'Japon',
 '55° 40′ 40′′ n, 12° 31′ 58′′ e': 'Danemark',
 '36° 43′ 15′′ n, 4° 24′ 54′′ w': 'Espagne',
 '48° 53′ 52′′ n, 2° 15′ 11′′ e': 'France',
 '34° 53′ 24′′ n, 1° 19′ 12′′ w': 'Algérie',
 '34° 41′ 29′′ n, 135° 11′ 31′′ e': 'Japon',
 '3° 25′ 16′′ n, 76° 31′ 20′′ w': 'Colombie',
 '45° 56′ 29′′ n, 0° 58′ 18′′ w': 'France',
 '49° 01′ 37′′ n, 1° 09′ 05′′ e': 'France',
 '32° 48′ 43′′ n, 34° 59′ 55′′ e': 'Israël',
 '63° 25′ 00′′ n, 10° 23′ 00′′ e': 'Norvège',
 '50° 58′ 41′′ n, 11° 01′ 45′′ e': 'Allemagne',
 '13° 05′ 24′′ n, 80° 16′ 12′′ e': 'Inde',
 '43° 15′ 24′′ n, 79° 52′ 09′′ w': 'Canada',
 '34° 09′ 48′′ n, 118° 07′ 37′′ w': 'États-Unis',
 '44° 55′ 34′′ n, 2° 26′ 26′′ e': 'France',
 '45° 24′ n, 71° 54′ w': 'Canada',
 '22° 16′ 33′′ s, 166° 27′ 29′′ e': 'Nouvelle-Calédonie',
 '46° 27′ 56′′ n, 6° 50′ 56′′ e': 'Suisse',
 '33° 35′ 24′′ n, 130° 24′ 06′′ e': 'Japon',
 '35° 06′ n, 129° 02′ e': 'Corée du Sud',
 '34° 05′ 54′′ n, 118° 19′ 36′′': 'États-Unis',
 '45° 09′ 30′′ n, 1° 31′ 55′′ e': 'France',
 '50° 55′ n, 5° 20′ e': 'Belgique',
 '31° 24′ 30′′ s, 64° 11′ 02′′ w': 'Argentine',
 '51° 37′ 00′′ n, 3° 57′ 00′′ w': 'Royaume-Uni',
 '47° 03′ n, 8° 18′ e': 'Suisse',
 '41° 59′ 48′′ n, 21° 25′ 57′′ e': 'Macédoine du Nord',
 '48° 32′ 26′′ n, 2° 39′ 36′′ e': 'France',
 '49° 21′ 32′′ n, 6° 10′ 09′′ e': 'France',
 '51° 31′ 01′′ n, 7° 27′ 00′′ e': 'Allemagne',
 '37° 52′ 13′′ n, 122° 16′ 05′′ w': 'États-Unis',
 '53° 47′ 31′′ n, 1° 45′ 14′′ w': 'Royaume-Uni',
 '41° 08′ 00′′ n, 16° 52′ 00′′ e': 'Italie',
 '50° 51′ n, 4° 22′ e': 'Belgique',
 '51° 29′ 34′′ n, 0° 13′ 22′′ w': 'Royaume-Uni',
 '51° 22′ 51′′ n, 2° 21′ 37′′ w': 'Royaume-Uni',
 '50° 04′ 55′′ n, 8° 14′ 29′′ e': 'Allemagne',
 '47° 14′ n, 39° 43′ e': 'Russie',
 '35° 51′ 26′′ n, 139° 38′ 57′′ e': 'Japon',
 '47° 37′ 23′′ n, 6° 09′ 21′′ e': 'France',
 '48° 25′ 00′′ n, 71° 04′ 00′′ w': 'Canada',
 '45° 33′ 00′′ n, 11° 33′ 00′′ e': 'Italie',
 '48° 25′ 20′′ n, 123° 21′ 57′′ w': 'Canada',
 '47° 25′ 00′′ n, 9° 22′ 00′′ e': 'Suisse',
 '36° 54′ 15′′ n, 7° 45′ 07′′ e': 'Algérie',
 '51° 30′ 01′′ n, 0° 11′ 27′′ w': 'Royaume-Uni',
 '47° 30′ 37′′ n, 6° 47′ 56′′ e': 'France',
 '49° 42′ 09′′ n, 4° 56′ 28′′ e': 'France',
 '9° 56′ 00′′ n, 84° 05′ 00′′ w': 'Costa Rica',
 '38° 11′ 00′′ n, 15° 33′ 00′′ e': 'Italie',
 '21° 02′ n, 105° 51′ e': 'Vietnam',
 '41° 15′ 31′′ n, 95° 56′ 15′′ w': 'États-Unis',
 '48° 50′ 52′′ n, 2° 26′ 21′′ e': 'France',
 '50° 43′ 00′′ n, 3° 31′ 00′′ w': 'Royaume-Uni',
 '45° 02′ 39′′ n, 3° 53′ 09′′ e': 'France',
 '36° 12′ 00′′ n, 37° 09′ 36′′ e': 'Syrie',
 '12° 21′ 58′′ n, 1° 31′ 05′′ w': 'Burkina Faso',
 '44° 26′ 54′′ n, 1° 26′ 29′′ e': 'France',
 '48° 34′ 42′′ n, 3° 49′ 36′′ w': 'France',
 '48° 35′ 22′′ n, 6° 30′ 06′′ e': 'France',
 '37° 52′ 45′′ n, 4° 46′ 47′′ w': 'Espagne',
 '30° 19′ n, 81° 39′ w': 'États-Unis',
 '51° 25′ 29′′ n, 6° 45′ 03′′ e': 'Allemagne',
 '48° 55′ 25′′ n, 2° 15′ 08′′ e': 'France',
 '48° 47′ 58′′ n, 2° 29′ 59′′ e': 'France',
 '48° 28′ 03′′ n, 35° 02′ 24′′ e': 'Ukraine',
 '37° 18′ 15′′ n, 121° 52′ 22′′ w': 'États-Unis',
 '41° 19′ 39′′ n, 19° 49′ 07′′ e': 'Albanie',
 '50° 50′ 00′′ n, 12° 55′ 00′′ e': 'Allemagne',
 '45° 45′ 35′′ n, 21° 13′ 48′′ e': 'Roumanie',
 '50° 54′ 54′′ n, 1° 23′ 43′′ w': 'Royaume-Uni',
 '24° 40′ 57′′ n, 46° 44′ 16′′ e': 'Arabie saoudite',
 '38° 25′ n, 27° 08′ e': 'Turquie',
 '36° 09′ 00′′ n, 5° 26′ 00′′ e': 'Algérie',
 '43° 16′ 39′′ n, 76° 53′ 45′′ e': 'Kazakhstan',
 '43° 40′ 00′′ n, 6° 55′ 00′′ e': 'France',
 '50° 58′ 59′′ n, 11° 19′ 01′′ e': 'Allemagne',
 '46° 04′ 00′′ n, 13° 14′ 00′′ e': 'Italie',
 '48° 56′ 52′′ n, 2° 14′ 51′′ e': 'France',
 '53° 52′ 01′′ n, 10° 42′ 00′′ e': 'Allemagne',
 '48° 57′ 37′′ n, 2° 53′ 18′′ e': 'France',
 '37° 32′ 27′′ n, 77° 26′ 12′′ w': 'États-Unis',
 '0° 23′ 24′′ n, 9° 27′ 15′′ e': 'Gabon',
 '60° 27′ 06′′ n, 22° 16′ 01′′ e': 'Finlande',
 '42° 59′ 01′′ n, 81° 14′ 59′′ w': 'Canada',
 '48° 54′ 39′′ n, 2° 17′ 20′′ e': 'France',
 '56° 18′ 40,32′′ n, 43° 55′ 50,88′′ e': 'Russie',
 '4° 56′ 05′′ n, 52° 19′ 49′′ w': 'Guyane française',
 '44° 48′ 31′′ n, 0° 35′ 18′′ w': 'France',
 '47° 09′ 44′′ n, 27° 35′ 20′′ e': 'Roumanie',
 '43° 53′ 29′′ n, 0° 29′ 58′′ w': 'France',
 '43° 07′ 00′′ n, 12° 23′ 00′′ e': 'Italie',
 '34° 58′ 37′′ n, 138° 22′ 59′′ e': 'Japon',
 '34° 31′ 01′′ n, 69° 07′ 59′′ e': 'Afghanistan',
 '48° 47′ 28′′ n, 2° 27′ 46′′ e': 'France',
 '51° 07,52′ n, 4° 34,1′ e': 'Belgique',
 '2° 11′ 00′′ s, 79° 53′ 00′′ w': 'Équateur',
 '35° 49′ 34′′ n, 10° 38′ 24′′ e': 'Tunisie',
 '48° 52′ 58′′ n, 2° 22′ 55′′ e': 'France',
 '44° 33′ 34′′ n, 6° 04′ 43′′ e': 'France',
 '51° 33′ 15′′ n, 0° 10′ 28′′ w': 'Royaume-Uni',
 '18° 54′ 44′′ s, 47° 31′ 18′′ e': 'Madagascar',
 '1° 17′ 00′′ s, 36° 49′ 00′′ e': 'Kenya',
 '47° 16′ 50′′ n, 2° 12′ 31′′ w': 'France',
 '45° 15′ 33′′ n, 19° 49′ 45′′ e': 'Serbie',
 '53° 13′ 07′′ n, 6° 34′ 02′′ e': 'Pays-Bas',
 '42° 51′ 00′′ n, 2° 41′ 00′′ w': 'France',
 '6° 21′ 36′′ n, 2° 26′ 24′′ e': 'Bénin',
 '48° 50′ 38′′ n, 2° 13′ 09′′ e': 'France',
 '39° 46′ n, 84° 12′ w': 'États-Unis',
 '55° 23′ 45,48′′ n, 10° 23′ 18,73′′ e': 'Danemark',
 '42° 02′ 28′′ n, 87° 41′ 24′′ w': 'États-Unis',
 '47° 03′ 36′′ n, 0° 52′ 42′′ w': 'France',
 '49° 22′ 54′′ n, 3° 19′ 25′′ e': 'France',
 '55° 47′ n, 49° 10′ e': 'Russie',
 '46° 40′ 31′′ n, 5° 33′ 16′′ e': 'France',
 '34° 23′ 13′′ n, 132° 26′ 43′′ e': 'Japon',
 '45° 44′ 00′′ n, 7° 19′ 00′′ e': 'Italie',
 '45° 16′ 02′′ n, 1° 45′ 56′′ e': 'France',
 '46° 20′ 27′′ n, 2° 36′ 12′′ e': 'France',
 '51° 50′ 03′′ n, 12° 14′ 16′′ e': 'Allemagne',
 '19° 55′ 41′′ s, 43° 56′ 31′′ w': 'Brésil',
 '33° 53′ 42′′ n, 5° 33′ 17′′ w': 'Maroc',
 '45° 19′ 38′′ n, 14° 26′ 33′′ e': 'Croatie',
 '51° 48′ 00′′ n, 4° 41′ 00′′ e': 'Pays-Bas',
 '47° 51′ 12′′ n, 5° 20′ 02′′ e': 'France',
 '48° 54′ 47′′ n, 2° 23′ 00′′ e': 'France',
 '45° 46′ 41′′ n, 4° 49′ 41′′ e': 'France',
 '45° 44′ 47′′ n, 0° 38′ 00′′ w': 'France',
 '46° 07′ 28′′ n, 3° 25′ 42′′ e': 'France',
 '54° 05′ 00′′ n, 12° 08′ 00′′ e': 'Allemagne',
 '17° 51′ 50′′ s, 31° 01′ 47′′ e': 'Zimbabwe',
 '56° 50′ n, 60° 35′ e': 'Russie',
 '43° 27′ 36′′ n, 3° 48′ 00′′ w': 'Espagne',
 '51° 19′ n, 4° 56′ e': 'Belgique',
 '44° 38′ 52′′ n, 63° 34′ 17′′ w': 'Canada',
 '59° 50′ 00′′ n, 17° 40′ 00′′ e': 'Suède',
 '10° 46′ 01′′ n, 106° 40′ 01′′ e': 'Vietnam',
 '32° 47′ 00′′ n, 79° 55′ 55′′ w': 'États-Unis',
 '49° 14′ 00′′ n, 7° 00′ 00′′ e': 'Allemagne',
 '48° 53′ 42′′ n, 2° 17′ 14′′ e': 'France',
 '45° 53′ 40′′ n, 3° 06′ 48′′ e': 'France',
 '31° 32′ 59′′ n, 74° 20′ 37′′ e': 'Pakistan',
 '50° 44′ 46′′ n, 2° 15′ 42′′ e': 'France',
 '49° 44′ 51′′ n, 13° 22′ 39′′ e': 'Tchéquie',
 '46° 46′ 08′′ n, 23° 35′ 26′′ e': 'Roumanie',
 '45° 11′ 00′′ n, 9° 09′ 00′′ e': 'Italie',
 '48° 46′ 19′′ n, 5° 09′ 37′′ e': 'France',
 '32° 45′ 23′′ n, 97° 19′ 57′′ w': 'États-Unis',
 '17° 32′ 06′′ s, 149° 34′ 11′′ w': 'Polynésie française',
 '47° 08′ 06′′ n, 7° 14′ 24′′ e': 'Suisse',
 '34° 41′ 11′′ n, 135° 31′ 12′′ e': 'Japon',
 '39° 01′ 00′′ n, 125° 44′ 00′′ e': 'Corée du Nord',
 '49° 33′ 50′′ n, 3° 37′ 28′′ e': 'France',
 '45° 08′ 00′′ n, 10° 02′ 00′′ e': 'Italie',
 '48° 48′ 05′′ n, 2° 15′ 46′′ e': 'France',
 '45° 49′ 00′′ n, 9° 05′ 00′′ e': 'Italie',
 '45° 40′ 20′′ n, 12° 14′ 32′′ e': 'Italie',
 '51° 50′ 00′′ n, 5° 52′ 00′′ e': 'Pays-Bas',
 '37° 41′ 20′′ n, 97° 20′ 10′′ w': 'États-Unis',
 '46° 49′ 04′′ n, 0° 32′ 46′′ e': 'France',
 '8° 03′ 14′′ s, 34° 52′ 51′′ w': 'Brésil',
 '47° 30′ n, 8° 45′ e': 'Suisse',
 '52° 00′ 42′′ n, 4° 21′ 25′′ e': 'Pays-Bas',
 '36° 08′ n, 95° 56′ w': 'États-Unis',
 '42° 08′ 48′′ n, 24° 45′ 03′′ e': 'Bulgarie',
 '16° 30′ 00′′ s, 68° 08′ 56′′ w': 'Bolivie',
 '51° 32′ 00′′ n, 9° 56′ 00′′ e': 'Allemagne',
 '50° 56′ n, 4° 02′ e': 'Belgique',
 '53° 44′ 40′′ n, 0° 19′ 57′′ w': 'Royaume-Uni',
 '49° 01′ 00′′ n, 12° 06′ 00′′ e': 'Allemagne',
 '50° 56′ n, 3° 07′ e': 'Belgique',
 '44° 03′ 21′′ n, 5° 02′ 56′′ e': 'France',
 '50° 50′ 00′′ n, 4° 18′ 00′′ e': 'Belgique',
 '48° 51′ 36′′ n, 2° 20′ 31′′ e': 'France',
 '42° 39′ n, 73° 46′ w': 'États-Unis',
 '51° 59′ 00′′ n, 5° 55′ 00′′ e': 'Pays-Bas',
 '25° 02′ 15′′ n, 121° 33′ 45′′ e': 'Taïwan',
 '48° 44′ 14′′ n, 1° 21′ 59′′ e': 'France',
 '28° 37′ n, 77° 14′ e': 'Inde',
 '51° 09′ n, 4° 08′ e': 'Belgique',
 '30° 18′ 00′′ n, 97° 44′ 00′′ w': 'États-Unis',
 '35° 52′ n, 128° 36′ e': 'Corée du Sud',
 '25° 58′ s, 32° 35′ e': 'Mozambique',
 '35° 46′ 01′′ n, 5° 48′ 00′′ w': 'Maroc',
 '47° 05′ 30′′ n, 5° 29′ 47′′ e': 'France',
 '33° 02′ 47′′ s, 71° 37′ 11′′ w': 'Chili',
 '43° 04′ 29′′ n, 89° 23′ 04′′ w': 'États-Unis',
 '34° 41′ 29′′ n, 135° 10′ 59′′ e': 'Japon',
 '50° 51′ 00′′ n, 5° 41′ 00′′ e': 'Belgique',
 '35° 10′ 49′′ n, 136° 54′ 23′′ e': 'Japon',
 '9° 02′ n, 38° 44′ e': 'Éthiopie',
 '50° 21′ 00′′ n, 7° 36′ 00′′ e': 'Allemagne',
 '43° 22′ 00′′ n, 5° 50′ 00′′ w': 'Espagne',
 '43° 37′ 00′′ n, 13° 31′ 00′′ e': 'Italie',
 '45° 52′ 49′′ s, 170° 30′ 13′′ e': 'Nouvelle-Zélande',
 '11° 52′ n, 15° 36′ w': 'Guinée-Bissau',
 '49° 24′ 54′′ n, 2° 49′ 23′′ e': 'France',
 '51° 26′ 17′′ n, 5° 28′ 31′′ e': 'Pays-Bas',
 '5° 49′ 25′′ n, 55° 10′ 11′′ w': 'Suriname',
 '61° 29′ 53′′ n, 23° 45′ 36′′ e': 'Finlande',
 '46° 13′ 40′′ n, 7° 21′ 31′′ e': 'Suisse',
 '25° 40′ 56′′ n, 100° 18′ 40′′ w': 'Mexique',
 '48° 50′ 12′′ n, 2° 28′ 57′′ e': 'France',
 '41° 39′ 10′′ n, 83° 32′ 16′′ w': 'États-Unis',
 '44° 03′ 00′′ n, 12° 33′ 58′′ e': 'Italie',
 '35° 28′ 56′′ n, 97° 32′ 07′′ w': 'États-Unis',
 '35° 33′ n, 6° 10′ e': 'Algérie',
 '48° 00′ n, 37° 48′ e': 'Ukraine',
 '50° 51′ n, 2° 53′ e': 'Belgique',
 '48° 27′ 23′′ n, 2° 02′ 56′′ w': 'France',
 '54° 54′ 22′′ n, 1° 22′ 53′′ w': 'Royaume-Uni',
 '18° 27′ n, 66° 04′ w': 'Porto Rico',
 '58° 58′ 10′′ n, 5° 43′ 56′′ e': 'Norvège',
 '52° 24′ 29′′ n, 1° 30′ 38′′ w': 'Royaume-Uni',
 '46° 04′ 00′′ n, 11° 07′ 00′′ e': 'Italie',
 '46° 30′ 00′′ n, 11° 21′ 00′′ e': 'Italie',
 '49° 45′ 35′′ n, 6° 38′ 38′′ e': 'Luxembourg',
 '48° 48′ 47′′ n, 2° 14′ 19′′ e': 'France',
 '50° 49′ 27′′ n, 4° 20′ 45′′ e': 'Belgique',
 '48° 49′ 26′′ n, 2° 12′ 42′′ e': 'France',
 '52° 14′ 14′′ n, 0° 53′ 46′′ w': 'Royaume-Uni',
 '34° 41′ 12′′ n, 1° 54′ 41′′ w': 'Algérie',
 '43° 03′ n, 141° 21′ e': 'Japon',
 '45° 12′ 26′′ n, 5° 44′ 28′′ e': 'France',
 '11° 40′ 11′′ s, 27° 29′ 00′′ e': 'Zambie',
 '43° 56′ 00′′ n, 10° 55′ 00′′ e': 'Italie',
 '35° 11′ 38′′ n, 0° 38′ 29′′ w': 'Algérie',
 '40° 48′ 33′′ n, 73° 56′ 54′′ w': 'États-Unis',
 '44° 14′ 00′′ n, 12° 03′ 00′′ e': 'Italie',
 '52° 35′ 05′′ n, 2° 07′ 40′′ w': 'Royaume-Uni',
 '50° 22′ 12′′ n, 4° 08′ 31′′ w': 'Royaume-Uni',
 '44° 42′ 00′′ n, 10° 38′ 00′′ e': 'Italie',
 '51° 14′ 00′′ n, 22° 34′ 00′′ e': 'Pologne',
 '44° 54′ 58′′ n, 0° 14′ 34′′ w': 'France',
 '40° 12′ 00′′ n, 8° 25′ 00′′ w': 'Portugal',
 '46° 57′ 06′′ n, 4° 17′ 58′′ e': 'France',
 '43° 38′ 47′′ n, 0° 35′ 08′′ e': 'France',
 '16° 02′ n, 16° 30′ w': 'Sénégal',
 '44° 25′ 00′′ n, 12° 12′ 00′′ e': 'Italie',
 '41° 32′ 54′′ n, 2° 06′ 27′′ e': 'Espagne',
 '48° 51′ 18′′ n, 2° 21′ 24′′ e': 'France',
 '35° 10′ 01′′ n, 33° 21′ 00′′ e': 'Chypre',
 '42° 20′ 27′′ n, 3° 41′ 59′′ w': 'Espagne',
 '50° 51′ n, 4° 19′ e': 'Belgique',
 '38° 20′ 43′′ n, 0° 28′ 59′′ w': 'Espagne',
 '35° 18′ 29,86′′ s, 149° 07′ 27,8′′ e': 'Australie',
 '45° 59′ 25′′ n, 4° 43′ 13′′ e': 'France',
 '48° 40′ 30′′ n, 5° 53′ 30′′ e': 'France',
 '50° 31′ n, 5° 14′ e': 'Belgique',
 '49° 03′ 06′′ n, 2° 06′ 06′′ e': 'France',
 '36° 29′ 00′′ n, 2° 50′ 00′′ e': 'Algérie',
 '25° 27′ 19′′ s, 49° 15′ 46′′ w': 'Brésil',
 '50° 15′ 54′′ n, 19° 01′ 26′′ e': 'Pologne',
 '46° 15′ 18′′ n, 20° 08′ 42′′ e': 'Hongrie',
 '35° 52′ n, 139° 39′ e': 'Japon',
 '43° 28′ 54′′ n, 1° 33′ 22′′ w': 'France',
 '6° 29′ 50′′ n, 2° 36′ 18′′ e': 'Bénin',
 '32° 41′ n, 51° 41′ e': 'Iran',
 '42° 06′ 45′′ n, 72° 32′ 51′′ w': 'États-Unis',
 '36° 46′ 54′′ n, 119° 47′ 32′′ w': 'États-Unis',
 '39° 13′ n, 9° 07′ e': 'Italie',
 '51° 42′ 00′′ n, 5° 19′ 00′′ e': 'Pays-Bas',
 '48° 17′ 06′′ n, 6° 57′ 00′′ e': 'France',
 '43° 22′ 17′′ n, 8° 23′ 46′′ w': 'Espagne',
 '49° 27′ 45′′ n, 1° 05′ 14′′ e': 'France',
 '47° 15′ 09′′ n, 122° 26′ 51′′': 'États-Unis',
 '53° 12′ 00′′ n, 5° 47′ 00′′ e': 'Pays-Bas',
 '39° 44′ 54′′ n, 75° 33′ 05′′ w': 'États-Unis',
 '51° 35′ 00′′ n, 4° 47′ 00′′ e': 'Pays-Bas',
 '37° 27′ 50′′ n, 126° 38′ 55′′ e': 'Corée du Sud',
 '21° 25′ 21′′ n, 39° 49′ 34′′ e': 'Arabie saoudite',
 '48° 48′ 28′′ n, 2° 22′ 29′′ e': 'France',
 '24° 51′ n, 67° 00′ e': 'Pakistan',
 '38° 04′ 48′′ n, 46° 17′ 31′′ e': 'Iran',
 '50° 16′ 39′′ n, 3° 58′ 24′′ e': 'Belgique',
 '48° 43′ 57′′ n, 2° 26′ 59′′ e': 'France',
 '46° 48′ 00′′ n, 71° 11′ 00′′ w': 'Canada',
 '52° 39′ 55′′ n, 8° 37′ 26′′ w': 'Irlande',
 '36° 32′ 00′′ n, 6° 17′ 00′′ w': 'Espagne',
 '50° 37′ 48′′ n, 3° 46′ 50′′ e': 'Belgique',
 '34° 10′ 15′′ n, 118° 15′ 00′′': 'États-Unis',
 '48° 55′ 03′′ n, 2° 16′ 06′′ e': 'France',
 '41° 04′ 23′′ n, 81° 31′ 04′′ w': 'États-Unis',
 '36° 50′ 49′′ n, 76° 17′ 07′′ w': 'États-Unis',
 '46° 00′ 24′′ n, 8° 57′ 05′′ e': 'Italie',
 '45° 46′ 07′′ n, 4° 50′ 01′′ e': 'France',
 '51° 27′ 15′′ n, 0° 58′ 23′′ w': 'Royaume-Uni',
 '55° 50′ 44′′ n, 4° 25′ 03′′ w': 'Royaume-Uni',
 '43° 32′ 00′′ n, 5° 42′ 00′′ w': 'Espagne',
 '42° 57′ 40′′ n, 85° 39′ 50′′ w': 'États-Unis',
 '48° 58′ 11′′ n, 2° 18′ 29′′ e': 'France',
 '51° 20′ 00′′ n, 6° 34′ 00′′ e': 'Allemagne',
 '49° 06′ 52′′ n, 1° 05′ 30′′ w': 'France',
 '44° 33′ 29′′ n, 4° 45′ 03′′ e': 'France',
 '48° 54′ 08′′ n, 2° 28′ 58′′ e': 'France',
 '51° 32′ 38′′ n, 0° 06′ 10′′ w': 'Royaume-Uni'
 }

LIST_OF_GOOD_LOCALISATION = """48° 51′ 24′′ n, 2° 21′ 07′′ e
51° 30′ 26′′ n, 0° 07′ 39′′ w
40° 42′ 46′′ n, 74° 00′ 22′′ w
41° 53′ 19′′ n, 12° 29′ 12′′ e
52° 31′ n, 13° 23′ e
45° 30′ 12′′ n, 73° 35′ 13′′ w
48° 12′ 30′′ n, 16° 22′ 21′′ e
55° 45′ 09′′ n, 37° 37′ 23,11′′ e
43° 17′ 47′′ n, 5° 22′ 12′′ e
50° 51′ 01′′ n, 4° 21′ 00′′ e
41° 52′ 55′′ n, 87° 37′ 40′′ w
34° 03′ n, 118° 15′ w
40° 26′ 00′′ n, 3° 41′ 00′′ w
45° 45′ 28′′ n, 4° 49′ 56′′ e
35° 41′ 22′′ n, 139° 41′ 30′′ e
59° 56′ 02′′ n, 30° 18′ 22′′ e
47° 29′ 54′′ n, 19° 02′ 27′′ e
45° 28′ 00′′ n, 9° 10′ 00′′ e
41° 22′ 57′′ n, 2° 10′ 37′′ e
40° 39′ 03′′ n, 73° 56′ 59′′ w
44° 50′ 16′′ n, 0° 34′ 46′′ w
43° 36′ 16′′ n, 1° 26′ 38′′ e
34° 36′ 29′′ s, 58° 22′ 13′′ w
39° 57′ 10′′ n, 75° 09′ 49′′ w
52° 22′ n, 4° 53′ e
51° 13′ n, 4° 24′ e
43° 46′ 18′′ n, 11° 15′ 13′′ e
48° 34′ 24′′ n, 7° 45′ 08′′ e
46° 12′ 00′′ n, 6° 09′ 00′′ e
40° 50′ 00′′ n, 14° 15′ 00′′ e
47° 13′ 05′′ n, 1° 33′ 10′′ w
52° 13′ 56′′ n, 21° 00′ 30′′ e
50° 05′ 16′′ n, 14° 25′ 14′′ e
48° 09′ 00′′ n, 11° 34′ 30′′ e
55° 41′ 24′′ n, 12° 35′ 09,6′′ e
43° 40′ 13′′ n, 79° 23′ 12′′ w
53° 20′ 36′′ n, 6° 16′ 03′′ w
36° 47′ 51′′ n, 10° 09′ 57′′ e
50° 38′ 23′′ n, 5° 34′ 14′′ e
36° 46′ 34′′ n, 3° 03′ 36′′ e
50° 38′ 14′′ n, 3° 03′ 48′′ e
42° 21′ 37′′ n, 71° 03′ 28′′ w
53° 33′ n, 10° 00′ e
48° 53′ 17′′ n, 2° 16′ 07′′ e
59° 19′ 46′′ n, 18° 04′ 07′′ e
49° 26′ 36′′ n, 1° 06′ 00′′ e
33° 51′ 22′′ s, 151° 11′ 33′′ e
22° 54′ 35′′ s, 43° 10′ 35′′ w
45° 04′ 00′′ n, 7° 42′ 00′′ e
19° 21′ 14′′ n, 99° 08′ 09′′ w
43° 41′ 45′′ n, 7° 16′ 17′′ e
43° 09′ 57.30′′ n, 4° 02′ 49.41′′ w
33° 26′ 16′′ s, 70° 39′ 02′′ w
38° 53′ 42′′ n, 77° 02′ 12′′ w
48° 49′ 59′′ n, 2° 19′ 36′′ e
43° 36′ 43′′ n, 3° 52′ 38′′ e
38° 43′ n, 9° 08′ w
48° 41′ 37′′ n, 6° 11′ 05′′ e
49° 07′ 13′′ n, 6° 10′ 40′′ e
48° 06′ 53′′ n, 1° 40′ 46′′ w
37° 33′ 57′′ n, 126° 58′ 41′′ e
45° 26′ 23′′ n, 12° 19′ 55′′ e
55° 51′ 29′′ n, 4° 15′ 32′′ w
33° 34′ 42,44′′ n, 7° 36′ 23,89′′ w
51° 03′ n, 3° 44′ e
48° 51′ 46′′ n, 2° 16′ 34′′ e
34° 53′ 00′′ s, 56° 10′ 00′′ w
44° 24′ 48′′ n, 26° 05′ 52′′ e
48° 50′ 07′′ n, 2° 14′ 27′′ e
37° 46′ 30′′ n, 122° 25′ 10′′ w
46° 48′ 58′′ n, 71° 13′ 27′′ w
48° 48′ 19′′ n, 2° 08′ 06′′ e
44° 30′ 00′′ n, 11° 21′ 00′′ e
46° 31′ 16′′ n, 6° 37′ 52′′ e
44° 24′ 24′′ n, 8° 56′ 00′′ e
47° 22′ 40′′ n, 8° 32′ 28′′ e
37° 48′ 51′′ s, 144° 58′ 06′′ e
48° 52′ 19′′ n, 2° 21′ 27′′ e
23° 32′ 52′′ s, 46° 38′ 11′′ w
55° 57′ 17′′ n, 3° 12′ 06′′ w
37° 58′ 00′′ n, 23° 43′ 00′′ e
60° 10′ 15′′ n, 24° 56′ 15′′ e
59° 54′ 48′′ n, 10° 44′ 20′′ e
47° 19′ 18′′ n, 5° 02′ 29′′ e
42° 19′ 54′′ n, 83° 02′ 51′′ w
45° 11′ 16′′ n, 5° 43′ 37′′ e
50° 07′ 01′′ n, 8° 40′ 59′′ e
12° 02′ 43′′ s, 77° 01′ 52′′ w
49° 15′ 46′′ n, 4° 02′ 05′′ e
35° 40′ 51′′ n, 51° 24′ 50′′ e
30° 02′ 40′′ n, 31° 14′ 44′′ e
39° 28′ 13′′ n, 0° 22′ 36′′ w
50° 27′ 13′′ n, 30° 30′ 59′′ e
44° 49′ n, 20° 28′ e
43° 07′ 20′′ n, 5° 55′ 48′′ e
52° 28′ 59′′ n, 1° 53′ 37′′ w
47° 14′ 35′′ n, 6° 01′ 19′′ e
48° 53′ 04′′ n, 2° 19′ 19′′ e
4° 18′ 23′′ s, 15° 18′ 31′′ e
14° 43′ 55′′ n, 17° 27′ 26′′ w
41° 43′ 01′′ n, 44° 46′ 59′′ e
38° 38′ 53′′ n, 90° 12′ 44′′ w
53° 24′ 33′′ n, 2° 59′ 09′′ w
47° 23′ 37′′ n, 0° 41′ 21′′ e
48° 23′ 27′′ n, 4° 29′ 08′′ w
40° 23′ 43′′ n, 49° 52′ 56′′ e
41° 00′ 44′′ n, 28° 58′ 34′′ e
50° 56′ 33′′ n, 6° 57′ 32′′ e
43° 50′ 16′′ n, 4° 21′ 39′′ e
53° n, 1° w
43° 57′ 00′′ n, 4° 49′ 01′′ e
51° 03′ 00′′ n, 13° 44′ 00′′ e
47° 28′ 25′′ n, 0° 33′ 15′′ w
47° 54′ 09′′ n, 1° 54′ 32′′ e
51° 20′ 25′′ n, 12° 22′ 29′′ e
49° 15′ 39′′ n, 123° 06′ 50′′ w
39° 17′ 11′′ n, 76° 36′ 54′′ w
38° 07′ 00′′ n, 13° 22′ 00′′ e
45° 46′ 33′′ n, 3° 04′ 56′′ e
41° 00′ 45′′ n, 28° 58′ 48′′ e
51° 55′ 00′′ n, 4° 29′ 00′′ e
56° 56′ 56′′ n, 24° 06′ 23′′ e
52° 05′ n, 4° 19′ e
35° 42′ 10′′ n, 0° 38′ 57′′ w
45° 26′ 05′′ n, 4° 23′ 25′′ e
41° 29′ 57′′ n, 81° 41′ 41′′ w
48° 50′ 29′′ n, 2° 18′ 01′′ e
48° 52′ 40′′ n, 2° 19′ 04′′ e
49° 10′ 56′′ n, 0° 22′ 14′′ w
53° 29′ 00′′ n, 2° 15′ 00′′ w
31° 11′ 53′′ n, 29° 55′ 09′′ e
48° 46′ 36′′ n, 9° 10′ 40′′ e
48° 52′ 21′′ n, 2° 20′ 25′′ e
48° 52′ 22′′ n, 2° 20′ 26′′ e
47° 34′ 01′′ n, 7° 34′ 59′′ e
49° 53′ 39′′ n, 2° 17′ 45′′ e
29° 45′ 46′′ n, 95° 22′ 59′′ w
50° 04′ n, 19° 57′ e
43° 31′ 52′′ n, 5° 27′ 14′′ e
48° 51′ 02′′ n, 2° 19′ 58′′ e
47° 44′ 58′′ n, 7° 20′ 24′′ e
48° 50′ 28′′ n, 2° 23′ 17′′ e
40° 26′ 30′′ n, 80° 00′ 00′′ w
51° 07′ 00′′ n, 17° 02′ 00′′ e
42° 41′ 55′′ n, 2° 53′ 44′′ e
45° 51′ 00′′ n, 1° 15′ 00′′ e
40° 50′ 14′′ n, 73° 53′ 10′′ w
36° 51′ 00′′ s, 174° 47′ 00′′ e
51° 12′ n, 3° 13′ e
42° 41′ 50′′ n, 23° 19′ 00′′ e
43° 29′ 37′′ n, 1° 28′ 30′′ w
40° 43′ 42′′ n, 73° 59′ 39′′ w
45° 48′ 47′′ n, 15° 58′ 38′′ e
23° 08′ 20′′ n, 82° 21′ 26′′ w
29° 58′ 34′′ n, 90° 04′ 42′′ w
41° 08′ 58′′ n, 8° 36′ 39′′ w
46° 56′ 57′′ n, 7° 26′ 50′′ e
51° 13′ 32′′ n, 6° 46′ 58′′ e
5° 20′ 11′′ n, 4° 01′ 36′′ w
48° 51′ 10′′ n, 2° 19′ 46′′ e
48° 52′ 01′′ n, 2° 20′ 26′′ e
48° 52′ 12′′ n, 2° 19′ 15′′ e
33° 45′ 16′′ n, 84° 23′ 23′′ w
54° 35′ 46′′ n, 5° 54′ 50′′ w
49° 29′ 24′′ n, 0° 06′ 00′′ e
43° 18′ 06′′ n, 0° 22′ 07′′ w
50° 49′ 58′′ n, 4° 22′ 03′′ e
52° 22′ 28′′ n, 9° 44′ 19′′ e
48° 56′ 08′′ n, 2° 21′ 14′′ e
59° 26′ 00′′ n, 24° 43′ 50′′ e
33° 53′ 23′′ n, 35° 30′ 01′′ e
3° 52′ n, 11° 31′ e
57° 42′ 00′′ n, 11° 56′ 00′′ e
46° 28′ n, 30° 44′ e
48° 51′ 30′′ n, 2° 22′ 47′′ e
48° 53′ 32′′ n, 2° 20′ 40′′ e
52° 12′ 29′′ n, 0° 07′ 21′′ e
26° 12′ 16′′ s, 28° 02′ 44′′ e
47° 36′ 18′′ n, 122° 19′ 48′′ w
32° 46′ 45′′ n, 96° 48′ 32′′ w
39° 06′ 00′′ n, 84° 30′ 45′′ w
34° 01′ 16′′ n, 6° 50′ 29′′ w
46° 34′ 55′′ n, 0° 20′ 10′′ e
37° 23′ 00′′ n, 5° 59′ 48′′ w
34° 41′ 37′′ n, 135° 30′ 07′′ e
45° 25′ 29′′ n, 75° 41′ 42′′ w
48° 51′ 25′′ n, 2° 19′ 12′′ e
50° 48′ n, 4° 20′ e
4° 36′ 36′′ n, 74° 04′ 55′′ w
48° 00′ 15′′ n, 0° 11′ 49′′ e
50° 28′ n, 4° 52′ e
4° 03′ n, 9° 42′ e
6° 27′ 06′′ n, 3° 23′ 21′′ e
10° 29′ 28′′ n, 66° 54′ 07′′ w
50° 41′ 24′′ n, 3° 10′ 54′′ e
50° 53′ n, 4° 42′ e
18° 55′ 55′′ n, 72° 50′ 10′′ e
49° 51′ n, 24° 01′ e
53° 55′ 45′′ n, 27° 29′ 46′′ e
31° 13′ 56′′ n, 121° 28′ 09′′ e
45° 34′ 12′′ n, 5° 54′ 42′′ e
52° 05′ 00′′ n, 5° 06′ 00′′ e
49° 27′ 00′′ n, 11° 05′ 00′′ e
48° 17′ 51′′ n, 4° 04′ 27′′ e
27° 28′ 00′′ s, 153° 02′ 00′′ e
48° 51′ 02′′ n, 2° 19′ 57′′ e
50° 21′ 29′′ n, 3° 31′ 24′′ e
44° 58′ 55′′ n, 93° 16′ 09′′ w
18° 32′ 24′′ n, 72° 20′ 24′′ w
31° 47′ 00′′ n, 35° 13′ 00′′ e
35° 01′ n, 135° 46′ e
39° 54′ 13′′ n, 116° 23′ 15′′ e
17° 59′ n, 76° 48′ w
54° 44′ n, 20° 29′ e
12° 38′ 00′′ n, 7° 59′ 00′′ w
32° 42′ 54′′ n, 117° 09′ 45′′ w
49° 59′ 33′′ n, 36° 13′ 52′′ e
43° 20′ 51′′ n, 3° 13′ 08′′ e
25° 47′ n, 80° 13′ w
33° 55′ 31′′ s, 18° 25′ 26′′ e
54° 41′ n, 25° 16′ e
54° 58′ 00′′ n, 1° 36′ 00′′ w
5° 33′ 29′′ n, 0° 12′ 04′′ w
46° 03′ 05,13′′ n, 14° 30′ 21,47′′ e
51° 45′ 07′′ n, 1° 15′ 28′′ w
39° 44′ 21′′ n, 104° 59′ 05′′ w
64° 08′ 51′′ n, 21° 56′ 06′′ w
49° 53′ 44′′ n, 97° 08′ 19′′ w
43° 03′ n, 87° 57′ w
37° 48′ n, 122° 15′ w
40° 44′ 08′′ n, 74° 10′ 20′′ w
47° 04′ 14′′ n, 15° 26′ 17′′ e
40° 09′ 33′′ n, 44° 30′ 33′′ e
53° 47′ 59′′ n, 1° 32′ 57′′ w
50° 27′ 18′′ n, 3° 57′ 07′′ e
53° 22′ 01′′ n, 1° 30′ 00′′ w
51° 27′ 00′′ n, 2° 34′ 59′′ w
46° 59′ 25′′ n, 6° 55′ 50′′ e
48° 08′ 41′′ n, 17° 06′ 46′′ e
45° 26′ 00′′ n, 10° 59′ 00′′ e
45° 25′ 00′′ n, 11° 52′ 00′′ e
45° 31′ 59′′ n, 10° 13′ 59′′ e
45° 54′ 58′′ n, 6° 07′ 59′′ e
49° 11′ 31′′ n, 16° 36′ 47′′ e
39° 03′ n, 94° 35′ w
51° 45′ 00′′ n, 19° 28′ 00′′ e
50° 25′ 00′′ n, 4° 26′ 39′′ e
51° 03′ n, 114° 04′ w
48° 04′ 54′′ n, 7° 21′ 20′′ e
54° 21′ 07′′ n, 18° 38′ 48′′ e
47° 05′ 04′′ n, 2° 23′ 47′′ e
47° 45′ n, 3° 22′ w
45° 39′ n, 13° 46′ e
48° 04′ 22′′ n, 0° 46′ 12′′ w
50° 36′ n, 3° 23′ e
42° 53′ 11′′ n, 78° 52′ 41′′ w
50° 49′ 43′′ n, 4° 23′ 23′′ e
48° 38′ 50′′ n, 2° 00′ 32′′ w
48° 30′ 49′′ n, 2° 45′ 55′′ w
48° 52′ n, 2° 13′ e
51° 01′ n, 4° 28′ e
33° 20′ 00′′ n, 44° 26′ 00′′ e
32° 57′ 04′′ s, 60° 39′ 59′′ w
41° 39′ 00′′ n, 0° 53′ 00′′ w
57° 09′ 00′′ n, 2° 07′ 23′′ w
53° 32′ 00′′ n, 113° 30′ 00′′ w
22° 17′ n, 114° 10′ e
50° 52′ 03′′ n, 4° 22′ 25′′ e
32° 02′ 43′′ n, 34° 46′ 11′′ e
48° 27′ 21′′ n, 1° 29′ 03′′ e
50° 43′ 35′′ n, 1° 36′ 53′′ e
43° 33′ 05′′ n, 7° 00′ 46′′ e
49° 47′ 17′′ n, 9° 56′ 10′′ e
52° 22′ 49′′ n, 4° 38′ 26′′ e
48° 53′ 56′′ n, 2° 05′ 38′′ e
35° 08′ 46′′ n, 90° 03′ 07′′ w
50° 35′ 27′′ n, 5° 51′ 42′′ e
49° 29′ 20′′ n, 8° 28′ 09′′ e
44° 48′ 00′′ n, 10° 20′ 00′′ e
45° 31′ n, 122° 40′ w
40° 38′ 00′′ n, 22° 57′ 00′′ e
48° 49′ 56′′ n, 2° 21′ 20′′ e
50° 22′ 17′′ n, 3° 04′ 48′′ e
43° 19′ 17′′ n, 1° 59′ 08′′ w
35° 26′ n, 139° 38′ e
8° 50′ 18′′ s, 13° 14′ 04′′ e
39° 46′ 07′′ n, 86° 09′ 29′′ w
36° 17′ 00′′ n, 6° 37′ 00′′ e
41° 17′ 55′′ s, 174° 46′ 52′′ e
46° 09′ 33′′ n, 1° 09′ 06′′ w
43° 15′ 25′′ n, 2° 55′ 24′′ w
40° 42′ 49′′ n, 73° 49′ 41′′ w
22° 34′ 22′′ n, 88° 21′ 50′′ e
49° 00′ 50′′ n, 8° 24′ 15′′ e
43° 30′ 36′′ n, 16° 26′ 24′′ e
45° 45′ 15′′ n, 4° 49′ 45′′ e
52° 08′ 00′′ n, 11° 37′ 00′′ e
25° 17′ 39′′ s, 57° 38′ 31′′ w
52° 24′ 00′′ n, 16° 55′ 00′′ e
52° 24′ 00′′ n, 13° 04′ 00′′ e
41° 18′ 30′′ n, 69° 15′ 35′′ e
43° 12′ 47′′ n, 2° 21′ 07′′ e
44° 50′ 00′′ n, 11° 37′ 00′′ e
13° 45′ 08′′ n, 100° 29′ 38′′ e
48° 50′ 46′′ n, 2° 20′ 41′′ e
49° 38′ 20′′ n, 1° 37′ 30′′ w
34° 03′ 00′′ n, 4° 58′ 59′′ w
47° 35′ 38′′ n, 1° 19′ 41′′ e
43° 33′ 00′′ n, 10° 19′ 00′′ e
9° 32′ 53′′ n, 13° 40′ 14′′ w
52° 57′ 12′′ n, 1° 08′ 51′′ w
43° 50′ 51′′ n, 18° 21′ 23′′ e
34° 55′ 48′′ s, 138° 35′ 59′′ e
50° 17′ 23′′ n, 2° 46′ 51′′ e
48° 51′ 22′′ n, 2° 21′ 20′′ e
49° 50′ 55′′ n, 3° 17′ 11′′ e
49° 52′ 00′′ n, 8° 39′ 00′′ e
33° 30′ 44′′ n, 36° 17′ 54′′ e
47° 59′ 48′′ n, 4° 05′ 47′′ w
51° 29′ 07′′ n, 3° 11′ 12′′ w
48° 51′ 57′′ n, 2° 21′ 50′′ e
44° 12′ 18′′ n, 0° 37′ 16′′ e
45° 38′ 56′′ n, 0° 09′ 39′′ e
38° 15′ 22′′ n, 85° 45′ 05′′ w
51° 02′ 18′′ n, 2° 22′ 39′′ e
44° 01′ 05′′ n, 1° 21′ 21′′ e
53° 04′ 59′′ n, 8° 48′ 00′′ e
50° 00′ 00′′ n, 8° 16′ 16′′ e
50° 44′ n, 7° 06′ e
48° 51′ 54′′ n, 2° 23′ 57′′ e
49° 24′ 39′′ n, 8° 42′ 07′′ e
51° 27′ 00′′ n, 7° 01′ 00′′ e
47° 38′ 17′′ n, 6° 51′ 46′′ e
47° 39′ 21′′ n, 2° 45′ 37′′ w
42° 42′ 03′′ n, 9° 27′ 01′′ e
51° 19′ 11′′ n, 9° 29′ 52′′ e
60° 22′ 57′′ n, 5° 20′ 41′′ e
46° 19′ 33′′ n, 0° 27′ 38′′ w
4° 16′ 04′′ s, 15° 16′ 31′′ e
48° 22′ 08′′ n, 10° 53′ 52′′ e
14° 36′ 48′′ n, 61° 03′ 52′′ w
50° 49′ n, 3° 16′ e
52° 09′ 00′′ n, 4° 29′ 00′′ e
45° 42′ 00′′ n, 9° 39′ 58′′ e
46° 59′ 34′′ n, 3° 09′ 42′′ e
47° 16′ 00′′ n, 11° 23′ 00′′ e
45° 46′ 18′′ n, 4° 51′ 17′′ e
43° 20′ 00′′ n, 11° 20′ 00′′ e
52° 38′ 03′′ n, 1° 08′ 19′′ w
57° n, 5° w
55° 35′ 00′′ n, 13° 02′ 00′′ e
50° 49′ 00′′ n, 1° 05′ 00′′ w
53° 25′ n, 14° 35′ e
40° 45′ 00′′ n, 111° 53′ 00′′ w
43° 13′ 51′′ n, 0° 04′ 21′′ e
29° 53′ 00′′ s, 31° 03′ 00′′ e
38° 34′ 31′′ n, 121° 29′ 10′′ w
21° 18′ 17′′ n, 157° 51′ 26′′ w
48° 10′ 28′′ n, 6° 27′ 04′′ e
43° 55′ 44′′ n, 2° 08′ 47′′ e
48° 50′ 46′′ n, 2° 20′ 40′′ e
43° 24′ 19′′ n, 3° 41′ 51′′ e
43° 43′ 00′′ n, 10° 24′ 00′′ e
31° 57′ s, 115° 52′ e
43° 09′ 56′′ n, 77° 36′ 58′′ w
46° 12′ 20′′ n, 5° 13′ 44′′ e
47° 00′ 00′′ n, 28° 55′ 00′′ e
53° 57′ n, 1° 05′ w
43° 31′ 54′′ s, 172° 38′ 12′′ e
34° 44′ n, 10° 46′ e
52° 37′ 42′′ n, 1° 17′ 48′′ e
25° 44′ 42′′ s, 28° 11′ 25′′ e
33° 46′ 05′′ n, 118° 11′ 44′′ w
6° 10′ 31′′ s, 106° 49′ 37′′ e
41° 18′ 30′′ n, 72° 55′ 30′′ w
47° 06′ 05′′ n, 6° 49′ 30′′ e
37° 30′ 58′′ n, 15° 03′ 58′′ e
35° 26′ 52′′ n, 139° 38′ 33′′ e
48° 51′ 37′′ n, 2° 26′ 35′′ e
45° 11′ 02′′ n, 0° 42′ 57′′ e
42° 49′ 00′′ n, 1° 39′ 00′′ w
41° 39′ 07′′ n, 4° 43′ 43′′ w
41° 55′ 36′′ n, 8° 44′ 13′′ e
50° 49′ 42′′ n, 0° 08′ 22′′ w
48° 51′ 50′′ n, 2° 21′ 42′′ e
49° 09′ 39′′ n, 5° 23′ 18′′ e
45° 45′ 31′′ n, 4° 51′ 21′′ e
49° 25′ 49′′ n, 2° 05′ 43′′ e
51° 29′ 58′′ n, 0° 08′ 00′′ w
48° 57′ 27′′ n, 4° 21′ 54′′ e
50° 46′ 00′′ n, 6° 06′ 00′′ e
39° 57′ 44′′ n, 83° 00′ 02′′ w
6° 08′ 14′′ n, 1° 12′ 45′′ e
43° 11′ 01′′ n, 3° 00′ 15′′ e
51° 28′ 00′′ n, 11° 58′ 00′′ e
50° 56′ 53′′ n, 1° 51′ 23′′ e
43° 40′ 36′′ n, 4° 37′ 40′′ e
51° 53′ 49′′ n, 8° 28′ 41′′ w
50° 43′ 30′′ n, 3° 09′ 43′′ e
48° 50′ 32′′ n, 2° 25′ 07′′ e
49° 11′ 24′′ n, 2° 06′ 36′′ w
36° 09′ 44′′ n, 86° 46′ 28′′ w
16° 14′ 30′′ n, 61° 32′ 09′′ w
20° 40′ 35′′ n, 103° 20′ 32′′ w
50° 10′ 36′′ n, 3° 14′ 08′′ e
43° 42′ 26′′ n, 1° 03′ 19′′ w
56° 08′ 59′′ n, 10° 13′ 27′′ e
44° 39′ 00′′ n, 10° 56′ 00′′ e
46° 33′ 55′′ n, 3° 20′ 00′′ e
46° 48′ 22′′ n, 7° 09′ 46′′ e
47° 48′ 09′′ n, 13° 02′ 45′′ e
46° 46′ 50′′ n, 4° 51′ 10′′ e
46° 02′ 12′′ n, 4° 04′ 08′′ e
48° 51′ 35′′ n, 2° 20′ 40′′ e
47° 47′ 55′′ n, 3° 34′ 02′′ e
52° 16′ 01′′ n, 10° 31′ 59′′ e
48° 18′ 11′′ n, 14° 17′ 26′′ e
41° 49′ n, 71° 25′ w
47° 59′ 44′′ n, 7° 51′ 08′′ e
6° 14′ 00′′ n, 75° 34′ 00′′ w
48° 51′ 29′′ n, 2° 21′ 23′′ e
48° 24′ 35′′ n, 2° 42′ 09′′ e
44° 21′ 02′′ n, 2° 34′ 30′′ e
48° 51′ 20′′ n, 2° 21′ 59′′ e
49° 55′ 20′′ n, 1° 04′ 43′′ e
58° 22′ 44′′ n, 26° 43′ 12′′ e
48° 25′ 47′′ n, 0° 05′ 31′′ e
33° 26′ 54′′ n, 112° 04′ 26′′ w
46° 48′ 37′′ n, 1° 41′ 28′′ e
51° 57′ 47′′ n, 7° 37′ 43′′ e
44° 07′ 41′′ n, 4° 04′ 54′′ e
43° 36′ 19′′ n, 2° 14′ 27′′ e
39° 34′ 00′′ n, 2° 39′ 00′′ e
31° 37′ 46′′ n, 7° 58′ 52′′ w
46° 21′ n, 72° 33′ w
47° 15′ 36′′ n, 0° 04′ 37′′ w
51° 13′ 33′′ n, 2° 55′ 10′′ e
39° 55′ 38′′ n, 32° 51′ 52′′ e
54° 54′ n, 23° 56′ e
14° 35′ n, 120° 58′ e
48° 54′ 16′′ n, 2° 18′ 23′′ e
52° 11′ 28′′ n, 2° 13′ 20′′ w
50° 06′ 21′′ n, 1° 50′ 03′′ e
46° 18′ 22′′ n, 4° 49′ 53′′ e
29° 25′ 30′′ n, 98° 29′ 38′′ w
45° 09′ 23′′ n, 10° 47′ 28′′ e
56° 27′ 51′′ n, 2° 58′ 13′′ w
41° 45′ 48′′ n, 72° 41′ 06′′ w
37° 05′ 00′′ n, 15° 17′ 00′′ e
54° 20′ 00′′ n, 10° 08′ 00′′ e
43° 51′ 00′′ n, 10° 31′ 00′′ e
44° 56′ 39′′ n, 93° 05′ 37′′ w
35° 10′ 52′′ n, 136° 54′ 23′′ e
55° 40′ 40′′ n, 12° 31′ 58′′ e
36° 43′ 15′′ n, 4° 24′ 54′′ w
48° 53′ 52′′ n, 2° 15′ 11′′ e
34° 53′ 24′′ n, 1° 19′ 12′′ w
34° 41′ 29′′ n, 135° 11′ 31′′ e
3° 25′ 16′′ n, 76° 31′ 20′′ w
45° 56′ 29′′ n, 0° 58′ 18′′ w
49° 01′ 37′′ n, 1° 09′ 05′′ e
32° 48′ 43′′ n, 34° 59′ 55′′ e
63° 25′ 00′′ n, 10° 23′ 00′′ e
50° 58′ 41′′ n, 11° 01′ 45′′ e
13° 05′ 24′′ n, 80° 16′ 12′′ e
43° 15′ 24′′ n, 79° 52′ 09′′ w
34° 09′ 48′′ n, 118° 07′ 37′′ w
44° 55′ 34′′ n, 2° 26′ 26′′ e
45° 24′ n, 71° 54′ w
22° 16′ 33′′ s, 166° 27′ 29′′ e
46° 27′ 56′′ n, 6° 50′ 56′′ e
33° 35′ 24′′ n, 130° 24′ 06′′ e
35° 06′ n, 129° 02′ e
34° 05′ 54′′ n, 118° 19′ 36′′
45° 09′ 30′′ n, 1° 31′ 55′′ e
50° 55′ n, 5° 20′ e
31° 24′ 30′′ s, 64° 11′ 02′′ w
51° 37′ 00′′ n, 3° 57′ 00′′ w
47° 03′ n, 8° 18′ e
41° 59′ 48′′ n, 21° 25′ 57′′ e
48° 32′ 26′′ n, 2° 39′ 36′′ e
49° 21′ 32′′ n, 6° 10′ 09′′ e
51° 31′ 01′′ n, 7° 27′ 00′′ e
37° 52′ 13′′ n, 122° 16′ 05′′ w
53° 47′ 31′′ n, 1° 45′ 14′′ w
41° 08′ 00′′ n, 16° 52′ 00′′ e
50° 51′ n, 4° 22′ e
51° 29′ 34′′ n, 0° 13′ 22′′ w
51° 22′ 51′′ n, 2° 21′ 37′′ w
50° 04′ 55′′ n, 8° 14′ 29′′ e
47° 14′ n, 39° 43′ e
35° 51′ 26′′ n, 139° 38′ 57′′ e
47° 37′ 23′′ n, 6° 09′ 21′′ e
48° 25′ 00′′ n, 71° 04′ 00′′ w
45° 33′ 00′′ n, 11° 33′ 00′′ e
48° 25′ 20′′ n, 123° 21′ 57′′ w
47° 25′ 00′′ n, 9° 22′ 00′′ e
36° 54′ 15′′ n, 7° 45′ 07′′ e
51° 30′ 01′′ n, 0° 11′ 27′′ w
47° 30′ 37′′ n, 6° 47′ 56′′ e
49° 42′ 09′′ n, 4° 56′ 28′′ e
9° 56′ 00′′ n, 84° 05′ 00′′ w
38° 11′ 00′′ n, 15° 33′ 00′′ e
21° 02′ n, 105° 51′ e
41° 15′ 31′′ n, 95° 56′ 15′′ w
48° 50′ 52′′ n, 2° 26′ 21′′ e
50° 43′ 00′′ n, 3° 31′ 00′′ w
45° 02′ 39′′ n, 3° 53′ 09′′ e
36° 12′ 00′′ n, 37° 09′ 36′′ e
12° 21′ 58′′ n, 1° 31′ 05′′ w
44° 26′ 54′′ n, 1° 26′ 29′′ e
48° 34′ 42′′ n, 3° 49′ 36′′ w
48° 35′ 22′′ n, 6° 30′ 06′′ e
37° 52′ 45′′ n, 4° 46′ 47′′ w
30° 19′ n, 81° 39′ w
51° 25′ 29′′ n, 6° 45′ 03′′ e
48° 55′ 25′′ n, 2° 15′ 08′′ e
48° 47′ 58′′ n, 2° 29′ 59′′ e
48° 28′ 03′′ n, 35° 02′ 24′′ e
37° 18′ 15′′ n, 121° 52′ 22′′ w
41° 19′ 39′′ n, 19° 49′ 07′′ e
50° 50′ 00′′ n, 12° 55′ 00′′ e
45° 45′ 35′′ n, 21° 13′ 48′′ e
50° 54′ 54′′ n, 1° 23′ 43′′ w
24° 40′ 57′′ n, 46° 44′ 16′′ e
38° 25′ n, 27° 08′ e
36° 09′ 00′′ n, 5° 26′ 00′′ e
43° 16′ 39′′ n, 76° 53′ 45′′ e
43° 40′ 00′′ n, 6° 55′ 00′′ e
50° 58′ 59′′ n, 11° 19′ 01′′ e
46° 04′ 00′′ n, 13° 14′ 00′′ e
48° 56′ 52′′ n, 2° 14′ 51′′ e
53° 52′ 01′′ n, 10° 42′ 00′′ e
48° 57′ 37′′ n, 2° 53′ 18′′ e
37° 32′ 27′′ n, 77° 26′ 12′′ w
0° 23′ 24′′ n, 9° 27′ 15′′ e
60° 27′ 06′′ n, 22° 16′ 01′′ e
42° 59′ 01′′ n, 81° 14′ 59′′ w
48° 54′ 39′′ n, 2° 17′ 20′′ e
56° 18′ 40,32′′ n, 43° 55′ 50,88′′ e
4° 56′ 05′′ n, 52° 19′ 49′′ w
44° 48′ 31′′ n, 0° 35′ 18′′ w
47° 09′ 44′′ n, 27° 35′ 20′′ e
43° 53′ 29′′ n, 0° 29′ 58′′ w
43° 07′ 00′′ n, 12° 23′ 00′′ e
34° 58′ 37′′ n, 138° 22′ 59′′ e
34° 31′ 01′′ n, 69° 07′ 59′′ e
48° 47′ 28′′ n, 2° 27′ 46′′ e
51° 07,52′ n, 4° 34,1′ e
2° 11′ 00′′ s, 79° 53′ 00′′ w
35° 49′ 34′′ n, 10° 38′ 24′′ e
48° 52′ 58′′ n, 2° 22′ 55′′ e
44° 33′ 34′′ n, 6° 04′ 43′′ e
51° 33′ 15′′ n, 0° 10′ 28′′ w
18° 54′ 44′′ s, 47° 31′ 18′′ e
1° 17′ 00′′ s, 36° 49′ 00′′ e
47° 16′ 50′′ n, 2° 12′ 31′′ w
45° 15′ 33′′ n, 19° 49′ 45′′ e
53° 13′ 07′′ n, 6° 34′ 02′′ e
42° 51′ 00′′ n, 2° 41′ 00′′ w
6° 21′ 36′′ n, 2° 26′ 24′′ e
48° 50′ 38′′ n, 2° 13′ 09′′ e
39° 46′ n, 84° 12′ w
55° 23′ 45,48′′ n, 10° 23′ 18,73′′ e
42° 02′ 28′′ n, 87° 41′ 24′′ w
47° 03′ 36′′ n, 0° 52′ 42′′ w
49° 22′ 54′′ n, 3° 19′ 25′′ e
55° 47′ n, 49° 10′ e
46° 40′ 31′′ n, 5° 33′ 16′′ e
34° 23′ 13′′ n, 132° 26′ 43′′ e
45° 44′ 00′′ n, 7° 19′ 00′′ e
45° 16′ 02′′ n, 1° 45′ 56′′ e
46° 20′ 27′′ n, 2° 36′ 12′′ e
51° 50′ 03′′ n, 12° 14′ 16′′ e
19° 55′ 41′′ s, 43° 56′ 31′′ w
33° 53′ 42′′ n, 5° 33′ 17′′ w
45° 19′ 38′′ n, 14° 26′ 33′′ e
51° 48′ 00′′ n, 4° 41′ 00′′ e
47° 51′ 12′′ n, 5° 20′ 02′′ e
48° 54′ 47′′ n, 2° 23′ 00′′ e
45° 46′ 41′′ n, 4° 49′ 41′′ e
45° 44′ 47′′ n, 0° 38′ 00′′ w
46° 07′ 28′′ n, 3° 25′ 42′′ e
54° 05′ 00′′ n, 12° 08′ 00′′ e
17° 51′ 50′′ s, 31° 01′ 47′′ e
56° 50′ n, 60° 35′ e
43° 27′ 36′′ n, 3° 48′ 00′′ w
51° 19′ n, 4° 56′ e
44° 38′ 52′′ n, 63° 34′ 17′′ w
59° 50′ 00′′ n, 17° 40′ 00′′ e
10° 46′ 01′′ n, 106° 40′ 01′′ e
32° 47′ 00′′ n, 79° 55′ 55′′ w
49° 14′ 00′′ n, 7° 00′ 00′′ e
48° 53′ 42′′ n, 2° 17′ 14′′ e
45° 53′ 40′′ n, 3° 06′ 48′′ e
31° 32′ 59′′ n, 74° 20′ 37′′ e
50° 44′ 46′′ n, 2° 15′ 42′′ e
49° 44′ 51′′ n, 13° 22′ 39′′ e
46° 46′ 08′′ n, 23° 35′ 26′′ e
45° 11′ 00′′ n, 9° 09′ 00′′ e
48° 46′ 19′′ n, 5° 09′ 37′′ e
32° 45′ 23′′ n, 97° 19′ 57′′ w
17° 32′ 06′′ s, 149° 34′ 11′′ w
47° 08′ 06′′ n, 7° 14′ 24′′ e
34° 41′ 11′′ n, 135° 31′ 12′′ e
39° 01′ 00′′ n, 125° 44′ 00′′ e
49° 33′ 50′′ n, 3° 37′ 28′′ e
45° 08′ 00′′ n, 10° 02′ 00′′ e
48° 48′ 05′′ n, 2° 15′ 46′′ e
45° 49′ 00′′ n, 9° 05′ 00′′ e
45° 40′ 20′′ n, 12° 14′ 32′′ e
51° 50′ 00′′ n, 5° 52′ 00′′ e
37° 41′ 20′′ n, 97° 20′ 10′′ w
46° 49′ 04′′ n, 0° 32′ 46′′ e
8° 03′ 14′′ s, 34° 52′ 51′′ w
47° 30′ n, 8° 45′ e
52° 00′ 42′′ n, 4° 21′ 25′′ e
36° 08′ n, 95° 56′ w
42° 08′ 48′′ n, 24° 45′ 03′′ e
16° 30′ 00′′ s, 68° 08′ 56′′ w
51° 32′ 00′′ n, 9° 56′ 00′′ e
50° 56′ n, 4° 02′ e
53° 44′ 40′′ n, 0° 19′ 57′′ w
49° 01′ 00′′ n, 12° 06′ 00′′ e
50° 56′ n, 3° 07′ e
44° 03′ 21′′ n, 5° 02′ 56′′ e
50° 50′ 00′′ n, 4° 18′ 00′′ e
48° 51′ 36′′ n, 2° 20′ 31′′ e
42° 39′ n, 73° 46′ w
51° 59′ 00′′ n, 5° 55′ 00′′ e
25° 02′ 15′′ n, 121° 33′ 45′′ e
48° 44′ 14′′ n, 1° 21′ 59′′ e
28° 37′ n, 77° 14′ e
51° 09′ n, 4° 08′ e
30° 18′ 00′′ n, 97° 44′ 00′′ w
35° 52′ n, 128° 36′ e
25° 58′ s, 32° 35′ e
35° 46′ 01′′ n, 5° 48′ 00′′ w
47° 05′ 30′′ n, 5° 29′ 47′′ e
33° 02′ 47′′ s, 71° 37′ 11′′ w
43° 04′ 29′′ n, 89° 23′ 04′′ w
34° 41′ 29′′ n, 135° 10′ 59′′ e
50° 51′ 00′′ n, 5° 41′ 00′′ e
35° 10′ 49′′ n, 136° 54′ 23′′ e
9° 02′ n, 38° 44′ e
50° 21′ 00′′ n, 7° 36′ 00′′ e
43° 22′ 00′′ n, 5° 50′ 00′′ w
43° 37′ 00′′ n, 13° 31′ 00′′ e
45° 52′ 49′′ s, 170° 30′ 13′′ e
11° 52′ n, 15° 36′ w
49° 24′ 54′′ n, 2° 49′ 23′′ e
51° 26′ 17′′ n, 5° 28′ 31′′ e
5° 49′ 25′′ n, 55° 10′ 11′′ w
61° 29′ 53′′ n, 23° 45′ 36′′ e
46° 13′ 40′′ n, 7° 21′ 31′′ e
25° 40′ 56′′ n, 100° 18′ 40′′ w
48° 50′ 12′′ n, 2° 28′ 57′′ e
41° 39′ 10′′ n, 83° 32′ 16′′ w
44° 03′ 00′′ n, 12° 33′ 58′′ e
35° 28′ 56′′ n, 97° 32′ 07′′ w
35° 33′ n, 6° 10′ e
48° 00′ n, 37° 48′ e
50° 51′ n, 2° 53′ e
48° 27′ 23′′ n, 2° 02′ 56′′ w
54° 54′ 22′′ n, 1° 22′ 53′′ w
18° 27′ n, 66° 04′ w
58° 58′ 10′′ n, 5° 43′ 56′′ e
52° 24′ 29′′ n, 1° 30′ 38′′ w
46° 04′ 00′′ n, 11° 07′ 00′′ e
46° 30′ 00′′ n, 11° 21′ 00′′ e
49° 45′ 35′′ n, 6° 38′ 38′′ e
48° 48′ 47′′ n, 2° 14′ 19′′ e
50° 49′ 27′′ n, 4° 20′ 45′′ e
48° 49′ 26′′ n, 2° 12′ 42′′ e
52° 14′ 14′′ n, 0° 53′ 46′′ w
34° 41′ 12′′ n, 1° 54′ 41′′ w
43° 03′ n, 141° 21′ e
45° 12′ 26′′ n, 5° 44′ 28′′ e
11° 40′ 11′′ s, 27° 29′ 00′′ e
43° 56′ 00′′ n, 10° 55′ 00′′ e
35° 11′ 38′′ n, 0° 38′ 29′′ w
40° 48′ 33′′ n, 73° 56′ 54′′ w
44° 14′ 00′′ n, 12° 03′ 00′′ e
52° 35′ 05′′ n, 2° 07′ 40′′ w
50° 22′ 12′′ n, 4° 08′ 31′′ w
44° 42′ 00′′ n, 10° 38′ 00′′ e
51° 14′ 00′′ n, 22° 34′ 00′′ e
44° 54′ 58′′ n, 0° 14′ 34′′ w
40° 12′ 00′′ n, 8° 25′ 00′′ w
46° 57′ 06′′ n, 4° 17′ 58′′ e
43° 38′ 47′′ n, 0° 35′ 08′′ e
16° 02′ n, 16° 30′ w
44° 25′ 00′′ n, 12° 12′ 00′′ e
41° 32′ 54′′ n, 2° 06′ 27′′ e
48° 51′ 18′′ n, 2° 21′ 24′′ e
35° 10′ 01′′ n, 33° 21′ 00′′ e
42° 20′ 27′′ n, 3° 41′ 59′′ w
50° 51′ n, 4° 19′ e
38° 20′ 43′′ n, 0° 28′ 59′′ w
35° 18′ 29,86′′ s, 149° 07′ 27,8′′ e
45° 59′ 25′′ n, 4° 43′ 13′′ e
48° 40′ 30′′ n, 5° 53′ 30′′ e
50° 31′ n, 5° 14′ e
49° 03′ 06′′ n, 2° 06′ 06′′ e
36° 29′ 00′′ n, 2° 50′ 00′′ e
25° 27′ 19′′ s, 49° 15′ 46′′ w
50° 15′ 54′′ n, 19° 01′ 26′′ e
46° 15′ 18′′ n, 20° 08′ 42′′ e
35° 52′ n, 139° 39′ e
43° 28′ 54′′ n, 1° 33′ 22′′ w
6° 29′ 50′′ n, 2° 36′ 18′′ e
32° 41′ n, 51° 41′ e
42° 06′ 45′′ n, 72° 32′ 51′′ w
36° 46′ 54′′ n, 119° 47′ 32′′ w
39° 13′ n, 9° 07′ e
51° 42′ 00′′ n, 5° 19′ 00′′ e
48° 17′ 06′′ n, 6° 57′ 00′′ e
43° 22′ 17′′ n, 8° 23′ 46′′ w
49° 27′ 45′′ n, 1° 05′ 14′′ e
47° 15′ 09′′ n, 122° 26′ 51′′
53° 12′ 00′′ n, 5° 47′ 00′′ e
39° 44′ 54′′ n, 75° 33′ 05′′ w
51° 35′ 00′′ n, 4° 47′ 00′′ e
37° 27′ 50′′ n, 126° 38′ 55′′ e
21° 25′ 21′′ n, 39° 49′ 34′′ e
48° 48′ 28′′ n, 2° 22′ 29′′ e
24° 51′ n, 67° 00′ e
38° 04′ 48′′ n, 46° 17′ 31′′ e
50° 16′ 39′′ n, 3° 58′ 24′′ e
48° 43′ 57′′ n, 2° 26′ 59′′ e
46° 48′ 00′′ n, 71° 11′ 00′′ w
52° 39′ 55′′ n, 8° 37′ 26′′ w
36° 32′ 00′′ n, 6° 17′ 00′′ w
50° 37′ 48′′ n, 3° 46′ 50′′ e
34° 10′ 15′′ n, 118° 15′ 00′′
48° 55′ 03′′ n, 2° 16′ 06′′ e
41° 04′ 23′′ n, 81° 31′ 04′′ w
36° 50′ 49′′ n, 76° 17′ 07′′ w
46° 00′ 24′′ n, 8° 57′ 05′′ e
45° 46′ 07′′ n, 4° 50′ 01′′ e
51° 27′ 15′′ n, 0° 58′ 23′′ w
55° 50′ 44′′ n, 4° 25′ 03′′ w
43° 32′ 00′′ n, 5° 42′ 00′′ w
42° 57′ 40′′ n, 85° 39′ 50′′ w
48° 58′ 11′′ n, 2° 18′ 29′′ e
51° 20′ 00′′ n, 6° 34′ 00′′ e
49° 06′ 52′′ n, 1° 05′ 30′′ w
44° 33′ 29′′ n, 4° 45′ 03′′ e
48° 54′ 08′′ n, 2° 28′ 58′′ e
51° 32′ 38′′ n, 0° 06′ 10′′ w""".split("\n")

NON_CAUSE_OF_DEATH = """France
Espagne
pierre ii de courtenay
Argentine
Nationalité française
Allemagne
États-Unis
République démocratique du Congo
Brésil
Italie
Suisse
Royaume-Uni de Grande-Bretagne et d'Irlande
Canada
Algérie
Royaume-Uni
Abbaye d'Egmond
Achab (roi)
Belgique
Samarie (ville ancienne)
Afghanistan
Malawi
israëlite
Christianisme
République du Congo
Mexique
Côte d'Ivoire
Jérusalem
Julius Avitus
Huguenot
Perdiccas II de Macédoine
Kenya
Hâroun ar-Rachîd
Bataille d'Hastings
Corée pendant la colonisation japonaise
Nigeria
Tchécoslovaquie
Archélaos Ier de Macédoine
Royaume d'Angleterre
Berbères
Maroc
Cimetière de Cameroun
Cimetière de la Recoleta
Grec ancien
Portugal
Dioclétien
Tirtza (ville)
Cameroun
Camp de concentration
Grandes Purges
Blitz
Schutzstaffel
Marches de la mort (Shoah)
Qunu
Cuba
Chapelle Saint-Georges de Windsor
Marcus Valerius Messalla Barbatus
Cimetière du Montparnasse
Cimetière anglais de Rome
Qom
Philippe (satrape)
Tombe de Philippe II de Macédoine
Tombeau de David
République de Genève
Église Notre-Dame-de-Bonsecours de Nancy
Balle (projectile)
Israël antique
Église de Riddarholmen
Questeur (Rome antique)
Coup d'État de 1987 au Burkina Faso
Fédération nationale catholique
Affan ibn Abi al-'As
Flèche (arme)
Sigebert III
Savannakhet
Sigurd Syr
Cimetière de Recoleta
Yougoslavie
Séleucie de Piérie
Vaudémont
Église de Waltham Abbey
FE de las JONS
Alphonse III de Portugal
Pakistan
Église Saint-Pantaléon de Cologne
Loeches
Mausolée de Kwame Nkrumah
Irak
Cathédrale Saint-Guy de Prague
Baudouin V de Hainaut
Assassinat d'Ismaël Haniyeh
Chapelles des Médicis
Monastère Donskoï
NSDAP
Colombie
Bataille d'Azincourt
Ferdinand II d'Aragon
Antipater (général)
Middelbourg
Marrakech
Capitole de l'État de Louisiane
Abbaye de Varnhem
Abbaye de Rijnsburg
Robert le Fort
Sisygambis
Crypte des Capucins
Repton
en:Zorah
Aldoin
Ptolémée Ier
Fièvre
Æthelred (roi du Wessex)
Albanie
Pons de Tripoli
Cimetière de la Chacarita
Prieuré d'Inchmahome
Empire coréen
Léovigild
Citadelle La Ferrière
Soissons
Nuit des Longs Couteaux
Royaume d'Espagne
Soumaâ du Khroub
Darius Ier
Cimetière de Mingorrubio
Pozuelo de Alarcón
Mahendra Bir Bikram Shah
Oahu
République populaire de Chine
Louis Becquey
Liste des comtes du Poher
Blythburgh
Séleucos Ier
Slovaquie
Démarate de Corinthe
Ithobaal Ier
en:Belevi Mausoleum
Yeoju
Hunéric
2
Syagrius
Théodoric le Grand
Marc Aurèle
Léon III d'Arménie
Abbaye de Vreta
Cathédrale Saint-Étienne de Vienne
Valentinien Ier
Mausolée d'Hadrien
Raoul Ier de Coucy
Reine Pédauque
Clovis Ier
Université de Salamanque
Journaliste
Tourbet El Bey
Sargon II
RPG-2
Al-Muʿtas̩im (Abbasside)
Jean VI Cantacuzène
Wulfrun
Cathédrale de la Almudena
Clovis II
Bataille de Stamford Bridge
826
Robert III de La Marck
Bordeaux
Université de Buenos Aires
Gibet de Montfaucon
Sri Lanka
Palestine (État)
Australie
Sabins
Fosse commune
Namibie
Dagobert Ier
Strasbourg
Hussein ben Ali (chérif de La Mecque)
Thành Thái
Nicolas Ducos
Mithridate VI
Kenchela
Église des Saints-Apôtres (Constantinople)
Pampliega
Colegio Nacional de Buenos Aires
Tombeaux saadiens
Basilique San Pietro in Ciel d'Oro
Hiempsal II
Pharnace Ier
Rædwald
Salta
Achaz
Elbeuf
Rhémétalcès Ier
Venceslas de Saxe
Javelot
Militaire
Gamla Uppsala
Wittiza
Goswinthe
Harald le Vieux
Ville de David
Jézabel
José Gabriel Condorcanqui
Personnalité politique
Louis Paul Sevaistre
Liuva Ier
Église de Jésus-Christ des saints des derniers jours
Abijam
Antiochos II
Parti radical-démocratique
Thiudimir
Parti ouvrier unifié polonais
Démétrios II Nicator
Iran
Pont-à-Mousson
Belfast
Église Saint-Louis-en-l'Île
Joram (Juda)
Alexandre le Grand
Cathédrale d'Uppsala
Valence (Drôme)
Cité de David
Occultation (islam)
en:Willesden Jewish Cemetery
Cimetière du Djellaz
Stettin
Chindaswinthe
Agni (roi)
Guatemala
Vranov (district de Brno-Campagne)
Assassinats de George Moscone et d'Harvey Milk
Comores (Pays)
Bataille de Messines (1917)
Engaku-ji (bouddhisme)
Ragnar Lodbrok
Incident du 15 mai
Eurydice (épouse d'Amyntas III)
Constance II
en:Ügyek
Royaume d'Imerina
Bangladesh
Al-Mahdi (Abbasside)
Maréchal de camp
Thothorsès
Teutberge d'Arles
Dácil
Epitácio Pessoa
Parti socialiste ouvrier espagnol
Oswiu
Tamoul
Empire allemand
Bikfaya
Allemand
Ézéchias
Caius Bruttius Praesens Laberius Maximus
Radbod Ier de Frise
Antiochos III
Ismaïl Ier de Grenade
Villette (Yvelines)
Persée (roi)
Inde
Mauritanie
Eysteinn
138 av. J.-C.
Henri II d'Orléans-Longueville
Parti républicain (États-Unis)
Perdiccas III de Macédoine
Aldea del Cano
Josias
Francs
Coup d'État de mai (Serbie)
Ghana
Pszczyna
Maurice (pays)
Amyntas III
Parti de l'Ordre
Cimetière du Centre
Djibouti
Antiochos X
Felipe Pardo y Aliaga
Tamatoa IV
Lhassa
Espagnols
pt:Valaravano
Adils
en:Hervor
Blót
premier
Tir national
Russes
Cassandre (roi)
Rwanda
Louis XIV
Dyggve
Brandonnet
Autriche
Yngvi et Alf
Islam
Bom Conselho
Premier avocat général
Amyntas II (roi de Macédoine)
Étienne-Thomas de Bosnie
Togo
Haïti
Empire romain
Vice-royauté du Río de la Plata
Madrid
Autigny-la-Tour
Ptolémée IX
Bohémond IV d'Antioche
Biélorussie
Drones
Joas (Israël)
Saxons de Transylvanie
Nicomède Ier
Aligern
Andromaque (fils d'Alexandre)
La Roche-sur-Yon
Gento
Abbaye d'Abingdon
Tulga
Tolède
Bulgarie
Rhescuporis Ier
Joachaz (Israël)
Démétrios II (roi séleucide)
Jéroboam II
Pierre runique
Roumain
Vanlandi
Premier ministre d'Haïti
Somalie
Ben Aknoun
Nongoma
Hébron
Mvog-Ada
Sarde
Conakry
Cimetière marin de Saint-Tropez
Derby (Royaume-Uni)
Lomé
Université Chulalongkorn
Séleucos II
Fidji
Angola
Arabie saoudite
Séleucos IV
Birmanie
Guinée
Zambie
Khmers rouges
Bosniaques
El Calafate
3
Amyntas III de Macédoine
Nivelon Ier de Pierrefonds
Lestko
Lisbonne
Liste des principaux accidents ferroviaires
Industrie
Jéhu
Gondioc
Union des républiques socialistes soviétiques
Boris Godounov
Philippines
Hilaliens
Tchad
République centrafricaine
Aéropos II de Macédoine
Martin de Córdova et Velasco
RKP (b)
Birendra Bir Bikram Shah Dev
Cimetière
Niger
Tibétains
Bhoutan
Jéroboam Ier
École impériale du Service de santé militaire de Strasbourg
Ostrogoths
Union républicaine et démocratique
Nyírbátor
Olinda
Cathédrale Notre-Dame-de-l'Assomption de Mata Utu
Le Vigan (Gard)
Kirghizistan
Liste des rois d'Est-Anglie
Britanniques
Culhuacan
Parti républicain-démocrate
Hébreu
Sans étiquette
Menahem (Roi d'Israël)
Persépolis
Ptolémée (roi d'Épire)
Cote d'ivoire
Grèce
Iloilo (ville)
Kalâa des Beni Abbès
Jean II de Courtejoye
en:Nabû-mukin-apli
Mali
Le Cannet
es:Rollaug
Religion grecque antique
Vienne (Isère)
Kribi
Tang Zhaozong
Uruguay
Aho Houegbadja
Crotone
Nikki (commune)
en:Pirathon
Tribu de Zabulon
Gotique
Takalédougou
Saint-Gervais-d'Auvergne
Aeropos II de Macédoine
Pandémie de Covid-19 en Papouasie-Nouvelle-Guinée
Rassemblement du peuple français
Guangdong
Saint-Laurent-en-Royans
La Réole
Alexandre Ier de Macédoine
Hangeul
Portomarín
Finlande
Action démocratique (Venezuela)
Yaoundé
Thoros Ier d'Arménie
Guanches
Revolutionäre Zellen
Neuilly-sur-Seine
Cimetière de Montmartre
Al-Mutawakkil (Abbasside)
Manassé (Juda)
Noble
Colmar""".split("\n")

GOOD_CAUSE_OF_DEATH = """
Assassinat
Infarctus du myocarde
Cancer
Tué à l'ennemi
Crise cardiaque
Suicide
Accident vasculaire cérébral
Cancer du poumon
Pneumonie
Exécution par arme à feu
Accident de la route
Pneumonie aiguë
Pendaison
Maladie à coronavirus 2019
Hémorragie cérébrale
Maladie
Insuffisance cardiaque chez l'humain
Accident aérien
Apoplexie
Arrêt cardiorespiratoire
Leucémie
Cancer de la prostate
Décapitation
Covid-19
wikt:guillotiné
Guillotine
Cancer du pancréas
Tumeur du cerveau
Maladie de Parkinson
Arrêt cardiaque
Cancer de l'estomac
Tuberculose
Choléra
Insuffisance cardiaque
Peine de mort
Accident d'avion
Maladie d'Alzheimer
Embolie pulmonaire
Infarctus
Cancer du côlon
Cancer de l'œsophage
Typhus
Insuffisance rénale
Noyade
Exécution sommaire
Blessure par balle
Cancer du cerveau
Cancer du foie
Accident de l'avion présidentiel polonais à Smolensk
Cancer du rein
Accident
Cancer colorectal
Hémorragie
Fibrose pulmonaire
Maladie cardiovasculaire
Anévrisme
Naturelle
Angine de poitrine
Peste
Homicide
Empoisonnement
Strangulation
Dysenterie
Maladie de Waldenström
Chute (traumatologie)
Mort subite (médecine)
Déportation
Hémorragie intracérébrale
Thrombose
Lèpre
Goutte (maladie)
Assassinat politique
Attentat
Mort pour la France
COVID-19
Cancer du sein
Accident de voiture
Grippe de 1918
Cancer de la gorge
Coronavirus
Grippe
Bombardement
Gangrène
Anévrisme de l'aorte abdominale
Sepsis
Insuffisance rénale aiguë
Variole
Fibrillation ventriculaire
Cancer des voies aérodigestives supérieures
Insuffisance respiratoire
Mort naturelle
Nécropole royale de la basilique de Saint-Denis
Paludisme
Septicémie
Cirrhose
Poumon
Cimetière de Passy
Asphyxie
Cimetière du Père-Lachaise
Pierre II de Courtenay
Pybba
Mort au combat
Empire russe
Israëlite
Amylose (maladie)
wikt:Guillotiné
Malaise cardiaque
Accident de l'hélicoptère d'Ebrahim Raïssi
Cancer de la vessie
Cancer de la bouche
Cyriacus Buyruk Khan
Cancer de la thyroïde
Royaume de France
Varsovie
Russe
Abbaye d'Alvastra
Étienne-Ostoïa
Néphropathie
Magnicide
Sclérose latérale amyotrophique
Emphysème pulmonaire
Cimetière monumental de Rouen
Cancer du colon
Œdème aigu du poumon
Grippe espagnole
Cancer du col utérin
Abcès
Épiglottite
Pleurésie
Transposition des gros vaisseaux
Glioblastome multiforme
Assassinat de Sadi Carnot
Assassinat de Patrice Lumumba
Intoxication médicamenteuse
Guillotiné
Congestion (médecine)
Œdème
Thrombose coronaire
Insuffisance rénale chronique (humain)
Cancer (maladie)
Mélanome
Fièvre typhoïde
Cathédrale Saint-Pierre d'Angoulême
Meurtre
Décapitation dans l'islam
Diarrhée du voyageur
Assassinat de Jean-Jacques Dessalines
Hépatite
Neuropathie
Athérosclérose
Syphilis
Choc septique
Cancer de la langue
Assassinat de Jovenel Moïse
Assassinat d'Yitzhak Rabin
Assassinat de Laurent-Désiré Kabila
Assassinat de Mohamed Boudiaf
Assassinat d'Alexandre Ier de Yougoslavie
Bronchopneumopathie chronique obstructive
Asthme
Exécution extrajudiciaire
Cancer du larynx
Naufrage
Hanged, drawn and quartered
Arrêt cardio-circulatoire
Assassinat d'Olof Palme
Infarctus cérébral
Hémorragie digestive
Staphylococcus
Pancréatite
Assassinat de Luis Carrero Blanco
Leucémie aiguë myéloblastique
Euthanasie volontaire
Assassinat de Talaat Pacha
Syndrome de défaillance multiviscérale
wikt:mort naturelle
Aide au suicide
Tumeur au cerveau
Anémie
Rage (maladie)
Maladie cardio-vasculaire
Légionellose
Cholangiocarcinome
Pandémie de Covid-19
Diabète sucré
Appendicite
Carcinome hépatocellulaire
Rupture d’anévrisme
Liposarcome
Actinomycose
Parti catholique
Septimanie
Fibrose pulmonaire idiopathique
Traumatisme contondant
Covid 19
Alcoolisme
Maladie à corps de Lewy
Vieillesse
Peste noire
Exécution
Urémie
Cancer de la peau
Diabète
Brûlure
Malaria
Cancer bronchique à petites cellules
Intoxication
Suicide par pendaison
Assassiné
Embolie
Glioblastome
Cancer des poumons
Injection létale
Crise d'épilepsie
Péritonite
Cancer des os
Crash aérien
Peste bubonique
Grève de la faim
Carcinome à cellules de Merkel
Longue maladie
Insuffisance rénale chronique
Attaque d'apoplexie
Rhumatisme articulaire aigu
Accident ferroviaire
Opération chirurgicale
Lymphome
Accident de circulation
Maladie de Charcot
Pancréatite chronique
Condamnation à mort
Épuisement
Infection bactérienne
Myélome multiple
Fusillade
Apnée
Lynchage
Agression
Accident d'un Tupolev Tu-154 russe en 2016
Chambre à gaz
Ulcère gastroduodénal
Néphrite (médecine)
Leucémie aiguë
Explosion
Aktion T4
Torture
""".split("\n")