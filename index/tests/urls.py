from django.urls import path
from .views import TestsListView, TestsListCreate, TestsRetrieveUpdateDelete
urlpatterns = [
    path('get/', TestsListView.as_view(), name='subjects-list-create'),
    path('post/', TestsListCreate.as_view(), name='subjects-list-create'),
    path('set/<uuid:pk>/', TestsRetrieveUpdateDelete.as_view(), name='subjects-retrieve-update-delete')
]
