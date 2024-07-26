from django.contrib import admin

from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    empty_value_display = "-пусто-"


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "menu", "parent")
    empty_value_display = "-пусто-"


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
