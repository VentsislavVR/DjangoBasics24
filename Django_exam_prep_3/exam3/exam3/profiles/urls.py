from django.urls import path

from exam3.profiles.views import DetailsProfileView,EditProfileView, DeleteProfileView


urlpatterns = (
    path('profile/', DetailsProfileView.as_view(), name='details profile'),
    path('edit/', EditProfileView.as_view(), name='edit profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete profile'),
)