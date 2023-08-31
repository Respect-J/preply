from django.db import models
from abstractModel.models import BaseModel, Language
from subjects.models import Subjects


class Topics(BaseModel, Language):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_ru

