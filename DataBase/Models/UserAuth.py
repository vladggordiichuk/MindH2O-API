from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from DataBase.database_connection import Base

class UserAuth(Base):
    __tablename__ = 'UserAuth'
    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    token = Column('token', VARCHAR(100))