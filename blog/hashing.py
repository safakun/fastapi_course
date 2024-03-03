from passlib.context import CryptContext

pwd_txt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def bcrypt(password: str):
        return pwd_txt.hash(password)