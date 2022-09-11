from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('change_pw/', views.change_pw, name='change_pw'),
    path('logout/', views.out, name="logout"),
]