from models.user import find_user_by_username
from utils.helpers import validate_password

def login():
    username = input("username:")
    password = input("password:")
    user = find_user_by_username(username)
    if user:
        existing_hash = user['password_hash']
        validate_password(existing_hash,password)
    else:
        print("Credentials are incorrect")
