from django.urls import path

from exam_prep_1.albums.views import  CreateAlbumView, DetailsAlbumView, EditAlbumView, DeleteAlbumView

urlpatterns = (
    path('create/', CreateAlbumView.as_view(), name='album create'),
    path('<int:pk>/details/', DetailsAlbumView.as_view(), name='album details'),
    path('<int:pk>/edit/', EditAlbumView.as_view(), name='album edit'),
    path('<int:pk>/delete/', DeleteAlbumView.as_view(), name='album delete'),
)