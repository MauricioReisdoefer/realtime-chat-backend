from flask import Flask, jsonify
from database import db
from routes.user_routes import user_bp
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'isso_nao_eh_seguro_mas_vou_mudar'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)

@app.route("/index")
def index():
    return jsonify({"message":"on"})

CORS(app)   
db.init_app(app) 

with app.app_context():
    db.create_all()
    
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
