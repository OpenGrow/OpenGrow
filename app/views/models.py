from datetime import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from app import app
#app.config['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    passwordhash = db.Column(db.String(54))

    def __init__(self, name=None):
        self.set_password(password)

    def set_password(self, password):
        self.passwordhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordhash, password)

class Project(db.Model):
    __tablename__ = 'projects'     
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(30))
    img_path = db.Column(db.String(100))
    date = db.Column(db.DateTime)

    def __init__(self, name, description, img_path, date):
        self.name = name
        self.description = description
        self.img_path = img_path
        if date is None:
            date = datetime.utcnow()
        self.date = date

class Sensor(db.Model):
    __tablename__ = 'sensors'    
    id = db.Column(db.Integer, primary_key=True)
    projet_id = db.Column(db.Integer)
    sensor_type = db.Column(db.String(10))

    def __init__(self, sensor_type, projet_id):
        self.projet_id = projet_id
        self.sensor_type = sensor_type

class Sensor_value(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'sensors_values' 
    sensor_id = db.Column(db.Integer)
    value = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, value, projet_id, date):
        self.sensor_id = sensor_id
        self.value = value
        if date is None:
            date = datetime.utcnow()
        self.date = date

class Log(db.Model):
    __tablename__ = 'logs'     
    id = db.Column(db.Integer, primary_key=True)
    projet_id = db.Column(db.Integer)
    comm = db.Column(db.String(300))
    date = db.Column(db.DateTime)

    def __init__(self, projet_id, com, date):
        self.projet_id = projet_id
        self.comm = comm
        if date is None:
            date = datetime.utcnow()
        self.date = date

class Photo(db.Model):
    __tablename__ = 'photos'     
    id = db.Column(db.Integer, primary_key=True)
    projet_id = db.Column(db.Integer)
    photo = db.Column(db.String(300))
    date = db.Column(db.DateTime)

    def __init__(self, projet_id, photo, date):
        self.projet_id = projet_id
        self.photo = photo
        if date is None:
            date = datetime.utcnow()
        self.date = date

engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
db.Model.metadata.create_all(engine)
db.create_all()

#fail fix
#Project.__table__.drop(engine)