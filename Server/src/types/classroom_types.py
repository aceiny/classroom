from pydantic import BaseModel , EmailStr
from enum import Enum

class CreateClassRoomDto(BaseModel) : 
    name : str 

class UpdateClassRoomDto(BaseModel) : 
    name : str

