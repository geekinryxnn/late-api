from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import Appearance, Guest, Episode, db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        appearance.validate_rating()
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    
    # Check if guest and episode exist
    if not Guest.query.get(data['guest_id']):
        return jsonify({"error": "Guest not found"}), 404
    if not Episode.query.get(data['episode_id']):
        return jsonify({"error": "Episode not found"}), 404
    
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201