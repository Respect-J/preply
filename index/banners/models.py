from django.db import models
from abstractModel.models import BaseModel


class Banners(BaseModel):
    title_uz = models.CharField(max_length=256)
    title_ru = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256)
    link = models.EmailField(max_length=256)
    image = models.ImageField(upload_to='img/banners/')

    def __str__(self):
        return self.title_ru


# Create your models here.
