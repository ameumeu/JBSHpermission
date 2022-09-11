from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.utils import timezone



# Create your views here.
def index(request): 
    try: #request.session['username'] is not None:
        print('nohai')
        username = request.session['username']
        password = request.session['password']
        error = request.session['error']
        user = authenticate(username=username, password=password)
        login(request, user)
        print('ready')
        return render(request, "permission/logout.html")
    except:
        return render(request, 'permission/index.html')
    

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user = authenticate(request, username=username, password=password2)
        if user is None:
            return redirect(reverse("permission:login"))
        login(request, user)
        return redirect(reverse("permission:index"))
    return render(request, 'permission/signup.html')


