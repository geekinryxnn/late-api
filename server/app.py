
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from .models import db
from .controllers.auth_controller import auth_controller
from .controllers.episode_controller import episode_controller
from .controllers.guest_controller import guest_controller
from .controllers.appearance_controller import appearance_controller

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(auth_controller, url_prefix='/')
app.register_blueprint(episode_controller, url_prefix='/')
app.register_blueprint(guest_controller, url_prefix='/')
app.register_blueprint(appearance_controller, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
