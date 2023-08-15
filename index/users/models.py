from django.db import models
import uuid

class UserProfile(models.Model):
    UNKNOWN = 'UNKNOWN'

    REGION_CHOICES = (
        (UNKNOWN, 'Unknown'),
        # Добавьте другие варианты региона по мере необходимости
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='user_photos/')
    phone_number = models.CharField(max_length=255)
    region = models.CharField(max_length=255, choices=REGION_CHOICES, default=UNKNOWN)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_status = models.BooleanField(default=False)
    basket = models.JSONField(default=list)

    def __str__(self):
        return self.username
