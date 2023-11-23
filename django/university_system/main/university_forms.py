from django import forms


class UniversityForm(forms.Form):
    full_name = forms.CharField(label='Полное название:', label_suffix='')
    small_name = forms.CharField(label='Сокращенное название:', label_suffix='')
    date = forms.DateField(
        label='Дата создания:',
        label_suffix='',
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'class': 'datepicker'}
        )
    )
