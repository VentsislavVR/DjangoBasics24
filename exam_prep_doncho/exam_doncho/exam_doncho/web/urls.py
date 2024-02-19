from django.urls import path

from exam_doncho.web.views import index, create_profile

urlpatterns = (
    path('', index, name='index'),
    path('create-profile/', create_profile, name='create_profile'),
)