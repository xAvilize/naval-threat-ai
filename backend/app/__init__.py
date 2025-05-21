from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import api_bp  # ✅ must match Blueprint name in routes.py
    app.register_blueprint(api_bp)  # ✅ url_prefix already set in routes.py

    return app
