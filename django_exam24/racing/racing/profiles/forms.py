from django import forms

from racing.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
        help_texts = {
            'age': 'Age requirement: 21 years and above.'
        }


class ProfileUpdateForm(ProfileBaseForm):
    pass
