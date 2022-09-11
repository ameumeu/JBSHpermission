from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import json

from .models import Permission, Place

# Create your views here.
def index(request):
    permission_list = Permission.objects.all()
    return render(request, 'permission/index.html', {'permission_list':permission_list})
    
def detail(request):
    return render(request, 'permission/details.html')

@login_required
def create(request):
    if request.method == "POST":
        """
        activity = models.CharField(max_length=10)
        activity_detail = models.CharField(max_length=2, default='')
        participants = models.JSONField()
        place = models.IntegerField(default=0)
        pub_date = models.DateField(default=datetime.date.today)
        period_1 = models.BooleanField(default=False)
        period_2 = models.BooleanField(default=False)
        is_permitted = models.BooleanField(default=False)
        representative =  models.IntegerField()
        advisor = models.CharField(max_length=35)
        """
        try:
            request.POST['period_1']
            period_1 = True
        except:
            period_1 = False
        
        try:
            request.POST['period_2']
            period_2 = True
        except:
            period_2 = False

        representative = request.POST['representative'] if request.POST['representative'] else int(request.user.username)

        p = Permission(
            activity = request.POST['activity'],
            activity_detail = request.POST['activity_detail'],
            participants = json.dumps({'participants':request.POST['participants']}),
            place = request.POST['place'],
            period_1 = period_1,
            period_2 = period_2,
            representative = representative,
            advisor = request.POST['advisor'],
        )
        p.save()
        return redirect('permission:index')
    else:
        return render(request, 'permission/create.html', {'place_list': Place.objects.all()})