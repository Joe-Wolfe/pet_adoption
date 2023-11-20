from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet Model"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    species = db.Column(db.String(50), nullable=False)

    photo_url = db.Column(
        db.String, nullable=False, default='https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg')

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.String, nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)
