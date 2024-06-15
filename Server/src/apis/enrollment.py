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


@router.post('/{classroomId}', tags=["enrollment"])
async def add_enrollment(classroomId : str):
    print(classroomId)
    userId = "clxgbavm30000bi7w2sae11kn"
    classroom_id = "clxgcef8200013b18nu6uo0p8"
    classroom = await prisma.classroom.find_unique(where={"id": classroom_id})
    if not classroom : 
        raise HTTPException(status_code=404, detail="Classroom not found")
    enrollment = await prisma.enrollment.create({
        "membreId": userId,
        "classroomId": classroom_id
    })
    if not enrollment : 
        raise HTTPException(status_code=404, detail="Enrollment failed")
