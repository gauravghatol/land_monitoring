from app import db
from geoalchemy2 import Geometry

class LandUse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    geom = db.Column(Geometry('POLYGON'))
