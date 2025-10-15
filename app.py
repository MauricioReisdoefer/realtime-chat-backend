from flask import Flask, jsonify
from database import db
from routes.user_routes import user_bp
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/index")
def index():
    return jsonify({"message":"on"})

CORS(app)   
db.init_app(app) 

with app.app_context():
    db.create_all()
    
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
