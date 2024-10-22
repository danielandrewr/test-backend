from passlib.context import CryptContext

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(password, hashed):
    return crypt_context.verify(password, hashed)

def get_password_hashed(password):
    return crypt_context.hash(password)