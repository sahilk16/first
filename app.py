from flask import Flask, Blueprint
from flask_restful import Api
from resources.user import User

app = Flask(__name__)
api_blueprint = Blueprint('api', __name__)
api = Api(app)

api.add_resource(User, '/User', '/user/<int:id>')
app.register_blueprint(api_blueprint)
