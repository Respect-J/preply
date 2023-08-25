from rest_framework import generics
from .models import Subjects
from .serializers import SubjectsSerializer


class SubjectsListView(generics.ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer


class SubjectsListCreate(generics.CreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer


class SubjectsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
