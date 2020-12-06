from secrets import token_urlsafe

from DataBase.Models.Logs import Log
from DataBase.Models.User import User
from DataBase.Models.UserAuth import UserAuth
from DataBase.Models.UserSettings import UserSettings

from DataBase.database_connection import session
from Extensions.security import pwd_context

def is_user_registered(email):
    return session.query(User).filter(User.email == email).first() is not None


def save_user_to_database(first_name, last_name, email, password):
    user = User(first_name,
                last_name,
                email,
                pwd_context.encrypt(password))
    session.add(user)
    session.commit()
    return user


def create_user_auth(user):
    auth = UserAuth(user.id, token_urlsafe(30))
    session.add(auth)
    session.commit()
    return auth


def get_user_by_email_and_password(email, password):
    user = session.query(User) \
        .filter(User.email == email) \
        .first()

    if user is not None:
        if pwd_context.verify(password, user.password):
            return user
    return None


def check_user_token(auth_token):
    if auth_token is not None:
        return session.query(User) \
            .filter(User.id == UserAuth.user_id, UserAuth.token == auth_token) \
            .first()
    else:
        return None


def remove_user_auth(auth_token):
    session.query(UserAuth) \
        .filter(UserAuth.token == auth_token) \
        .delete()
    session.commit()
    return True


def update_user_settings(user, daily_activity_minutes, body_weight_grams):

    user_settings_in_db = session.query(UserSettings) \
        .filter(UserSettings.user_id == user.id) \
        .first()

    if user_settings_in_db is not None:
        user_settings_in_db.daily_activity_minutes = daily_activity_minutes
        user_settings_in_db.body_weight_grams = body_weight_grams
        session.commit()
        return user_settings_in_db
    else:
        settings = UserSettings(user.id, daily_activity_minutes, body_weight_grams)
        session.add(settings)
        session.commit()
        return settings


def add_log(user, grams):
    log = Log(user.id, grams)
    session.add(log)
    session.commit()
    return log


def remove_log(user, id):
    log = session.query(Log) \
        .filter(Log.user_id == user.id, Log.id == id) \
        .first()

    if log is not None:
        session.delete(log)
        session.commit()
        return True
    else:
        return False


def get_logs(user):
    return session.query(Log) \
        .filter(Log.user_id == user.id) \
        .order_by(Log.created_at.desc()) \
        .all()
