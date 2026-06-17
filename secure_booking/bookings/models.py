from django.db import models
from django.conf import settings

class RoomType(models.Model):
    ROOM_CHOICES = (
        ('standard', 'Standard Room'),
        ('deluxe', 'Deluxe Room'),
        ('suite', 'Junior Suite'),
        ('executive', 'Executive Suite'),
        ('presidential', 'Presidential Suite'),
    )
    name = models.CharField(max_length=50, choices=ROOM_CHOICES, unique=True)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(default=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.get_name_display()

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='bookings'
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests = models.IntegerField(default=1)
    special_requests = models.TextField(blank=True)
    location = models.CharField(max_length=200, default='Main Building')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room_type} - {self.user.username} ({self.status})"

    def total_nights(self):
        if self.check_in_date and self.check_out_date:
            return (self.check_out_date - self.check_in_date).days
        return 0

    def total_price(self):
        if self.room_type and self.total_nights() > 0:
            return self.room_type.price_per_night * self.total_nights()
        return 0

    class Meta:
        ordering = ['-created_at']