from pydantic import BaseModel


class UserSerializer(BaseModel):
    username: str
    password: str


class ChangePasswordSerializer(BaseModel):
    username: str
    password: str
