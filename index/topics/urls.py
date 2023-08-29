from django.urls import path
from .views import TopicsListView, TopicsListCreate, TopicsRetrieveUpdateDelete

urlpatterns = [
    path('get/', TopicsListView.as_view(), name='subjects-list-create'),
    path('post/', TopicsListCreate.as_view(), name='subjects-list-create'),
    path('set/<uuid:pk>/', TopicsRetrieveUpdateDelete.as_view(), name='subjects-retrieve-update-delete')
]
