from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from DataBase.database_connection import Base

class UserAuth(Base):
    __tablename__ = 'UserAuth'
    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    token = Column('token', VARCHAR(100))

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def as_dict(self):
        return {
            'token': self.token
        }