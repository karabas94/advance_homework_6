from django import forms


class Pythagor(forms.Form):
    side_a = forms.IntegerField(label='lengths of the side "a"', help_text='cm', min_value=1)
    side_b = forms.IntegerField(label='lengths of the side "b"', help_text='cm', min_value=1)
