from rest_framework import serializers
from .models import Solves


class SolveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Solves
        fields = '__all__'