from django.urls import path

from exam3.profiles import views
from exam3.web.views import IndexView, CreateExpenseView, UpdateExpenseView, DeleteExpenseView

urlpatterns = (

    path('', IndexView.as_view(), name='index'),
    path('create/', CreateExpenseView.as_view(), name='create expense'),
    path('edit/<int:pk>/', UpdateExpenseView.as_view(), name='edit expense'),
    path('delete/<int:pk>/', DeleteExpenseView.as_view(), name='delete expense'),

)