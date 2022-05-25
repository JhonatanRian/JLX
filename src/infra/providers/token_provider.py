from datetime import datetime, timedelta
from jose import jwt

# Configs
SECRECT_KEY = "45c01a9f0e8e844270ffc7259adbbe8b"
ALGORITHN = "HS256"
ESPIRES_IN_MIN = 3000

def create_access_token(data: dict):
    infos = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=ESPIRES_IN_MIN)

    infos.update({"exp": expiration})

    token_jwt = jwt.encode(infos, SECRECT_KEY, algorithm=ALGORITHN)

    return token_jwt

def verify_access_token(token: str):
    payload = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHN])
    return payload.get("sub")