from django.urls import path, include

from exam_doncho.albums import views

urlpatterns = (
    path('add/', views.CreateAlbum.as_view(), name='create album'),
    path('<int:pk>/', include([
        path('details/', views.DetailsAlbum.as_view(), name='details album'),
        path('edit/', views.EditAlbum.as_view(), name='edit album'),
        path('delete/', views.DeleteAlbum.as_view(), name='delete album'),
    ])),
)