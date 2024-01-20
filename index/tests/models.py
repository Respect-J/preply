from django.db import models
from abstractModel.models import BaseModel, LanguageChoice
from subjects.models import Subjects
from topics.models import Topics
from enum import Enum


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

""" 
    "language": null,
    "is_mandatory": false,
    "correct_answer": null,
    "options": null,
    "subject": null,
    "topic": null
    
"""

class Tests(BaseModel):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    language = models.CharField(max_length=3, choices=LanguageChoice.choices)
    is_mandatory = models.BooleanField(default=False)
    question = models.TextField(null=True)
    img = models.FileField(upload_to="img/tests/", null=True)
    correct_answer = models.CharField(choices=AnswersChoice.choices)
    options = models.JSONField(null=True)

    def __str__(self):
        return f"Test on {self.subject} - {self.topic} ({self.language})"
