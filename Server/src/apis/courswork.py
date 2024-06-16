from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.apis.auth import router
from src.utils.classroom import check_if_user_is_classroom_professor , check_if_user_enrolleed_in_classroom
from src.types.courswork_types import CreateCoursworkDto
from src.utils.user import get_current_user
router = APIRouter(
    prefix="/courswork",
    tags=["courswork"],
    responses={404: {"description": "Not found"}},
)

@router.get('/{classroomId}')
async def get_classroom_all_coursworks(classroomId : str , userId=Depends(get_current_user)):
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
        } , 
    )
    return coursworks

@router.get('/{coursworkId}')
async def get_courswork_by_id(coursworkId : str , userId=Depends(get_current_user)):
    courswork = await prisma.courswork.find_unique(
        where = {
            "id": coursworkId
        }
    )
    if not courswork :
        raise HTTPException(status_code=404, detail="Courswork not found")
    await check_if_user_enrolleed_in_classroom(courswork.classroomId, userId)
    files = await prisma.file.find_many(
        where = {
            "coursworkId" : coursworkId
        }
    )
    if files :
        courswork.files = files
    return courswork


@router.post('/{classroomId}')
async def add_courswork( classroomId : str , coursework : CreateCoursworkDto ,  userId=Depends(get_current_user) ):
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