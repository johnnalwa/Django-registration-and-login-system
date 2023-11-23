# users/admin.py

from django.contrib import admin
from .models import CustomUser, UserProfile, Client, Attendance, Sale, Commission, RoutePlan

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Client)
admin.site.register(Attendance)
admin.site.register(Sale)
admin.site.register(Commission)
admin.site.register(RoutePlan)
