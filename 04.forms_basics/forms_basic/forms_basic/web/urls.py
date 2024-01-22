from django.urls import path

from forms_basic.web.views import index, index_models

urlpatterns=(
    path('',index,name='index'),
    path('models/',index_models,name='index_models'),
    path('modelforms/<int:pk>/',index_models,name='update_employee'),
)