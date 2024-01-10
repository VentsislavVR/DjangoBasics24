from django.urls import path

from django101.tasks.views import index

urlpatterns = (
    path('', index, name='index'),
)