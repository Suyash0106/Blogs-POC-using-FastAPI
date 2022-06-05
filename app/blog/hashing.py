from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_context.hash(password)

    def verify(normal_password, hashed_password):
        return pwd_context.verify(normal_password, hashed_password)