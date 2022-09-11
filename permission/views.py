from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.utils import timezone

from .models import User


# Create your views here.
def index(request):    
    if request.COOKIES.get('username') is not None:
        username = request.COOKES.get('username')
        password = request.COOKIES.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("permission:index")
        else:
            return redirect("permission:index")

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            response = redirect("permission:index")
            return response
        else:
            return render(request, 'account/login.html', {'error':'다시 입력해주세요.'})
    
    else:
        return render(request, "permission/index.html")
    

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

def logout(request):
    response = render(request, 'permission/index.html')
    response.delete_cookie('username')
    response.delete_cookie('password')
    logout(request)
    return response

def change_pw(request):
    context = {}
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        user = request.user
        if check_password(old_password, user.password):
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1 == password2:
                user.set_password(password1)
                user.save()
                login(request, user)
                return redirect('permission:index')
            else:
                context.update({'error':'새 비밀번호가 확인되지 않았습니다.'})
        else:
            context.update({'error':'현재 비밀번호가 틀립니다.'})
    return render(request, 'permission/change_pw.html', context)