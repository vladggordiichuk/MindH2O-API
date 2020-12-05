from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from DataBase.database_connection import Base

class UserSettings(Base):
    __tablename__ = 'UserSettings'
    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    daily_activity_minutes = Column('daily_activity_minutes', Integer)
    body_weight_grams = Column('body_weight_grams', Integer)