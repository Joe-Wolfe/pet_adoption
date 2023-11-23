from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, Optional, URL, DataRequired, AnyOf


class PetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet Name", validators=[
                       InputRequired(), DataRequired(), Length(min=2, max=100)])
    species = StringField("Species", filters=[lambda s: s.lower() if s else s], validators=[AnyOf(['cat', 'dog', 'porcupine'], message="Must be a cat, dog, or porcupine"),
                          InputRequired(), DataRequired(), Length(min=2, max=100)])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[
                       NumberRange(min=0, max=30), Optional()])
    notes = StringField("Notes")
    available = BooleanField("Available")


class EditPetForm(FlaskForm):
    """Form for editing pets."""
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available")
