from django.db import models
from abstractModel.models import BaseModel


class Categories(BaseModel):
    title_uz = models.CharField(max_length=256)
    title_ru = models.CharField(max_length=256)
    title_ka = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='img/categories/')

    def __str__(self):
        return self.title_ru

# Create your models here.
