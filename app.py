from flask import Flask
from db import db, init_db
from routes.auth import auth_bp
from routes.shopping import shopping_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
init_db(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(shopping_bp, url_prefix="/shop")

if __name__ == "__main__":
    app.run(debug=True)