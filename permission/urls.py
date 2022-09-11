from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'permission'
urlpatterns = [
    path('', views.index, name="index"),
    
    # path('account/', include('account.urls')),
    path('change_pw/',  views.change_pw, name='change_pw'),
    path('logout/', views.out, name="logout"),
]