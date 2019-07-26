from django.contrib import admin

from .models import Sheet

# Register your models here.
class SheetAdmin(admin.ModelAdmin):
    list_display = ('erp_id', 'name', 'score', 'score_total', 'is_valid', 'shijuan')

admin.site.register(Sheet, SheetAdmin)
