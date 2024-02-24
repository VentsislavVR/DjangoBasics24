from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('racing.web.urls')),
    path('car/', include('racing.cars.urls')),
    path('profile/', include('racing.profiles.urls')),
]
