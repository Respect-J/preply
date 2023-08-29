from django.db import models
from abstractModel.models import BaseModel
from subjects.models import Subjects


class Topics(BaseModel):
    title_uz = models.CharField(max_length=256)
    title_ru = models.CharField(max_length=256)
    title_ka = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_ru

