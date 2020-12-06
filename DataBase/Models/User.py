from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from DataBase.database_connection import Base

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(100))
    last_name = Column(VARCHAR(100))
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(255))
    user_auth = relationship("UserAuth")
    user_settings = relationship("UserSettings", uselist = False, back_populates = "user")
    logs = relationship("Log")

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def as_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'user_settings': self.user_settings.as_dict()
        }