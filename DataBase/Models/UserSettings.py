from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from DataBase.database_connection import Base


class UserSettings(Base):
    __tablename__ = 'UserSettings'
    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship('User', back_populates='user_settings')
    daily_activity_minutes = Column('daily_activity_minutes', Integer)
    body_weight_grams = Column('body_weight_grams', Integer)

    def __init__(self, user_id, daily_activity_minutes, body_weight_grams):
        self.user_id = user_id
        self.daily_activity_minutes = daily_activity_minutes
        self.body_weight_grams = body_weight_grams

    def as_dict(self):
        return {
            'daily_activity_minutes': self.daily_activity_minutes,
            'body_weight_grams': self.body_weight_grams
        }