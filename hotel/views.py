from django.http import HttpResponse
from .models import Room , Booking
from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
from .forms import BookingForm , RoomForm
from django.contrib.admin.views.decorators import staff_member_required
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


@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'hotel/booking_confirmation.html', {'booking': booking})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-check_in')
    return render(request, 'hotel/my_bookings.html', {'bookings': bookings})

@staff_member_required
def admin_dashboard(request):
    bookings = Booking.objects.all().order_by('-check_in')
    return render(request, 'hotel/admin_dashboard.html', {'bookings': bookings})

@staff_member_required
def update_booking_status(request, booking_id, status):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = status
    booking.save()
    return redirect('admin_dashboard')

@login_required
def create_room(request):
    if not request.user.is_staff:
        return redirect('home')  

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')  
    else:
        form = RoomForm()

    return render(request, 'hotel/create_room.html', {'form': form})

def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)  

    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES, instance=room) 
        if form.is_valid():
            form.save()  
            return redirect('room_list')  
        else:
           
            return render(request, 'hotel/edit_room.html', {'form': form, 'room': room})
    else:
        form = RoomForm(instance=room)
        return render(request, 'hotel/edit_room.html', {'form': form, 'room': room})
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        room.delete()
        return redirect('room_list')  

    return render(request, 'hotel/rooms.html', {'room': room})