from django.shortcuts import render


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


