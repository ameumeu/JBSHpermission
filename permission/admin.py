from django.contrib import admin

# Register your models here.
from .models import Permission

admin.site.register(Permission)