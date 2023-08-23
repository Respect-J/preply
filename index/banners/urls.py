from django.urls import path
from .views import BannersListView, BannersListCreate, BannersRetrieveUpdateDelete

urlpatterns = [
    path('get/', BannersListView.as_view(), name='banners-list-create'),
    path('post/', BannersListCreate.as_view(), name='banners-list-create'),
    path('banners/<uuid:pk>/', BannersRetrieveUpdateDelete.as_view(), name='banners-retrieve-update-delete')
]
