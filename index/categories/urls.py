from django.urls import path
from .views import CategoriesListCreate, CategoriesListView, CategoriesRetrieveUpdateDelete

urlpatterns = [
    path('get/', CategoriesListView.as_view(), name='categories-list-create'),
    path('post/', CategoriesListCreate.as_view(), name='categories-list-create'),
    path('set/<uuid:pk>/', CategoriesRetrieveUpdateDelete.as_view(), name='categories-retrieve-update-delete')
]
