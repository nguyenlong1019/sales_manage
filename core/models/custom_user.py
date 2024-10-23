from django.db import models 
from django.contrib.auth.models import AbstractUser 


class CustomUser(AbstractUser):
    ROLE = (
        ('user', 'user'),
        ('admin', 'admin'),
    )
    role = models.CharField(max_length=15, default='user', choices=ROLE)

    def __str__(self):
        return f"{self.id} - {self.username} - {self.role}"
