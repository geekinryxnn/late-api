from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from controllers.guest_controller import guest_bp
from controllers.episode_controller import episode_bp
from controllers.appearance_controller import appearance_bp
from controllers.auth_controller import auth_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(guest_bp, url_prefix='/guests')
app.register_blueprint(episode_bp, url_prefix='/episodes')
app.register_blueprint(appearance_bp, url_prefix='/appearances')
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
