from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
import os,sys,json
from datetime import datetime
from .models import *
from django.db import connection

# Create your views here.


def dashboard(request):
    return render(request, "dashboard.html")

def get_application_list(request):
    apps = application.objects.all()
    d=[]
    for app in apps:
        d.append({'application': app.name, 'posx': app.posx, 'posy': app.posy, 'colspan':app.colspan, 'id':app.id})
    return HttpResponse(json.dumps(d), content_type="application/json")
 
def get_application_details(request,appname):
    if request.method == 'GET':
       result = dict()
       data = []
       ci = configure_item.objects.filter(application__name=appname)
       ci_params = [ str(sci) for sci in ci ]
       print(ci_params)
       s = servicenow()
       incs = s.get_incident_by_list_ci(ci_params)

       # Test incident
       result["title"] = appname
       result["updatedAt"] = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
       result["data"] = []

       if len(incs)==0:
          result["bgcolor"] = "#34A417"
          result["data"].append({"label":"message", "value":"No On-going Incident"})
          result["hasInc"] = 0
       else:
          result["bgcolor"] = "#A41914"
          result["hasInc"] = 1
          result["eta"] = "1.5h"
          for inc in incs:
            result["data"].append(inc)

       data.append(result)
       print(data)
       return HttpResponse(json.loads(json.dumps(data)), content_type="application/json")

def get_relation(request, incidentID):
    return render(request, "relation.html")

def get_fake_data(request):
    data = open(settings.DATA_PATH, "r")
    return HttpResponse(json.loads(json.dumps(data.readlines())), content_type="application/json")
    
def get_child(incidentID):
    c = connection.cursor()
    c.execute('select * from servicenow_incident where inc_dup_id in (select children from servicenow_incident where parent = "%s")' % incidentID)
    result = c.fetchall()
    return result

def get_parent(incidentID):
    c = connection.cursor()
    c.execute('select * from servicenow_incident where inc_dup_id in (select parent from servicenow_incident where children = "%s")' % incidentID)
    result = c.fetchall()
    return result
