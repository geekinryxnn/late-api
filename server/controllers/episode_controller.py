from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import Episode, Appearance, db
from datetime import datetime

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number
    } for episode in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [{
        'id': a.id,
        'rating': a.rating,
        'guest': {
            'id': a.guest.id,
            'name': a.guest.name,
            'occupation': a.guest.occupation
        }
    } for a in episode.appearances]
    
    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': appearances
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode deleted successfully"}), 200