from django.urls import path
from .views import solves, add_solve

urlpatterns = [
    path('get/<uuid:pk>/', solves),
    path('post/', add_solve)

]
