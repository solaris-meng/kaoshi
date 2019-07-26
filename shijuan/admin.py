from django.contrib import admin

from .models import Category,Shijuan,Stype

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('erp_id', 'name', 'is_valid')
class StypeAdmin(admin.ModelAdmin):
    list_display = ('erp_id', 'name', 'is_valid', 'is_manual', 'is_random', 'total')
class ShijuanAdmin(admin.ModelAdmin):
    list_display = ('erp_id', 'name', 'is_valid', 'category', 'stype')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Stype, StypeAdmin)
admin.site.register(Shijuan, ShijuanAdmin)
