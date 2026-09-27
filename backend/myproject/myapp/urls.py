from django.urls import path
from .views_folder import advanced_searched_for_user_view
from .views_folder import advanced_search_for_statistics_view
from .views_folder import qjis_map_view
from .views_folder import calc_score_of_variable_view
from .views_folder import basic_user_view
from .views_folder import database_view
from .views_folder import display_user_info_view

urlpatterns = [
    path("add_a_wikipedia_user_to_the_database",database_view.add_a_wikipedia_user_to_the_database),
    path("add_a_wikipedia_user_to_the_database_unique_town",database_view.add_a_wikipedia_user_to_the_database_unique_town),
    path("display_user_info/<str:username>",display_user_info_view.display_user_info),
    path("display_chunck_of_user_info/<int:chunk_nb>/",basic_user_view.display_chunck_of_user_info),
    path("display_chunck_of_user_info_advanced_search_qjis",qjis_map_view.display_chunck_user_birth_town_localisation_qjis),
    path("display_chunck_of_user_info_advanced_search/<int:chunk_nb>/",advanced_searched_for_user_view.display_chunck_of_user_info_advanced_search),
    path("get_advanced_statistics",advanced_search_for_statistics_view.get_advanced_statistics),
    path("calc_score_of_all_variable",calc_score_of_variable_view.calc_score_of_all_variable),
    path("update_all_wikipedia_user",database_view.update_all_wikipedia_user),
    path("calc_gender_ratio_of_all_country",calc_score_of_variable_view.calc_gender_ratio_of_all_country)
]
