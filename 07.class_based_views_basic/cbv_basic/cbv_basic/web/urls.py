from django.urls import path
from django.views.generic import TemplateView

from cbv_basic.web.views import index, IndexView, TodoCreateView, TodoDetailsView, IndexRawView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
    path("initkwargs/", TemplateView.as_view(template_name="web/index.html")),

    path("todos/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todos/<int:pk>/", TodoDetailsView.as_view(), name="todo_details"),

    path("raw/", IndexRawView.as_view(), name="index_raw"),
    path("raw/<int:pk>/", IndexRawView.as_view(), name="index_raw_with_pk"),)