# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('Enter your name:', validators=[DataRequired()])
    age = StringField('Enter your age:', validators=[DataRequired()])
    gender = StringField('Enter your gender:', validators=[DataRequired()])
    submit = SubmitField('Submit')
