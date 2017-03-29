from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context_processors import csrf
from forms import Complaintform, Usageform ,Applianceform
from django.shortcuts import render_to_response
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required
from pytz import timezone
# import urllib2
# import json

@login_required(login_url='/load/')
def HomePageView(request):
    if request.user.username == 'Admin':
        return HttpResponseRedirect('/admin')
    else:
        return HttpResponseRedirect('/load/sel')


@login_required(login_url='/load/')
def sel(request):
    if request.user.username == 'Admin':
        return HttpResponseRedirect('/admin')
    # response=urllib2.urlopen('http://shrave.pythonanywhere.com/sensors_json_all')
    # data=json.load(response)
    # for i in data:
    #     u=i['Username']
    #     a=i['DeviceName']
    #     us=i['Value']
    #     ti=i['Time']
    #     uc=User.objects.filter(username=u)
    #     uc=uc[0].pk
    #     ac1=ApplianceName.objects.filter(appliance=a)
    #     for a in ac1:
    #         if a.user_id==uc:
    #             ac=a.pk
    #             break
    #     us_check=Usage.objects.get(user_id=uc,app_id=ApplianceName.objects.get(pk=ac),use=us,recordtime=ti)
    #     if not us_check:
    #         new_usage=Usage.objects.create(user_id=uc,app_id=ApplianceName.objects.get(pk=ac),use=us,recordtime=ti)
    #         new_usage.save()
    all_appliances=ApplianceName.objects.filter(user_id=request.user.id)
    return render(request,'sel.html',{'aa':all_appliances,'name':request.user.username})

@login_required(login_url='/load/')
def complain(request):
    if request.user.username == 'Admin':
        return HttpResponseRedirect('/admin')
    if request.POST:
        form=Complaintform(request.POST)
        if form.is_valid():
            complaint=form.save(commit=False)
            complaint.user=request.user
            complaint.save()
            return HttpResponseRedirect('/load/complaint')
    else:
        form=Complaintform()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['name']=request.user.username
    args['com']=Complaint.objects.filter(user_id=request.user.id)
    return render_to_response('complain.html',args)

@login_required(login_url='/load/')
def appliance(request):
    if request.user.username == 'Admin':
        return HttpResponseRedirect('/admin')
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

@login_required(login_url='/load/')
def use(request):
    if request.user.username == 'Admin':
        return HttpResponseRedirect('/admin')
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

@login_required(login_url='/load/')
def details(request,appliance_id):
    if request.user.username == 'Admin':
        return HttpResponseRedirect('/admin')
    all_use=Usage.objects.filter(app_id=appliance_id)
    graph_use=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labels=[]
    today=datetime.now(timezone('Asia/Kolkata')).date()
    nt=[]
    app=ApplianceName.objects.get(id=appliance_id)
    app=str(app)
    app=app.split(" - ")
    app=app[2]
    for a in all_use:
        now=a.recordtime
        now_date=now.date()
        if now_date==today:
            now_time=now.time()
            now_min=now_time.minute+30
            now_hrs=now_time.hour+5+(now_min/60)
            nt.append(now_hrs)
            graph_use[now_hrs]+=a.use
    return render(request,'details.html',{'a':app,'used':all_use,'name':request.user.username,'g':graph_use,'l':labels,'t':today})

def adddata(request,aid,value):
    uid=ApplianceName.objects.get(pk=aid).user_id
    new_usage=Usage.objects.create(user_id=uid,app_id=ApplianceName.objects.get(pk=aid),use=value,recordtime=datetime.now(timezone('Asia/Kolkata')))
    new_usage.save()
    return render(request,'add.html',{'a':aid,'u':uid,'value':value})