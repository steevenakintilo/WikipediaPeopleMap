from collections import Counter
from unidecode import unidecode
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django_ratelimit.decorators import ratelimit

from myapp.models import WikipediaUser , WikipediaUserUniqueTown

from random import randint
from random import sample
from django.db.models import OuterRef, Subquery

from ..global_variable import *
from ..utility_function  import *


import ast
import os
import json
import csv

@ratelimit(key='ip', rate='30/15m', block=False)
def display_chunck_of_user_info(request,chunk_nb=0):
    """Display chunck (10000 users) of user info"""
    if getattr(request, 'limited', False):
        return JsonResponse(
            {
                "error": "too_many_requests",
                "message": "Trop de requêtes. Veuillez patienter quelques instants."
            },
            status=429
        )

    if request.method != "GET":
        return HttpResponse(f"Error!", status=404)

    all_user_obj = WikipediaUser.objects.all().order_by("position").filter(position__gte=0)

    #all_user_obj = WikipediaUser.objects.filter(number_of_user_who_have_linked_this_user=0,position__gte=0,position__lte=35000).order_by("position")
    
    
    length = all_user_obj.count()
    
    random_number_list = []
    if chunk_nb == 999999999:
        random_number = randint(0,NUMBER_OF_USER-501)
        all_user_obj = WikipediaUser.objects.filter(position__gte=random_number-500,position__lte=random_number)
        chunk_nb = 0
    #print(random_number)
    list_of_all_user_data =  []
    nb = NUMBER_OF_USERS_TO_SEARCH
    index_start = (chunk_nb * nb)
    
    index_end = (chunk_nb + 1) * nb



    tototo = 0
    list_of_localisation = []
    for user_obj in all_user_obj[index_start:index_end]:
        try:
            # if user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined":
            #     continue

            # if dms_to_decimal(user_obj.birth_town_localisation) in list_of_localisation:
            #     continue
            
            list_of_localisation.append(dms_to_decimal(user_obj.birth_town_localisation,user_obj.page_name))
            if len(user_obj.page_name) > 35:
                page_name_shorter = user_obj.page_name[0:35]+"..."
            else:
                page_name_shorter = user_obj.page_name

            if len(user_obj.page_name) > 15:
                page_name_even_shorter_for_mobile = user_obj.page_name[0:15]+"..."
            else:
                page_name_even_shorter_for_mobile = user_obj.page_name
            
            tototo+=user_obj.number_of_friends
            user_info_dict = {
                "page_name": user_obj.page_name,
                "page_name_shorter":page_name_shorter,
                "page_name_even_shorter_for_mobile":page_name_even_shorter_for_mobile,
                "page_url": user_obj.page_url,
                "gender":user_obj.gender,
                "is_alive":str(user_obj.is_alive),
                "picture_url": user_obj.picture_url,
                #"birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),
                "birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),   
                "birth_country_name":user_obj.country_birth_place,           
                "town_death_localisation": dms_to_decimal(user_obj.town_death_localisation),
                "country_birth_place_emoji":user_obj.country_birth_place_emoji,
                "page_nb":chunk_nb,
                "number_of_element":length
            }
            list_of_all_user_data.append(user_info_dict)
        except:

            pass
    print(tototo)
    print(int(tototo/500))
    return JsonResponse({"all_user_data":list_of_all_user_data},status=200)
