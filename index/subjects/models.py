from django.db import models
from abstractModel.models import BaseModel


class Subjects(BaseModel):
    title_uz = models.CharField(max_length=256)
    title_ru = models.CharField(max_length=256)
    title_ka = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256)
    is_mandatory = models.BooleanField(default=False)

    def __str__(self):
        return self.title_ru
