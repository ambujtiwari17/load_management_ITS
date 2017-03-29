from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context_processors import csrf
from forms import Complaintform, Usageform ,Applianceform
from django.shortcuts import render_to_response
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/load/')
def HomePageView(request):
    if request.user.username == 'Admin':
        return HttpResponseRedirect('/admin')
    else:
        return HttpResponseRedirect('/load/sel')


@login_required(login_url='/load/')
def sel(request):
    all_appliances=ApplianceName.objects.filter(user_id=request.user.id)
    return render(request,'sel.html',{'aa':all_appliances,'name':request.user.username})

@login_required(login_url='/load/')
def complain(request):
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
    all_use=Usage.objects.filter(app_id=appliance_id)
    return render(request,'details.html',{'a':appliance_id,'used':all_use,'name':request.user.username})