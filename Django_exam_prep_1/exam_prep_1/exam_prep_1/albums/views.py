from django.forms import TextInput, Textarea, NumberInput, URLInput, model_to_dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam_prep_1.albums import forms
from exam_prep_1.albums.forms import AlbumCreateForm
from exam_prep_1.albums.models import Album
from exam_prep_1.profiles.models import Profile


# Create your views here.


class CreateAlbumView(views.CreateView):
    model = Album
    template_name = 'albums/album-add.html'

    form_class = forms.AlbumCreateForm

    def get_success_url(self):
        # Return the URL of the 'index' view in the other app
        return reverse_lazy('index')

    def form_valid(self, form):
        album = form.save(commit=False)
        album.owner = Profile.objects.first()
        album.save()
        return super().form_valid(form)


class DetailsAlbumView(views.DetailView):
    model = Album
    template_name = 'albums/album-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = self.object  # Use self.object to access the album object
        return context


class EditAlbumView(views.UpdateView):
    model = Album
    template_name = 'albums/album-edit.html'
    fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['album_name'].widget = TextInput(attrs={'placeholder': 'Album Name'})
        form.fields['artist'].widget = TextInput(attrs={'placeholder': 'Artist'})
        form.fields['genre'].widget = TextInput(attrs={'placeholder': 'Genre'})
        form.fields['description'].widget = Textarea(attrs={'placeholder': 'Description'})
        form.fields['image_url'].widget = URLInput(attrs={'placeholder': 'Image URL'})
        form.fields['price'].widget = NumberInput(attrs={'placeholder': 'Price'})
        return form


class DeleteAlbumView(views.DeleteView):
    model = Album
    template_name = 'albums/album-delete.html'

    form_class = AlbumCreateForm  # Assuming AlbumCreateForm is your form class
    pk_url_kwarg = 'pk'

    success_url = reverse_lazy('index')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs


