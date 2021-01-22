from django.contrib import admin
from .models import Carpet, Natural
# Register your models here.

class CarpetAdmin(admin.ModelAdmin):
    list_display=('id','name','created_date','isPublished')
    list_display_links=('id','name')
    list_filter=('id','name','created_date')
    list_editable=('isPublished',)
    search_fields=('id','name','created_date')
    list_per_page= 5

class NaturalAdmin(admin.ModelAdmin):
    list_display=('id','name','created_date','isPublished')
    list_display_links=('id','name')
    list_filter=('id','name','created_date')
    list_editable=('isPublished',)
    search_fields=('id','name','created_date')
    list_per_page = 5



admin.site.register(Carpet,CarpetAdmin)
admin.site.register(Natural,NaturalAdmin)

