from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

class Character(db.Model):
    __tablename__ ='character'
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    url = db.Column(db.String(2000))

class Planet(db.Model):
    __tablename__ ='planets'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(200), nullable=False)
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(50))
    climate = db.Column(db.String(50))
    url = db.Column(db.String(2000))

class Favorite_Planets(db.Model):
    __tablename__ ='favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    id_planet = db.Column(db.Integer, ForeignKey('planets.id'))
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    
class Favorite_Characters(db.Model):
    __tablename__ ='favorites_characters'
    id = db.Column(db.Integer, primary_key=True)
    id_character = db.Column(db.Integer,  ForeignKey('character.id'))
    user_id = db.Column(db.Integer, ForeignKey('users.id'))