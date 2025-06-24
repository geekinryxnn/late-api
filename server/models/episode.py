from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', backref='episode', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'number': self.number,
            'appearances': [appearance.to_dict() for appearance in self.appearances]
        }