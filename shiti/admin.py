from django.contrib import admin

from .models import Category,Xuanzeti
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_valid')
class XuanzetiAdmin(admin.ModelAdmin):
    list_display = ('erp_id', 'wenti', 'daan', 'is_valid')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Xuanzeti, XuanzetiAdmin)
