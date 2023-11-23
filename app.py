
from flask import Flask, request, render_template, redirect
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.app_context().push()

connect_db(app)
db.create_all()


@app.route('/')
def home():
    """Show homepage with list of pets."""
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Show add pet form and handle form submission."""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name=name, species=species, age=age,
                      notes=notes, available=available)
        if photo_url:  # Only set photo_url if it's not an empty string
            new_pet.photo_url = photo_url
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet(pet_id):
    """Show details about a pet."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    print(form.errors)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_details.html', pet=pet, form=form)


if __name__ == '__main__':
    app.run(debug=True)
