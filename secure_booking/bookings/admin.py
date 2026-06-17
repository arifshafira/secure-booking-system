from django.contrib import admin
from .models import Booking, RoomType

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_per_night', 'capacity', 'is_available']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'room_type', 'check_in_date', 'check_out_date', 'status']