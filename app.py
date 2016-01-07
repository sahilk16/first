from flask import Flask, Blueprint
from flask_restful import Api
from resources.user import User
from db.database import db_session

app = Flask(__name__)
api_blueprint = Blueprint('api', __name__)
api = Api(app)

api.add_resource(User, '/User', '/user/<int:id>')
app.register_blueprint(api_blueprint)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
