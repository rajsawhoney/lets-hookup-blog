from django.contrib import admin

# Register your models here.
from .models import UserModel, IPAddress
@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    pass
