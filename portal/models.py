from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    permitted_place = models.IntegerField(default=0)
    is_advisor = models.BooleanField(default=False)

    def _id(self):
        return self.username
    pass
