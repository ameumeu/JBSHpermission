from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.utils import timezone

from .forms import CustomPasswordChangeForm
from .models import User


# Create your views here.
def index(request):    
    response = render(request, "portal/index.html")
    if request.COOKIES.get('user') is not None:
        try:
            # user = User.objects.get(username=request.COOKIES.get('user'))
            # print(user)
            username = user.get("username")
            password = user.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return response
            else:
                return response
        except:
            response.delete_cookie('user')
            return response

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user_instance = User.objects.get(username=username)
            response.set_cookie('user', user_instance)
            return redirect('portal:index')
        else:
            return render(request, 'portal/index.html', {'error':'다시 입력해주세요.'})
    
    else:
        return render(request, "portal/index.html")
    

@login_required
def out(request):
    response = redirect('portal:index')
    response.delete_cookie('user')
    logout(request)
    return response

@login_required
def change_pw(request):
    context = {}
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('portal:change_pw')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'portal/change_pw.html', {'form':form})