from django.http import HttpResponse
from .models import Room
from django.shortcuts import render
def home(request):
    return render(request, 'hotel/home.html')

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/rooms.html', {'rooms': rooms})
