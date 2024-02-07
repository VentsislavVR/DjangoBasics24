from django.urls import path

from cbv_basic.custom_cbv.views import index, IndexView

urlpatterns = (
    path("", index, name='ccbc_index'),
    path("cbv/", IndexView.as_view(), name='ccbc_cbv_index'),
)