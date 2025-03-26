from django import forms
from .models import Booking , Room

class BookingForm(forms.ModelForm):
    ROOM_TYPES = Room.ROOM_TYPES  

    room_type = forms.ChoiceField(choices=ROOM_TYPES)  
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    guests = forms.IntegerField(min_value=1)

    class Meta:
        model = Booking  
        fields = ['room_type', 'check_in', 'check_out', 'guests']
          
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'room_type', 'price_per_night', 'capacity', 'is_available', 'image_url']

        