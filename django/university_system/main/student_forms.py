from django import forms
from . import university_models


class StudentForm(forms.Form):
    name = forms.CharField(label='ФИО:', label_suffix='')
    date = forms.DateField(
        label='Дата рождения:',
        label_suffix='',
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'class': 'datepicker'}
        )
    )
    university = forms.ModelChoiceField(
        label='Университет:',
        label_suffix='',
        queryset=university_models.University.objects.all(),
        to_field_name='id'
    )
    year = forms.IntegerField(label='Год поступления:', label_suffix='')