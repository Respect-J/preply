from rest_framework import generics
from .models import Topics
from .serializers import TopicsSerializer


class TopicsListView(generics.ListAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer


class TopicsListCreate(generics.CreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer


class TopicsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer
