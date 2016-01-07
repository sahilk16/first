from db.database import db_session
from db.models.user_model import User


def create_user(user_obj):
    db_session.add(user_obj)
