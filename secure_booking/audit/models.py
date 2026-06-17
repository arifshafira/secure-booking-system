from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    ACTION_CHOICES = (
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('login_failed', 'Login Failed'),
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('deleted', 'Deleted'),
        ('viewed', 'Viewed'),
        ('access_denied', 'Access Denied'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    description = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user} - {self.action} - {self.timestamp}"