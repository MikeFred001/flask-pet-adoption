"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, Email

class AddPetForm(FlaskForm):
    """Class for add pet form"""

    name = StringField(
        "Name",
        validators=[InputRequired()])

    species = StringField(
        "Species",
        validators=[InputRequired()])

    photo_url = StringField(
        "Photo URL",
        validators=[InputRequired()])

    age = StringField(
        "Age",
        validators=[InputRequired()])

    notes = StringField(
        "Notes",
        validators=[InputRequired()])