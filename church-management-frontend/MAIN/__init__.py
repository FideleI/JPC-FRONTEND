from flask import Flask
from flask_login import LoginManager
import os 

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    with app.app_context():
        # Include our Routes
        from .HOME  .routes import index_bp
        from .AUTH  .routes import auth_bp
        from .DASH  .routes import dash_bp
        from .MEMBER  .routes import member_bp

        # Register Blueprints
        app.register_blueprint(index_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(dash_bp)
        app.register_blueprint(member_bp)
        return app
        