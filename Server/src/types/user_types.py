from pydantic import BaseModel
from enum import Enum


class Gender(Enum):
    Male = "male"
    Female = "female"

class UserLoginDto(BaseModel) : 
    username : str 
    password : str

class UserRegisterDto(BaseModel) : 
    username : str 
    password : str
    name : str
    gender : Gender

class SignInOut(BaseModel):
    token: str
    id : str
