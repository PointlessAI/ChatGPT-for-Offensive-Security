import hashlib
import os

def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.sha256(salt + password.encode()).hexdigest()
    return key, salt

def verify_password(stored_password, stored_salt, password):
    key = hashlib.sha256(stored_salt + password.encode()).hexdigest()
    return key == stored_password

password = "mY$ecuReP@ssw0rd"

hashed_password, salt = hash_password(password)

input_password = "mY$ecuReP@ssw0rd"
is_valid = verify_password(hashed_password, salt, input_password)

print("Password is valid:", is_valid)
