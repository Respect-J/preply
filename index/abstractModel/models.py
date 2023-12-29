from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Language(models.Model):
    title_uz = models.CharField(max_length=256)
    title_ru = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256)

    class Meta:
        abstract = True