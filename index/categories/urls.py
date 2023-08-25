from django.urls import path
from .views import CategoriesListCreate, CategoriesListView, CategoriesRetrieveUpdateDelete

urlpatterns = [
    path('get/', CategoriesListView.as_view(), name='userprofile-list-create'),
    path('post/', CategoriesListCreate.as_view(), name='userprofile-list-create'),
    path('set/<uuid:pk>/', CategoriesRetrieveUpdateDelete.as_view(), name='userprofile-retrieve-update-delete')
]
