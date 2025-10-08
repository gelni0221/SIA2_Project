from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def validate_password(existing_hash,entered_password):
    ph = PasswordHasher()
    try:
        ph.verify(existing_hash, entered_password)
        print("Login Success")
    except VerifyMismatchError:
        print("Credentials are incorrect")