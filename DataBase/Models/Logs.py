import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from DataBase.database_connection import Base

class Log(Base):
    __tablename__ = 'Logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    grams = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, user_id, grams):
        self.user_id = user_id
        self.grams = grams

    def as_dict(self):
        return {
            'id': self.id,
            'grams': self.grams,
            'created_at': self.created_at,
        }