from django.contrib import admin

from .models import Inventory, Software

admin.site.register(Inventory)
admin.site.register(Software)

