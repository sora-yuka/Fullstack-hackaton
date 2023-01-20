from django.contrib import admin
from applications.account.models import CustomUser, Profile

admin.site.register(CustomUser)
admin.site.register(Profile)