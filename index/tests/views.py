from rest_framework import generics
from .models import Tests
from .serializers import TestsSerializer


class TestsListView(generics.ListAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer


class TestsListCreate(generics.CreateAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer


class TestsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer


# Create your views here.
