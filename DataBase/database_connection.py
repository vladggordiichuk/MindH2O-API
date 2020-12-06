import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import Config.config as config

engine = create_engine('mysql+pymysql://' + config.mysql_user + ':' +
                       config.mysql_password + '@' +
                       config.mysql_host + ':' +
                       config.mysql_port + '/' +
                       config.mysql_database, pool_recycle=3600)

connection = engine.connect()
metadata = db.MetaData()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()