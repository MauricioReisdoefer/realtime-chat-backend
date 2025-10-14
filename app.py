from flask import Flask
from database import db
from routes.user_routes import user_bp
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(user_bp)

db.init_app(app)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)