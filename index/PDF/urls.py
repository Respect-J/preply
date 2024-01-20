from django.urls import path
from .views import PDFListView, PDFDetailView

urlpatterns = [
    path('get/', PDFListView.as_view(), name='subjects-list-create'),
    path('set/<uuid:pk>/', PDFDetailView.as_view(), name='subjects-retrieve-update-delete')
]
