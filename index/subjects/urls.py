from django.urls import path
from .views import SubjectsListView, SubjectsListCreate, SubjectsRetrieveUpdateDelete

urlpatterns = [
    path('get/', SubjectsListView.as_view(), name='subjects-list-create'),
    path('post/', SubjectsListCreate.as_view(), name='subjects-list-create'),
    path('set/<uuid:pk>/', SubjectsRetrieveUpdateDelete.as_view(), name='subjects-retrieve-update-delete')
]
