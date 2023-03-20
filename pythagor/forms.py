from django import forms

from .models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['first_name', 'last_name', 'email']


class Pythagor(forms.Form):
    side_a = forms.IntegerField(label='lengths of the side "a"', help_text='cm', min_value=1)
    side_b = forms.IntegerField(label='lengths of the side "b"', help_text='cm', min_value=1)
