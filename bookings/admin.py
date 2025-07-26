from django.contrib import admin
from .models import Service, TimeSlot, Booking

admin.site.register(Service)
admin.site.register(TimeSlot)
admin.site.register(Booking)
