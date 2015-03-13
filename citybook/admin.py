from django.contrib import admin
from citybook.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'food', 'timezone']


admin.site.register(City, CityAdmin)

