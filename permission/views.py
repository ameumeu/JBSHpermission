from django.shortcuts import render, redirect

import json

from .models import Permission

# Create your views here.
def index(request):
    permission_list = Permission.objects.all()
    return render(request, 'permission/index.html', {'permission_list':permission_list})
    
def detail(request):
    return render(request, 'permission/details.html')

def create(request):
    if request.method == "POST":
        """
        id = models.IntegerField()
        activity = models.CharField(max_length=10)
        participants = models.JSONField()
        classroom = models.TextField()
        pub_date = models.DateField(default=datetime.date.today)
        period_1 = models.BooleanField(default=False)
        period_2 = models.BooleanField(default=False)
        is_permitted = models.BooleanField(default=False)
        representative =  models.IntegerField()
        advisor = models.CharField(max_length=35)
        """
        p = Permission(
            activity = request.POST['activity'],
            participants = json.dumps({'participants':request.POST['participants']}),
            classroom = request.POST['classroom'],
            period_1 = request.POST['period_1'],
            period_2 = request.POST['peroid_2'],
            representative = request.POST['representative'],
            advisor = request.POST['advisor'],
        )
        p.save()
        return redirect('permission:index')
    else:
        return render(request, 'permission/create.html')