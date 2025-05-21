from django.contrib import admin
from .models import Purok, Street, Household, Resident

admin.site.register(Purok)
admin.site.register(Street)
admin.site.register(Household)
admin.site.register(Resident)

