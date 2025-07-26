from django import forms
from .models import Booking, Service, TimeSlot
from .models import Booking, Service


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time']