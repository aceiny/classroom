import src.apis
from typing import List
from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.utils.auth import JWTBearer, decodeJWT
from src.apis.auth import router
from src.types.classroom_types import CreateClassRoomDto

router = APIRouter(
    prefix="/classroom",
    tags=["classroom"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', tags=["classroom"])
async def read_classrooms():
    classrooms = await prisma.classroom.find_many()
    return classrooms


@router.get('/me', tags=["classroom"])
async def read_joined_classrooms() : 
    userId = "clxgbavm30000bi7w2sae11kn"
    enrollment = await prisma.enrollment.find_many(
        where={
            "membreId": userId 
        },
        include={
            "classroom": True
        }
    )
    return enrollment

@router.post('/')
async def create_classroom(classroom : CreateClassRoomDto) : 
    userId = "clxgbavm30000bi7w2sae11kn"
    classroom = await prisma.classroom.create({
        "name": classroom.name,
        "professorId": userId
    })
    if classroom : 
        return classroom