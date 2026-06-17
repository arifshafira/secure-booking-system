from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, ProfileUpdateForm
from audit.models import AuditLog

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('bookings:list')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            AuditLog.objects.create(
                user=user,
                action='created',
                description=f'New user registered: {user.username}',
                ip_address=get_client_ip(request)
            )
            messages.success(request, 'Account created! Please login.')
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('bookings:list')
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            AuditLog.objects.create(
                user=user,
                action='login',
                description=f'User logged in: {user.username}',
                ip_address=get_client_ip(request)
            )
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('bookings:list')
        else:
            AuditLog.objects.create(
                user=None,
                action='login_failed',
                description=f'Failed login attempt for username: {username}',
                ip_address=get_client_ip(request)
            )
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    AuditLog.objects.create(
        user=request.user,
        action='logout',
        description=f'User logged out: {request.user.username}',
        ip_address=get_client_ip(request)
    )
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('accounts:login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            AuditLog.objects.create(
                user=request.user,
                action='updated',
                description=f'User updated profile: {request.user.username}',
                ip_address=get_client_ip(request)
            )
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})