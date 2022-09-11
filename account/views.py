from msilib.schema import Error
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.utils import timezone

# Create your views here.
"""def login(request):    
    response = render(request, 'permission/index.html') # redirect("permission:index")
    if request.session['username'] is not None:
        username = request.session.get('username')
        password = request.session.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return response
        else:
            return response

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            request.session['password'] = password
            request.session['error'] = None  
            return response
        else:
            response = redirect('permission:index')
            request.session['error'] = 'err_index_1'
            return response
    
    else:
        return redirect("permission:index")
"""
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
                context.update({'error':'err_cpw_1'})
        else:
            context.update({'error':'err_cpw_2'})
    return render(request, 'account/change_pw.html', context)

def out(request):
    response = redirect('permission:index')
    response.delete_cookie('username')
    response.delete_cookie('password')
    logout(request)
    return response


def login(request):    
    response = render(request, 'permission/index.html') # redirect("permission:index")
    try: # request.session['username'] is not None:
        username = request.session.get('username')
        if username is None:
            raise ValueError
        password = request.session.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        print("ok thern")
        if user is not None:
            login(request, user)
            return response
        else:
            return response
    except:
        print("made error")
        if request.method == "POST":
            print('yeah post')
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['username'] = username
                request.session['password'] = password
                request.session['error'] = None  
                return response
            else:
                response = redirect('permission:index')
                request.session['error'] = 'err_index_1'
                return response
        else : redirect("permission:index")