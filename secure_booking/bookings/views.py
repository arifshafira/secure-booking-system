from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Booking
from .forms import BookingForm
from audit.models import AuditLog
from .models import Booking, RoomType

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

@login_required
def booking_list(request):
    if request.user.is_admin():
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/list.html', {'bookings': bookings})

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            AuditLog.objects.create(
                user=request.user,
                action='created',
                description=f'Booking created: {booking.title}',
                ip_address=get_client_ip(request)
            )
            messages.success(request, 'Reservation created successfully!')
            return redirect('bookings:list')
    else:
        form = BookingForm()
    rooms = RoomType.objects.filter(is_available=True)
    return render(request, 'bookings/form.html', {'form': form, 'action': 'Create', 'rooms': rooms})

@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if not request.user.is_admin() and booking.user != request.user:
        AuditLog.objects.create(
            user=request.user,
            action='access_denied',
            description=f'Unauthorized access attempt to booking #{pk}',
            ip_address=get_client_ip(request)
        )
        raise PermissionDenied
    return render(request, 'bookings/detail.html', {'booking': booking})

@login_required
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if not request.user.is_admin() and booking.user != request.user:
        AuditLog.objects.create(
            user=request.user,
            action='access_denied',
            description=f'Unauthorized edit attempt on booking #{pk}',
            ip_address=get_client_ip(request)
        )
        raise PermissionDenied
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            AuditLog.objects.create(
                user=request.user,
                action='updated',
                description=f'Booking updated: {booking.title}',
                ip_address=get_client_ip(request)
            )
            messages.success(request, 'Reservation updated successfully!')
            return redirect('bookings:list')
    else:
        form = BookingForm(instance=booking)
    rooms = RoomType.objects.filter(is_available=True)
    return render(request, 'bookings/form.html', {'form': form, 'action': 'Edit', 'rooms': rooms})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if not request.user.is_admin() and booking.user != request.user:
        AuditLog.objects.create(
            user=request.user,
            action='access_denied',
            description=f'Unauthorized delete attempt on booking #{pk}',
            ip_address=get_client_ip(request)
        )
        raise PermissionDenied
    if request.method == 'POST':
        title = booking.title
        booking.delete()
        AuditLog.objects.create(
            user=request.user,
            action='deleted',
            description=f'Booking deleted: {title}',
            ip_address=get_client_ip(request)
        )
        messages.success(request, 'Booking deleted successfully!')
        return redirect('bookings:list')
    return render(request, 'bookings/confirm_delete.html', {'booking': booking})