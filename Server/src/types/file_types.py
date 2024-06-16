from pydantic import BaseModel

class CreateFileDto(BaseModel) : 
    name : str 
    path : str 
    type : str  
    size : str  