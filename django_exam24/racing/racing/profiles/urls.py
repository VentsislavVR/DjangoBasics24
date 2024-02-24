from django.urls import path

from racing.profiles.views import ProfileDetailsView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView

urlpatterns = (

    path('create/', ProfileCreateView.as_view(), name='profile create'),
    path('details/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/', ProfileUpdateView.as_view(), name='profile update'),
    path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
)
