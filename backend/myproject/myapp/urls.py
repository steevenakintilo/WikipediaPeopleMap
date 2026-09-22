from django.urls import path
from . import views
from . import advanced_searched_for_user_view
from . import advanced_search_for_statistics_view

urlpatterns = [
    path('hi/', views.hi, name='members'),
    path("add_a_wikipedia_user_to_the_database",views.add_a_wikipedia_user_to_the_database),
    path("add_a_wikipedia_user_to_the_database_unique_town",views.add_a_wikipedia_user_to_the_database_unique_town),
    path("display_user_info/<str:username>",views.display_user_info),
    path("display_chunck_of_user_info/<int:chunk_nb>/",views.display_chunck_of_user_info),
    path("display_chunck_of_user_info_advanced_search_qjis/<int:chunk_nb>/",views.display_chunck_user_birth_town_localisation_qjis),
    path("display_chunck_of_user_info_advanced_search/<int:chunk_nb>/",advanced_searched_for_user_view.display_chunck_of_user_info_advanced_search),
    path("get_advanced_statistics",advanced_search_for_statistics_view.get_advanced_statistics),

]



