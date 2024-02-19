from django.urls import path

from exam_prep_2.web.views import IndexView, ProfileCreateView, ProfileDetailsView, ProfileEditView, ProfileDeleteView, \
    CatalogueView, PlantCreateView, PlantEditView, PlantDetailsView, PlantDeleteView

urlpatterns = (
    path('',IndexView.as_view(), name='index'),
    # Profile
    path('profile/create/', ProfileCreateView.as_view(), name='profile create'),
    path('profile/details/',ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile edit'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile delete'),
    # Catalogue
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    # Plant
    path('create/', PlantCreateView.as_view(), name='plant create'),
    path('details/<int:pk>/', PlantDetailsView.as_view(), name='plant details'),
    path('edit/<int:pk>/', PlantEditView.as_view(), name='plant edit'),
    path('delete/<int:pk>/', PlantDeleteView.as_view(), name='plant delete'),



)




