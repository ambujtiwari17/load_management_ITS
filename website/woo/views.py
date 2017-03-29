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
import pytz 
from pytz import timezone as t
from datetime import datetime, date, time

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
    today=datetime.now(t('Asia/Kolkata')).date()
    nt=[]
    app=ApplianceName.objects.get(id=appliance_id)
    app=str(app)
    app=app.split(" - ")
    app=app[2]
    for a in all_use:
        now=a.recordtime
        now_date=now.date()
        now_time=now.time()
        now_min=now_time.minute+30
        now_hrs=now_time.hour+5+(now_min/60)
        now_day=now_date.day+now_hrs/24
        number_of_days=31
        if now_date.month in [4,6,9,11] :
            number_of_days=30
        if now_date.month==2:
            if now_date.year%4==0 and now_date.year%100!=0:
                number_of_days=29
            else:
                number_of_days=28
        now_month=now_date.month+now_day/number_of_days
        now_year=now_date.year+now_month/12
        now_day=now_day%number_of_days
        now_min=now_min%60
        now_hrs=now_hrs%24
        now_month=now_month%12
        if now_day==today.day and now_month==today.month and now_year==today.year: 
            nt.append(time(now_hrs,now_min,0))
            graph_use[now_hrs]+=a.use
    return render(request,'details.html',{'a':app,'used':all_use,'name':request.user.username,'g':graph_use,'l':labels,'t':today})

def adddata(request,aid,value):
    uid=ApplianceName.objects.get(pk=aid).user_id
    new_usage=Usage.objects.create(user_id=uid,app_id=ApplianceName.objects.get(pk=aid),use=value,recordtime=datetime.now(timezone('Asia/Kolkata')))
    new_usage.save()
    return render(request,'add.html',{'a':aid,'u':uid,'value':value})