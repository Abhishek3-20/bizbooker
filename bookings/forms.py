from django import forms
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time']
        widgets = {
            'service': forms.Select(attrs={
                'placeholder': 'Select a service',
                'class': 'input input-bordered w-full text-gray-500'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Choose a date',
                'class': 'input input-bordered w-full text-gray-500'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'placeholder': 'Choose a time',
                'class': 'input input-bordered w-full text-gray-500'
            }),
            
        }
class SimpleRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'}),
        help_text="Choose any password you like"
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password1(self):
        return self.cleaned_data.get("password1") 