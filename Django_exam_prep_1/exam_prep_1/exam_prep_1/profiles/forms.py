

from django import forms

from exam_prep_1.albums.models import Album
from exam_prep_1.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Album.objects\
             .all()\
             .delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()