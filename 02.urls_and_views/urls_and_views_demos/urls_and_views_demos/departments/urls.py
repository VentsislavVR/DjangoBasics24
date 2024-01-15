from django.urls import path

from urls_and_views_demos.departments.views import department_details, department_details_by_name

urlpatterns = (

    path('<int:pk>/', department_details), # departments/<int:pk>
    path('departments/<str:name>/', department_details_by_name), # departments/departments/<str:name>
)