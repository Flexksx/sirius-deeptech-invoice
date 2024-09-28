from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# Import your controllers
from backend.src.view.ClientController import client_blueprint
from backend.src.view.ContractController import contract_blueprint

app = Flask(__name__)

# Config for SQLAlchemy (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Register the controllers (blueprints)
app.register_blueprint(client_blueprint, url_prefix="/api/clients")
app.register_blueprint(contract_blueprint, url_prefix="/api/contracts")

# Root route (optional)
@app.route('/')
def index():
    return "Welcome to the API. Try /api/clients or /api/contracts"

if __name__ == "__main__":
    app.run(debug=True)
