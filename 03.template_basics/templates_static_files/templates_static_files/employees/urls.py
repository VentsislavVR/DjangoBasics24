from django.urls import path

from templates_static_files.employees.views import index

urlpatterns = (
    path('', index, name='index'),
)
