from django.contrib import admin
from .models import Room

admin.site.register(Room)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'capacity', 'price_per_night', 'is_available')