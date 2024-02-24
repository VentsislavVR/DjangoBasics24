from django.views import generic as views

from racing.cars.models import Car
from racing.profiles.models import Profile


class IndexView(views.ListView):
    model = Profile
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context


class CatalogueView(views.ListView):
    queryset = Car.objects.all()
    template_name = "web/catalogue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = Car.objects.all()
        context["profile"] = Profile.objects.first()
        return context
