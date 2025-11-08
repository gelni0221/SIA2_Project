# These codes are only for testing purposes'
from models.user import find_user_by_username

# from controllers.auth_controller import login
#
# username = input("user:")
# password = input("pass:")
# login(username,password)

user = input("Enter User:")
print(find_user_by_username(user))


