"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)


# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def display_pets():
    """Displays homepage listing all pets"""

    pets = Pet.query.order_by("name").all()

    return render_template("pet_list.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add pet form; handle adding a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes
        )

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name} to Adoption List!")
        return redirect('/')

    else:
        return render_template("pet_add_form.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def display_pet_info(pet_id):
    """Displays information about a given pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url=form.photo_url.data
        notes=form.notes.data
        available=form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.commit()

        flash(f"Edited {pet.name} to Adoption List!")
        return redirect(f'/{pet.id}')
    else:
        return render_template("pet_info.html", pet=pet, form=form)