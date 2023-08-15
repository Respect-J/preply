from django.urls import path
from .views import UserProfileListView, UserProfileListCreate, UserProfileRetrieveUpdateDelete

urlpatterns = [
    path('get/', UserProfileListView.as_view(), name='userprofile-list-create'),
    path('post/', UserProfileListCreate.as_view(), name='userprofile-list-create'),
    path('userprofiles/<uuid:pk>/', UserProfileRetrieveUpdateDelete.as_view(), name='userprofile-retrieve-update-delete')
]
