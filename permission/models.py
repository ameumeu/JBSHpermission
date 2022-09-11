from django.db import models
import datetime

# Create your models here.
class Permission(models.Model):
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