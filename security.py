from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password): #return user object if password is correct
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user             # returned user used to generate token

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)