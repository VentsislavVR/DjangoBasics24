from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from exam_doncho.albums.models import Album
from exam_doncho.common.profile_helpers import get_profile
from exam_doncho.profiles.models import Profile



class AlbumFormViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs['placeholder'] = Album._meta.get_field('name').verbose_name
        form.fields['artist_name'].widget.attrs['placeholder'] = 'Artist Name'
        form.fields['genre'].widget.attrs['placeholder'] = 'Genre'
        form.fields['description'].widget.attrs['placeholder'] = 'Description'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        form.fields['price'].widget.attrs['placeholder'] = 'Price'
        return form


class ReadonlyViewMixin(views.DetailView):
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field in form.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
            # field.widget.attrs['disabled'] = 'disabled'

        return form


# Create your views here.
class CreateAlbum(AlbumFormViewMixin, views.CreateView):
    queryset = Album.objects.all()

    fields = ('name', 'artist_name',
              'genre', 'description',
              'image_url', 'price')
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs['placeholder'] = Album._meta.get_field('name').verbose_name
        form.fields['artist_name'].widget.attrs['placeholder'] = 'Artist Name'
        form.fields['genre'].widget.attrs['placeholder'] = 'Genre'
        form.fields['description'].widget.attrs['placeholder'] = 'Description'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        form.fields['price'].widget.attrs['placeholder'] = 'Price'
        return form

    def form_valid(self, form):
        # instance = form.save(commit=False)
        form.instance.owner = get_profile().pk
        # instance.owner = get_profile()
        # return super().form_valid(form)
        return super().form_valid(form)


class DetailsAlbum(views.DetailView):
    queryset = Album.objects.all()
    template_name = 'albums/album-details.html'


class EditAlbum(AlbumFormViewMixin, views.UpdateView):
    queryset = Album.objects.all()

    template_name = 'albums/album-edit.html'

    fields = ('name', 'artist_name',
              'genre', 'description',
              'image_url', 'price')

    success_url = reverse_lazy('index')


class DeleteAlbum(ReadonlyViewMixin, views.DeleteView):
    queryset = Album.objects.all()
    template_name = 'albums/album-delete.html'

    success_url = reverse_lazy('index')
    form_class = modelform_factory(
        Album,
        fields=('name', 'artist_name', 'genre', 'description', 'image_url', 'price')
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object

        return kwargs


