from django import forms

from exam3.web.models import Expense


class ReadOnlyExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['class'] = 'readonly'  # Add a CSS class for styling

    class Meta:
        model = Expense
        fields = ['title', 'price', 'description', 'image_url']
        widgets = {
            'plant_type': forms.TextInput(attrs={'readonly': True, 'class': 'readonly'}),}