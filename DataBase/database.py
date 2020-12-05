from DataBase.database_connection import Base, engine

import DataBase.Models.User
import DataBase.Models.UserAuth
import DataBase.Models.UserSettings
import DataBase.Models.Logs

Base.metadata.create_all(engine)