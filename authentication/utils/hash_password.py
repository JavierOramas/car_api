import bcrypt

def hash_password(password, salt):
    return bcrypt.hashpw(password, salt)