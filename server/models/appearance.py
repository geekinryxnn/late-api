from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.validate_rating()

    def validate_rating(self):
        if not 1 <= self.rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'guest_id': self.guest_id,
            'episode_id': self.episode_id
        }