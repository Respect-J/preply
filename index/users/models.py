from django.db import models
from abstractModel.models import BaseModel

class UserProfile(BaseModel):
    UNKNOWN = 'UNKNOWN'

    REGION_CHOICES = (
        ('Tashkent', 'Tashkent'),
        ('Samarkand', 'Samarkand')

    )

    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='img/user_photos/')
    phone_number = models.CharField(max_length=255)
    region = models.CharField(max_length=255, choices=REGION_CHOICES, default=UNKNOWN)
    password = models.CharField(max_length=255)
    payment_status = models.BooleanField(default=False)
    basket = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return self.username
