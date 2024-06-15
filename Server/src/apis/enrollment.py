import src.apis
from typing import List
from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.utils.auth import JWTBearer, decodeJWT
from src.apis.auth import router
from src.types.classroom_types import CreateClassRoomDto

router = APIRouter(
    prefix="/enrollment",
    tags=["enrollment"],
    responses={404: {"description": "Not found"}},
)


@router.get('/me', tags=["enrollment"])
async def get_enrollments():
    userId = "clxgdek8c00007q5axo4hg1dc"
    enrollment = await prisma.enrollment.find_many(
        where={
            "membreId": userId 
        },
        include={
            "classroom": True,
        }
    )
    return enrollment
@router.post('/{classroomId}', tags=["enrollment"])
async def add_enrollment(classroomId : str):
    print(classroomId)
    userId = "clxgdek8c00007q5axo4hg1dc"
    classroom = await prisma.classroom.find_unique(
        where={
            "id": classroomId
            }
        )
    if not classroom : 
        raise HTTPException(status_code=404, detail="Classroom not found")
    
    enrollment_exists = await prisma.enrollment.find_first(
        where={
            "membreId": userId,
            "classroomId": classroomId
        }
    )
    if enrollment_exists:
        raise HTTPException(status_code=400, detail="Enrollment already exists")
    
    enrollment = await prisma.enrollment.create({
        "membreId": userId,
        "classroomId": classroomId
    })
    if not enrollment : 
        raise HTTPException(status_code=404, detail="Enrollment failed")
    return enrollment
