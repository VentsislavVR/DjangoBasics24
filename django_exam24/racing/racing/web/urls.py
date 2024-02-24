from django.urls import path

from racing.web.views import IndexView, CatalogueView

urlpatterns = (

    path('', IndexView.as_view(), name='index'),
    path('car/catalogue/', CatalogueView.as_view(), name='catalogue'),

)