from django.urls import path, include

from racing.cars.views import CarCreateView, CarDetailsView, CarUpdateView, CarDeleteView

urlpatterns = (
    path('create/', CarCreateView.as_view(), name='car create'),
    path('<int:pk>/', include([
        path('details/', CarDetailsView.as_view(), name='car details'),
        path('edit/', CarUpdateView.as_view(), name='car edit'),
        path('delete/', CarDeleteView.as_view(), name='car delete'),

    ])
         )
)
