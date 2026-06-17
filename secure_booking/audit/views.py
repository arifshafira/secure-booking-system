from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import AuditLog

@login_required
def audit_log_view(request):
    if not request.user.is_admin():
        raise PermissionDenied
    logs = AuditLog.objects.all().order_by('-timestamp')[:200]
    return render(request, 'audit/logs.html', {'logs': logs})