from django.urls import path,reverse

from urls_and_views_demos.core.views import index, redirect_to_soft, redirect_to_index, redirect_to_index_with_params, \
    raise_error, raise_exeption

urlpatterns = (
    # redirect
    path('soft/', redirect_to_soft),
    path('to-index/', redirect_to_index,name='redirect_to_index'),
    path('to-index-with-params/', redirect_to_index_with_params,name='redirect_to_index_with_params'),
    # Error
    path('raise-error/', raise_error, name='raise_error_with_response'),
    path('raise-exception/', raise_exeption, name='raise_exception'),

    # Normal
    path('', index, name='index_no_params'),
    path('<int:pk>/', index, name='index'),
    path('<slug:slug>', index, name='index'),
    path('<int:pk>/<slug:slug>', index, name='index_with_ok_and_slug',),
    path('<str:pk>/', index),

)
