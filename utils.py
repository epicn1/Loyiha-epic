import os
from datetime import datetime,timedelta
from jose import jwt
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHIM = os.getenv("ALGORITHIM")
BOT_USERNAME = os.getenv("BOT_USERNAME")
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=48)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHIM)
    return encoded_jwt
def get_tg_link(otb_code:str):
    return f"https://t.me/{BOT_USERNAME}?start={otb_code}"