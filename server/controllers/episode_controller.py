from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ..models.episode import Episode
from ..models.appearance import Appearance
from ..models import db

episode_controller = Blueprint('episode_controller', __name__)

@episode_controller.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        "id": e.id,
        "date": e.date.isoformat(),
        "number": e.number
    } for e in episodes]), 200

@episode_controller.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": [{
            "id": a.id,
            "rating": a.rating,
            "guest_id": a.guest_id
        } for a in appearances]
    }), 200

@episode_controller.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"msg": "Episode deleted successfully"}), 200