from django.urls import path, include
from . import views

app_name = 'permission'
urlpatterns = [
    path('', views.index, name="index"),
    # path('account/', include('account.urls')),
]