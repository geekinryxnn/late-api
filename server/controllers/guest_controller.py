from flask import Blueprint, jsonify
from ..models.guest import Guest

guest_controller = Blueprint('guest_controller', __name__)

@guest_controller.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        "id": g.id,
        "name": g.name,
        "occupation": g.occupation
    } for g in guests]), 200