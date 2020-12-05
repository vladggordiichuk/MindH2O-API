import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from DataBase.database_connection import Base

class Log(Base):
    __tablename__ = 'Logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    grams = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)