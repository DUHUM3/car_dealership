from django.contrib import admin
from .models import Car, Manufacturer

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'manufacturer', 'image')

admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)
