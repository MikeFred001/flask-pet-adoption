"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, URL



class AddPetForm(FlaskForm):
    """Class for add pet form"""

    name = StringField(
        "Name",
        validators=[InputRequired()])

    species = StringField(
        "Species",
        validators=[InputRequired(), AnyOf(["cat","dog","porcupine"], message="Invalid Pet")])

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL(message = "Must be a URL")])

    age = StringField(
        "Age",
        validators=[InputRequired(), AnyOf(["baby","young","adult",'senior'], message="Invalid Age")])

    notes = StringField(
        "Notes",
        validators=[InputRequired()])