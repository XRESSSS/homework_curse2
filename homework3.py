import datetime

import jwt

import settings

payload = {
    "my_name": "Evgeny",
    "age": 16,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=15),
}


def encode_jwt(playload_data: dict) -> str:
    return jwt.encode(
        payload=playload_data,
        key=settings.JWT_SECRET,
        algorithm="HS256",
    )


def decoded_jwt(encoded_jwt_str: str) -> dict:
    try:
        return jwt.decode(
            encoded_jwt_str,
            settings.JWT_SECRET,
            algorithms=["HS256"],
        )
    except jwt.exceptions.ExpiredSignatureError:
        return {}
    except jwt.exceptions.InvalidSignatureError:
        return {}


data = encode_jwt(payload)

result = decoded_jwt(data)
