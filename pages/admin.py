from django.contrib import admin
from .models import Page, MenuPage, Settings

admin.site.register(Page)
admin.site.register(MenuPage)
admin.site.register(Settings)