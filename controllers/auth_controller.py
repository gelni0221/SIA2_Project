from models.user import find_user_by_username
from utils.helpers import validate_password

def login(username, password):
    user = find_user_by_username(username)
    if user:
        existing_hash = user['password_hash']
        return validate_password(existing_hash,password)
    else:
        print("Credentials are incorrect")
