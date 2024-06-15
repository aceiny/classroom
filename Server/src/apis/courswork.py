import src.apis
from typing import List
from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.utils.auth import JWTBearer, decodeJWT
from src.apis.auth import router
from src.types.classroom_types import CreateClassRoomDto, UpdateClassRoomDto

router = APIRouter(
    prefix="/courswork",
    tags=["courswork"],
    responses={404: {"description": "Not found"}},
)

@router.get('/{classroomId}')
async def get_classroom_all_coursworks(classroomId : str):
    classroom = await prisma.classroom.find_unique(
        where = {
            id : classroomId
        }
    )
    if not classroom : 
        raise HTTPException(status_code=404, detail="Classroom not found")
    coursworks = await prisma.courswork.find_many(
        where = {
            classroomId : classroomId
        }
    )

@router.post('/{classroomId}')
async def add_coursework( classroomId : str , coursework : CreateClassRoomDto):
    classroom = await prisma.classroom.find_unique(
        where = {
            id : coursework.classroomId
        }
    )
    if not classroom : 
        raise HTTPException(status_code=404, detail="Classroom not found")
    created = await prisma.courswork.create(
        {
            "title" : coursework.title,
            "description": coursework.description,
            "classroomId": classroomId,
            
        }
    )
    if created : 
        return created
    raise HTTPException(status_code=404, detail="Coursework creation failed")