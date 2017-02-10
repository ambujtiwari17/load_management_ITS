from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# ----------------------------------------------------------------------------------------
# mylogin_required : It is an authentication function used to check whether a user is logged in or not
# Uses the request object to check the user attribute. If the attribute is null (no user logged in) then redirects to log in page
# Any function can be made into an authenticated function by using the "@mylogin_required" override.

# ----------------------------------------------------------------------------------------
# index : Function generates the basic index page of the application.
# The index page displays ad introduction about the website/project
# Users are given the option to LogIn or SignUp. The page does not perform any functions other than linking the login and registration pages
# There is no need to be logged in to access the index page.
def index(request):
    context = dict()
    return render(request, 'loadmanage/index.html', context)

def indexnew(request):
    context = dict()
    return render(request, 'loadmanage/index.html', context)

def login_user(request):
	context = dict()
    #if request.method == "POST":
    #    username = request.POST['username']
    #    password = request.POST['password']
    #    user = authenticate(username=username, password=password)
    #    if user is not None:
    #        if user.is_active:
    #            login(request, user)
    #            return render(request, 'pages/index.html')
    #        else:
    #            return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
    #    else:
    #        return render(request, 'login.html', {'error_message': 'Invalid login'})
	return render(request, 'loadmanage/login.html',context)




