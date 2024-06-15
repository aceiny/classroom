from pydantic import BaseModel , EmailStr
from enum import Enum

class Gender(Enum):
    Male = "Male"
    Female = "Female"

class UserRole(Enum) : 
    Student = "Student"
    Professeur = "Professeur"

class UserLoginDto(BaseModel) : 
    email : EmailStr
    password : str

class UserRegisterDto(BaseModel) : 
    name : str 
    email : EmailStr 
    password : str
    gender : Gender
    role : UserRole

class SignInOut(BaseModel):
    token: str
    id : str
