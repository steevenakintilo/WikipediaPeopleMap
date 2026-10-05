from collections import Counter
from unidecode import unidecode
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django_ratelimit.decorators import ratelimit

from myapp.models import WikipediaUser , WikipediaUserUniqueTown , WikiopediaUserToUpdate

from random import randint
from random import sample
from django.db.models import OuterRef, Subquery
from dotenv import load_dotenv

from ..global_variable import *
from ..utility_function  import *


import ast
import os
import json
import csv

load_dotenv()


@ratelimit(key='ip', rate='4/h')
@csrf_exempt
def update_user_info_status(request):
    """A function that update an user info status"""
    if request.method != "POST":
        return HttpResponse(f"Bad request!", status=404)
    
    try:
        recieved_data = json.loads(request.body)
        user_obj = WikipediaUser.objects.filter(page_name=recieved_data["username"]).first()
        user_obj_update_obj = WikiopediaUserToUpdate.objects.filter(page_name=recieved_data["username"]).first()
        if user_obj_update_obj is None:
            for data in recieved_data["fields"]:
                print(data)
            user_obj_update_obj = WikiopediaUserToUpdate(
                page_name=recieved_data["username"],
                data_to_update=recieved_data["fields"],
                update_level = 4
            )
            send_message_discord(f"Change {recieved_data["username"]}\n {user_obj.page_url}\n Les infos à changer:\n {recieved_data["fields"]}")
            user_obj_update_obj.save()
        return JsonResponse({"success": True}, status=200)
    except:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": False}, status=400)

@csrf_exempt
def update_user_info(request):
    """A function that update an user info"""
    if request.headers.get("X-Admin-API-Key") != os.environ["ADMIN_API_KEY"]:
        return JsonResponse({"error": "Unauthorized"}, status=401)
    if request.method != "PATCH":
        return HttpResponse(f"Bad request!", status=404)
    if request.headers.get("X-Admin-API-Key") != os.environ["ADMIN_API_KEY"]:
        return JsonResponse({"error": "Unauthorized"}, status=401)
    try:
        recieved_data = json.loads(request.body)
        user_obj = WikipediaUser.objects.filter(page_name=recieved_data["username"]).first()
        user_obj_update_obj = WikiopediaUserToUpdate.objects.filter(page_name=recieved_data["username"]).first()
        for key , value in recieved_data.items():
            if key != "username":
                if str(value) != "":
                    setattr(user_obj, key, value)


        #user_obj = WikipediaUser.objects.filter(page_name=recieved_data["username"]).first()
        #user_obj.save()
        if recieved_data["is_alive"] is False:
            user_obj_update_obj.data_to_update = []
            user_obj_update_obj.update_level = 1

        else:
            user_obj_update_obj.data_to_update = []
            user_obj_update_obj.update_level = 2
            
        user_obj_update_obj.save()
        user_obj.save()
        return JsonResponse({"success": True}, status=200)
    except:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": False}, status=400)


@ratelimit(key='ip', rate='1/m')
@ratelimit(key='ip', rate='10/h')
@csrf_exempt
def validate_an_user(request,user=""):
    """A function that validate an user (his information)"""
    if request.method != "POST":
        return HttpResponse(f"Bad request!", status=404)

    try:
        NUMBER_OF_GOOD_REPORT_NEEDED = 99
        user_obj_update_obj = WikiopediaUserToUpdate.objects.filter(page_name=user).first()
        user_obj = WikipediaUser.objects.filter(page_name=user).first()
        if user_obj_update_obj is None:
            user_obj_update_obj = WikiopediaUserToUpdate(
                page_name=user,
                nb_of_good_report = 1,
                update_level=3
            )
            user_obj_update_obj.save()
        else:
            if user_obj_update_obj.nb_of_good_report >= NUMBER_OF_GOOD_REPORT_NEEDED:
                user_obj_update_obj.nb_of_good_report = NUMBER_OF_GOOD_REPORT_NEEDED
                if user_obj.is_alive:
                    user_obj_update_obj.update_level = 2
                else:
                    user_obj_update_obj.update_level = 1
                                
            else:
                user_obj_update_obj.nb_of_good_report+=1
                user_obj_update_obj.update_level=3
            print("user_obj_update_obj.nb_of_good_report " , user_obj_update_obj.nb_of_good_report,user_obj_update_obj.update_level)
            user_obj_update_obj.save()
        
        return JsonResponse({"success": True}, status=200)
    except:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": False}, status=400)
