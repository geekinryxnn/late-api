from server.app import app, db
from server.models import User, Guest, Episode, Appearance
from datetime import date

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create test user
        user = User(username="testuser")
        user.set_password("testpassword")
        db.session.add(user)
        
        # Create guests
        guests = [
            Guest(name="John Doe", occupation="Comedian"),
            Guest(name="Jane Smith", occupation="Actor"),
            Guest(name="Bob Johnson", occupation="Musician")
        ]
        db.session.add_all(guests)
        
        # Create episodes
        episodes = [
            Episode(date=date(2023, 1, 1), number=101),
            Episode(date=date(2023, 1, 8), number=102),
            Episode(date=date(2023, 1, 15), number=103)
        ]
        db.session.add_all(episodes)
        
        db.session.commit()
        
        # Create appearances
        appearances = [
            Appearance(rating=4, guest_id=1, episode_id=1),
            Appearance(rating=5, guest_id=2, episode_id=1),
            Appearance(rating=3, guest_id=3, episode_id=2),
            Appearance(rating=5, guest_id=1, episode_id=3)
        ]
        db.session.add_all(appearances)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()