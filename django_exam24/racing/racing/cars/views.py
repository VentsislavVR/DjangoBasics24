from django.urls import reverse, reverse_lazy
from django.views import generic as views

from racing.cars.forms import CarCreateForm, CarDeleteForm
from racing.cars.models import Car
from racing.common.utils import get_profile


class CarCreateView(views.CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/car-create.html'

    def get_success_url(self):
        return reverse('catalogue')

    def form_valid(self, form):
        profile = get_profile()
        form.instance.owner = profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class CarDetailsView(views.DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class CarUpdateView(views.UpdateView):
    queryset = Car.objects.all()
    template_name = 'cars/car-edit.html'
    form_class = CarCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context

    def get_success_url(self):
        return reverse('catalogue')


class CarDeleteView(views.DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'

    form_class = CarDeleteForm

    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object

        return kwargs
