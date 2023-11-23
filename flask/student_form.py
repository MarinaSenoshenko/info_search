from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    name = StringField('ФИО:', validators=[DataRequired()])
    date = DateField('Дата рождения:', format='%Y-%m-%d', validators=[DataRequired()])
    university = IntegerField('Университет:', validators=[DataRequired()])
    year = IntegerField('Год поступления:', validators=[DataRequired()])
