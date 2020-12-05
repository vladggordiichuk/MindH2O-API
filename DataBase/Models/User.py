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
    user_settings = relationship("UserSettings")
    logs = relationship("Log")