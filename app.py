
from flask import Flask, request, render_template, redirect
from models import db, connect_db, Pet
from forms import petForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

connect_db(app)
db.create_all()


@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


def add_pet():
    form = petForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
