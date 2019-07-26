from django.contrib import admin

from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('erp_id', 'name', 'nick_name', 'tel', 'openid_xcx', 'is_valid')

admin.site.register(User, UserAdmin)
