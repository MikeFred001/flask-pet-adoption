"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, URL

IMAGE_URL = "https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Ftimes%2Fprodmigration%2Fweb%2Fbin%2F5ca5cbde-984c-328c-97f5-3805b28ebb87.jpg?crop=1500%2C1000%2C0%2C0"


class AddPetForm(FlaskForm):
    """Class for add pet form"""

    name = StringField(
        "Name",
        validators=[InputRequired()])

    species = StringField(
        "Species",
        validators=[InputRequired(),
                    AnyOf(["cat","dog","porcupine"],
                          message="Invalid Pet")])
    # Select field
    photo_url = StringField(
        "Photo URL",
        default=IMAGE_URL,
        validators=[Optional(), URL(message = "Must be a URL")])

    age = StringField(
        "Age",
        validators=[
            InputRequired(),
            AnyOf(["baby","young","adult",'senior'], message="Invalid Age")])

    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Class for add pet form"""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL(message = "Must be a URL")])

    notes = StringField("Notes")

    available = BooleanField("Available", default=True)