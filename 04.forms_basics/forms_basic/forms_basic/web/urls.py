from django.urls import path

from forms_basic.web.views import index, index_models, update_employee

urlpatterns=(
    path('',index,name='index'),
    path('modelforms/',index_models,name='index_models'),
    path('modelforms/<int:pk>/',update_employee,name='update_employee'),
)