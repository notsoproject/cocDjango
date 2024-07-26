# users/admin.py
from django.contrib import admin
from .models import Users_Details, CustomUser

admin.site.register(Users_Details)
admin.site.register(CustomUser)
