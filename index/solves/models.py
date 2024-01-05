from django.db import models
from users.models import UserProfile
from tests.models import Tests

class Solves(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)

# Create your models here.
