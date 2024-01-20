from django.db import models
from abstractModel.models import BaseModel, LanguageChoice


class PDF(BaseModel):
    language = models.CharField(max_length=3, choices=LanguageChoice.choices)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='img/PdfFile/')
    img = models.ImageField(upload_to='img/Pdfimg/')
    price = models.IntegerField(null=True)

    def formatted_price(self):
        return f"${self.price}" if self.price is not None else "N/A"

    def file_url(self):
        return self.file.url if self.file else None

    def __str__(self):
        return self.title
