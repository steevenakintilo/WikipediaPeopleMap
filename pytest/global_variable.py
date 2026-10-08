"""Global variable file"""
PAGE_URL = "http://localhost:5173/"

# (id du bouton, libellé affiché, route vers laquelle il mène)
HOME_BUTTONS = [
    ("WorldMapPageButton", "Explorer la Map", "/WorldMap"),
    ("StatisticsPageButton", "Statistiques détaillées", "/Statistics"),
    ("OtherStatisticsPageButton", "Autres statistiques", "/OtherStatistics"),
    ("QjisMapPageButton", "Carte pour QGIS", "/Qjis"),
    ("GamePageButton", "Jeux", "/WikiGames"),
    ("AboutPageButton", "À propos", "/About"),
]

LIST_OF_PAGE_BUTTON_ID = [button[0] for button in HOME_BUTTONS]
LIST_OF_PAGE_BUTTON_NAME = [button[1] for button in HOME_BUTTONS]

HOME_TITLE = "Wikipedia People Map - La carte des personnes de Wikipédia"
