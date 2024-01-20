from django.db import models
from abstractModel.models import BaseModel, LanguageChoice


class PDF(BaseModel):
    language = models.CharField(max_length=3, choices=LanguageChoice.choices)
    decription = models.TextField()
    file = models.ImageField(upload_to='img/PdfFile/file')
    img = models.ImageField(upload_to='img/PdfFile/img')
    price = models.IntegerField(null=True)


    def __str__(self):
        return self.title_ru


