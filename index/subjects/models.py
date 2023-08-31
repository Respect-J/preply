from django.db import models
from abstractModel.models import BaseModel, Language


class Subjects(BaseModel, Language):
    is_mandatory = models.BooleanField(default=False)

    def __str__(self):
        return self.title_ru
