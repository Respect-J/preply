from django.urls import path
from .views import solves

urlpatterns = [
    path('get/<uuid:pk>/', solves)

]
