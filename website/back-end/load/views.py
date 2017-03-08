from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from forms import Complaintform, Usageform ,Applianceform
from django.shortcuts import render_to_response
from .models import *

def index(request):
    html="<h1>Select Appliance</h1><br>"
    all_appliances=ApplianceName.objects.all()
    for app in all_appliances:
        url="/load/"+str(app.id)+"/"
        html +="<a href ="+url+">"+app.appliance+"</a><br>"
    return HttpResponse(html)

def complain(request):
    if request.POST:
        form=Complaintform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/load/complaint')
    else:
        form=Complaintform()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('complain.html',args)

def appliance(request):
    if request.POST:
        form=Applianceform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/load/appliance')
    else:
        form=Applianceform()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('appliance.html',args)

def use(request):
    if request.POST:
        form=Usageform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/load/use')
    else:
        form=Usageform()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('use.html',args)

def details(request,appliance_id):
    html="<h2>Details of appliance id:" + str(appliance_id) + "</h2><br>"
    all_use=Usage.objects.filter(app_id=appliance_id)
    html+="<table>"
    for a in all_use:
        html+="<tr><td>" + str(a.use) + "</td><td>" + str(a.recordtime) + "</td></tr>"
    html+="</table>"
    return HttpResponse(html)