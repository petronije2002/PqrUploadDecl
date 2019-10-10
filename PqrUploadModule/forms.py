from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField, DecimalField, FileField
from wtforms.validators import Required
# from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired

class DelcarationForm(FlaskForm):

    date_ = DateField(label='date_')

    description123 = StringField(label='description123')

    excl_btw = DecimalField(label='excl_btw')

    btw = DecimalField(label='btw')

    incl_btw = DecimalField(label='incl_btw')

    file_ = FileField(label='file_')

    submit = SubmitField(label='submit')

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])