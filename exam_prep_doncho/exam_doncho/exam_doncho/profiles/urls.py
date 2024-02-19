from django.urls import path

from exam_doncho.profiles import views

urlpatterns = (

    path('details/', views.DetailProfileView.as_view(), name='details profile'),
    path('delete/', views.DeleteProfileView.as_view(), name='delete profile'),

)