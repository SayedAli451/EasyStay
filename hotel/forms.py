from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out', 'guests']  
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }
