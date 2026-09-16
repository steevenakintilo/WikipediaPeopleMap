from django.db import models

# Create your models here.

from django.db import models


class WikipediaUser(models.Model):
    """Model representing a person/personality from Wikipedia."""

    # ─────────────────────────────────────────────
    # Wikipedia information
    # ─────────────────────────────────────────────

    page_name = models.CharField(max_length=300, unique=True)
    page_url = models.URLField(max_length=500)
    picture_url = models.URLField(max_length=500, blank=True, null=True)

    first_name = models.CharField(max_length=100, blank=True, null=True)
    first_name_standard = models.CharField(max_length=100, blank=True, null=True)

    last_name = models.CharField(max_length=100, blank=True, null=True)
    last_name_standard = models.CharField(max_length=100, blank=True, null=True)

    job = models.CharField(max_length=300, blank=True, null=True)

    # ─────────────────────────────────────────────
    # Birth information
    # ─────────────────────────────────────────────

    town_birth_place = models.CharField(max_length=300, blank=True, null=True)
    town_birth_place_href = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    birth_town_localisation = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    country_birth_place = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    time_period_of_birth = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    continent_of_birth = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    region_of_birth = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    birth_date = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    birth_year = models.IntegerField(
        blank=True,
        null=True,
    )

    birth_month = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    birth_day = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    birth_month_day = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Death information
    # ─────────────────────────────────────────────

    town_death_place = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    town_death_place_href = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    town_death_localisation = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    country_death_place = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    continent_of_death = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    region_of_death = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    death_date = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    death_year = models.CharField(
        blank=True,
        null=True,
    )

    death_month = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    death_day = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    death_month_day = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Birth / death comparisons
    # ─────────────────────────────────────────────

    born_and_died_in_the_same_town = models.CharField(
    max_length=20,
    default="False"
    )

    born_and_died_in_the_same_country = models.CharField(
        max_length=20,
        default="False"
    )

    born_and_died_in_the_same_continent = models.CharField(
        max_length=20,
        default="False"
    )

    born_and_died_in_the_same_day = models.CharField(
            max_length=20,
            default="False"
    )
        
    born_and_died_in_the_same_region = models.CharField(
        max_length=20,
        default="False"
    )
    
    born_before_christ = models.CharField(
        max_length=20,
        default="False"
    )

    died_before_christ = models.CharField(
        max_length=20,
        default="False"
    )

    born_and_died_before_christ = models.CharField(
        max_length=20,
        default="False"
    )

    born_and_died_after_christ = models.CharField(
        max_length=20,
        default="False"
    )

    born_before_christ_and_died_after_christ = models.CharField(
        max_length=20,
        default="False"
    )

    age = models.IntegerField(
        blank=True,
        null=True
    )

    is_alive = models.BooleanField(
        default=True
    )

    # ─────────────────────────────────────────────
    # Personal information
    # ─────────────────────────────────────────────

    gender = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Ranking
    # ─────────────────────────────────────────────

    power_ranking = models.IntegerField(
        blank=True,
        null=True
    )

    position = models.IntegerField(
        blank=True,
        null=True
    )

    position_percentage = models.FloatField(
        blank=True,
        null=True
    )

    grade_over_20 = models.FloatField(
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Wikipedia page analysis
    # ─────────────────────────────────────────────

    first_char_of_the_page = models.CharField(
        max_length=1,
        blank=True,
        null=True
    )

    wikipedia_page_lenght = models.IntegerField(
        default=0
    )

    all_links_of_a_page = models.JSONField(
        default=list,
        blank=True
    )

    number_of_links = models.IntegerField(
        default=0
    )

    
    all_links_of_a_page = models.JSONField(
        default=list,
        blank=True
    )

    number_of_user_who_have_linked_this_user = models.IntegerField(default=0)
    
    list_of_page_name_linked_sorted = models.JSONField(
        default=list,
        blank=True
    )
        
    number_of_friends = models.IntegerField(default=0)
        
    list_of_friend_of_user = models.JSONField(
        default=list,
        blank=True
    )
    
    preciseness_level = models.IntegerField(
        blank=True,
        null=True
    )

    list_of_unpreciseness_data = models.JSONField(
        default=list,
        blank=True
    )

    # ─────────────────────────────────────────────
    # Country emojis
    # ─────────────────────────────────────────────

    country_birth_place_emoji = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    country_death_place_emoji = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Metadata
    # ─────────────────────────────────────────────

    is_updated = models.BooleanField(
        default=False
    )

    number_of_update = models.IntegerField(
        default=0
    )

    page_lenght = models.IntegerField(
        default=0
    )

    number_of_word_in_page_name = models.IntegerField(
        default=0
    )
    # created_at = models.DateTimeField(
    #     auto_now_add=True
    # )

    # updated_at = models.DateTimeField(
    #     auto_now=True
    # )

class WikipediaDetailedStat(models.Model):
    """Model representing a person/personality from Wikipedia."""

    # ─────────────────────────────────────────────
    # Wikipedia information
    # ─────────────────────────────────────────────

    page_name = models.CharField(max_length=300, unique=True)
    picture_url = models.URLField(max_length=500, blank=True, null=True)

    first_name = models.CharField(max_length=100, blank=True, null=True)
    first_name_standard = models.CharField(max_length=100, blank=True, null=True)

    last_name = models.CharField(max_length=100, blank=True, null=True)
    last_name_standard = models.CharField(max_length=100, blank=True, null=True)

    job = models.CharField(max_length=300, blank=True, null=True)

    # ─────────────────────────────────────────────
    # Birth information
    # ─────────────────────────────────────────────

    town_birth_place = models.CharField(max_length=300, blank=True, null=True)
    town_birth_place_href = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    birth_town_localisation = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    country_birth_place = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    time_period_of_birth = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    continent_of_birth = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    region_of_birth = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    birth_date = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    birth_year = models.IntegerField(
        blank=True,
        null=True,
    )

    birth_month = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    birth_day = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    birth_month_day = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Death information
    # ─────────────────────────────────────────────

    town_death_place = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    town_death_place_href = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    town_death_localisation = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    country_death_place = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    continent_of_death = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    region_of_death = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    death_date = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    death_year = models.CharField(
        blank=True,
        null=True,
    )

    death_month = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    death_day = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    death_month_day = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Birth / death comparisons
    # ─────────────────────────────────────────────

    born_and_died_in_the_same_town = models.CharField(
    max_length=20,
    default="False"
    )

    born_and_died_in_the_same_country = models.CharField(
        max_length=20,
        default="False"
    )

    born_and_died_in_the_same_continent = models.CharField(
        max_length=20,
        default="False"
    )

    born_and_died_in_the_same_day = models.CharField(
            max_length=20,
            default="False"
    )
        
    born_and_died_in_the_same_region = models.CharField(
        max_length=20,
        default="False"
    )
    
    born_before_christ = models.CharField(
        max_length=20,
        default="False"
    )

    died_before_christ = models.CharField(
        max_length=20,
        default="False"
    )

    born_and_died_before_christ = models.CharField(
        max_length=20,
        default="False"
    )

    born_and_died_after_christ = models.CharField(
        max_length=20,
        default="False"
    )

    born_before_christ_and_died_after_christ = models.CharField(
        max_length=20,
        default="False"
    )

    age = models.IntegerField(
        blank=True,
        null=True
    )

    is_alive = models.BooleanField(
        default=True
    )

    # ─────────────────────────────────────────────
    # Personal information
    # ─────────────────────────────────────────────

    gender = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Ranking
    # ─────────────────────────────────────────────

    power_ranking = models.IntegerField(
        blank=True,
        null=True
    )

    position = models.IntegerField(
        blank=True,
        null=True
    )

    position_percentage = models.FloatField(
        blank=True,
        null=True
    )

    grade_over_20 = models.FloatField(
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Wikipedia page analysis
    # ─────────────────────────────────────────────

    first_char_of_the_page = models.CharField(
        max_length=1,
        blank=True,
        null=True
    )

    wikipedia_page_lenght = models.IntegerField(
        default=0
    )

    all_links_of_a_page = models.JSONField(
        default=list,
        blank=True
    )

    number_of_links = models.IntegerField(
        default=0
    )
    preciseness_level = models.IntegerField(
        blank=True,
        null=True
    )

    list_of_unpreciseness_data = models.JSONField(
        default=list,
        blank=True
    )

    # ─────────────────────────────────────────────
    # Country emojis
    # ─────────────────────────────────────────────

    country_birth_place_emoji = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    country_death_place_emoji = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    # ─────────────────────────────────────────────
    # Metadata
    # ─────────────────────────────────────────────

    is_updated = models.BooleanField(
        default=False
    )

    number_of_update = models.IntegerField(
        default=0
    )
        
    # created_at = models.DateTimeField(
    #     auto_now_add=True
    # )

    # updated_at = models.DateTimeField(
    #     auto_now=True
    # )
