from rest_framework import generics
from .models import PDF
from .serializers import PDFSerializer

class PDFListView(generics.ListCreateAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

class PDFDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer




