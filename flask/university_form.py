from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.widgets import Input


class UniversityForm(FlaskForm):
    full_name = StringField('Полное название:')
    small_name = StringField('Сокращенное название:')
    date = DateField('Дата создания:', widget=Input(input_type='date'))
