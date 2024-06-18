from flask import Blueprint, jsonify, request
from app import db
from app.models import LandUse

bp = Blueprint('main', __name__)

@bp.route('/land_use', methods=['GET'])
def get_land_use():
    land_uses = LandUse.query.all()
    results = [{"id": lu.id, "name": lu.name, "geom": lu.geom} for lu in land_uses]
    return jsonify(results)

@bp.route('/land_use', methods=['POST'])
def add_land_use():
    data = request.get_json()
    name = data['name']
    geom = data['geom']
    new_land_use = LandUse(name=name, geom=geom)
    db.session.add(new_land_use)
    db.session.commit()
    return jsonify({"message": "Land use added successfully"}), 201
