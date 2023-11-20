from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, Optional, URL, DataRequired


class petForm(FlaskForm):
    """Form for adding pets."""


class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
                       InputRequired(), DataRequired(), Length(min=2, max=100)])
    species = StringField("Species", validators=[
                          InputRequired(), DataRequired(), Length(min=2, max=100)])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    available = BooleanField("Available")
