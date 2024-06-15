import src.apis
from typing import List
from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.utils.auth import JWTBearer, decodeJWT
from src.apis.auth import router
from src.types.classroom_types import CreateClassRoomDto, UpdateClassRoomDto
from src.utils.classroom import check_if_user_is_classroom_professor , check_if_user_enrolleed_in_classroom
from src.types.courswork_types import CreateCoursworkDto
router = APIRouter(
    prefix="/courswork",
    tags=["courswork"],
    responses={404: {"description": "Not found"}},
)

@router.get('/{classroomId}')
async def get_classroom_all_coursworks(classroomId : str):
    userId = "clxgdek8c00007q5axo4hg1dc"
    await check_if_user_enrolleed_in_classroom(classroomId, userId)
    classroom = await prisma.classroom.find_unique(
        where = {
            "id" : classroomId
        }
    )
    if not classroom : 
        raise HTTPException(status_code=404, detail="Classroom not found")
    coursworks = await prisma.courswork.find_many(
        where = {
            "classroomId" : classroomId
        }
    )
    return coursworks

@router.post('/{classroomId}')
async def add_courswork( classroomId : str , coursework : CreateCoursworkDto):
    userId = "clxgdek8c00007q5axo4hg1dc"
    user = await prisma.user.find_unique(
        where=
                {
                "id": userId
                }
        )   
    if not user : 
        raise HTTPException(status_code=404, detail="User not found")
    await check_if_user_is_classroom_professor(classroomId, userId)
    created = await prisma.courswork.create(
        {
            "title" : coursework.title,
            "description": coursework.description,
            "classroomId": classroomId,
            "professorId" : userId,
            "due_date" : coursework.due_date,
            "type" : coursework.type.value,            
        }
    )
    if created : 
        return created
    raise HTTPException(status_code=404, detail="Coursework creation failed")