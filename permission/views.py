from django.shortcuts import render

from .models import Permission

# Create your views here.
def index(request):
    permission_list = Permission.objects.all()
    return render(request, 'permission/index.html', {'permission_list':permission_list})