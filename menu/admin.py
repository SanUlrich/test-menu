from django.contrib import admin
from .models import *


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('item_title', 'item_slug', 'parent')
    prepopulated_fields = {"item_slug": ("item_title",)}


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
