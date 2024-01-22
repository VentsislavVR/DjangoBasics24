from django import forms

from forms_basic.web.models import Employee


class DemoForm(forms.Form):
    first_name = forms.CharField(
        max_length=35,
        required=False,
        label='First Name:',
        help_text='Enter your first name',
        # disabled=True,

    )

    last_name = forms.CharField(
        max_length=35,
        required=False,
        label='Last Name:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your last name'
            }
        ),
    )

    email = forms.EmailField(
        required=False,
    )

    age = forms.IntegerField(
        required=False

    )
    INTERESTS = (
        (1, 'Programming'),
        (2, 'Cooking'),
        (3, 'Traveling'),
        (4, 'Gaming'),
        (5, 'Reading'),
    )

    interests = forms.ChoiceField(
        choices=INTERESTS,
        required=False
    )
    interests2 = forms.IntegerField(
        widget=forms.Select(choices=INTERESTS),
        required=False,
    )

    interests3 = forms.IntegerField(
        widget=forms.RadioSelect(choices=INTERESTS),
        required=False,
    )

    interests4 = forms.IntegerField(
        widget=forms.CheckboxSelectMultiple(choices=INTERESTS),
        required=False,
    )


class EmployeeForm(forms.ModelForm):
    department = forms.CharField(
        max_length=35,
    )


    class Meta:
        model = Employee
        fields = '__all__'


        labels = {

            'first_name': 'First Name:',
            'last_name': 'Last Name:',
        }

        widgets = {
            'role': forms.RadioSelect(
                # attrs={
                #     'disabled': 'disabled',
                #
                # }
            ),

        }





