import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
TOKEN_EXPIRE_IN_MINUTES = int(os.getenv("TOKEN_EXPIRE_IN_MINUTES"))