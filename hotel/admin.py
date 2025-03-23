from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'capacity', 'price_per_night', 'is_available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'check_in', 'check_out', 'status')
    list_filter = ('status', 'check_in', 'check_out')
    search_fields = ('room__name', 'user__username')
