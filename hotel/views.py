from django.http import HttpResponse
from .models import Room , Booking
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
from .forms import BookingForm

def home(request):
    return render(request, 'hotel/home.html')

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/rooms.html', {'rooms': rooms})

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'hotel/register.html', {'form': form})


@login_required
def book_room(request, room_id):
    room = Room.objects.get(id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room 
            booking.total_price = (booking.check_out - booking.check_in).days * room.price_per_night
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)

    else:
        form = BookingForm(initial={'room': room})

    return render(request, 'hotel/book_room.html', {'form': form, 'room': room})