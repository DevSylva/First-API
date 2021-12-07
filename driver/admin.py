from django.contrib import admin
from .models import Driver
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Driver)
admin.site.unregister(Group)