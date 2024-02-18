from django.urls import path

from exam_prep_1.profiles import views

urlpatterns = (
    path('',views.IndexView.as_view(), name='index'),
    path('profile/details/', views.ProfileDetailsView.as_view(), name='profile details'),
    path('profile/delete/', views.ProfileDeleteView.as_view(), name='profile delete'),

)