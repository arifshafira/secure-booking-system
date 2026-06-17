from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'Normal User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def is_admin(self):
        return self.role == 'admin'

    def __str__(self):
        return f"{self.username} ({self.role})"