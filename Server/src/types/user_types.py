from pydantic import BaseModel
class UserLoginDto(BaseModel) : 
    username : str 
    password : str

class UserRegisterDto(BaseModel) : 
    username : str 
    password : str
    name : str
    gender : str

class SignInOut(BaseModel):
    token: str
    id : str