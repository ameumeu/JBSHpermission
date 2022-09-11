from django.contrib import admin

# Register your models here.
from .models import Permission, Place

admin.site.register(Permission)
admin.site.register(Place)