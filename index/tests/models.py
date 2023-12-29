from django.db import models
from abstractModel.models import BaseModel
from subjects.models import Subjects
from topics.models import Topics
from enum import Enum


class Language(Enum):
    UZ = "UZ"
    EN = "EN"
    RU = "RU"


class LanguageChoice(models.TextChoices):
    UZ = Language.UZ.value, "Uzbek"
    EN = Language.EN.value, "English"
    RU = Language.RU.value, "Russian"


class Answers(Enum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"


class AnswersChoice(models.TextChoices):
    A = Answers.A.value, "a"
    B = Answers.B.value, "b"
    C = Answers.C.value, "c"
    D = Answers.D.value, "d"


class Tests(BaseModel):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    language = models.CharField(max_length=3, choices=LanguageChoice.choices)
    is_mandatory = models.BooleanField(default=False)
    correct_answer = models.CharField(max_length=3, choices=AnswersChoice.choices)
    options = models.JSONField()

    def __str__(self):
        return f"Test on {self.subject} - {self.topic} ({self.language})"