from sqlalchemy import Column, Integer, String
from db.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(120), unique=True)

    def __init__(self, username, first_name, last_name, email_address):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def __repr__(self):
        return "<User> {} {}".format(self.first_name, self.last_name)
