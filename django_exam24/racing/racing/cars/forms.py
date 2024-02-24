from django import forms

from racing.cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['class'] = 'readonly'

    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        widgets = {
            'type': forms.TextInput(attrs={'readonly': True, 'class': 'readonly'}),
        }
