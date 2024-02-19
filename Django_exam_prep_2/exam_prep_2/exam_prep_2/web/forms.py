from django import forms

from exam_prep_2.web.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter username'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }
            ),
        }

class ReadOnlyPlantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['class'] = 'readonly'  # Add a CSS class for styling

    class Meta:
        model = Plant
        fields = ['plant_type', 'name', 'image_url', 'description', 'price']
        widgets = {
            'plant_type': forms.TextInput(attrs={'readonly': True, 'class': 'readonly'}),
        }