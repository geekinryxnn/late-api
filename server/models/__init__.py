from server.app import db  # Import db from app.py

# Optional: import your models here too
from .guest import Guest
from .episode import Episode

__all__ = ['db', 'Guest', 'Episode']

