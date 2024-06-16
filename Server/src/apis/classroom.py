from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.apis.auth import router
from src.types.classroom_types import CreateClassRoomDto, UpdateClassRoomDto
from src.utils.classroom import check_if_user_is_classroom_professor
from src.utils.user import get_current_user
router = APIRouter(
    prefix="/classroom",
    tags=["classroom"],
    responses={404: {"description": "Not found"}},
)

@router.get('/', tags=["classroom"])
async def read_classrooms():
    classrooms = await prisma.classroom.find_many()
    return classrooms


@router.post('/')
async def create_classroom(classroom : CreateClassRoomDto , userId=Depends(get_current_user)):
    user = await prisma.user.find_unique(where={"id": userId})
    if not user : 
        raise HTTPException(status_code=404, detail="User not found")
    if user.role != "Professor" :
        raise HTTPException(status_code=404, detail="User is not a professor")
    try : 
        classroom = await prisma.classroom.create({
            "name": classroom.name,
            "professorId": userId
        })
        await prisma.enrollment.create({
            "membreId": userId,
            "classroomId": classroom.id
        })
        if classroom : 
            return classroom
    except : 
        raise HTTPException(status_code=404, detail="Error while creating classroom")
    
@router.put('/{classroomId}', tags=["classroom"])
async def update_classroom(classroomId : str, classroom : UpdateClassRoomDto , userId=Depends(get_current_user)):
    user = await prisma.user.find_unique(
        where={
        "id": userId
        })
    if not user : 
        raise HTTPException(status_code=404, detail="User not found")
    if user.role != "Professor" :
        raise HTTPException(status_code=404, detail="User is not a professor")

    await check_if_user_is_classroom_professor(classroomId, userId)

    updated_classroom = await prisma.classroom.update(
        where={
            "id": classroomId
        },
        data={
            "name": classroom.name,  
        }
    )
    return updated_classroom

@router.delete('/{classroomId}', tags=["classroom"])
async def delete_classroom(classroomId : str):
    userId = "clxgdek8c00007q5axo4hg1dc"
    user = await prisma.user.find_unique(
        where={
        "id": userId
        })
    if not user : 
        raise HTTPException(status_code=404, detail="User not found")
    if user.role != "Professor" :
        raise HTTPException(status_code=404, detail="User is not a professor")
    try : 
        await check_if_user_is_classroom_professor(classroomId, userId)
        
        await prisma.enrollment.delete_many(
        where={
            "classroomId": classroomId
        })
        courseworks = await prisma.courswork.find_many(
            where={
                "classroomId": classroomId
            }
        )

        for coursework in courseworks : 
            await prisma.submission.delete_many(
                where={
                    "courseworkId": coursework.id
                }
            )
            await prisma.courswork.delete(
            where={
                "id": coursework.id
            }
        )
            
        classroom = await prisma.classroom.delete(
            where={
                "id": classroomId
            }  
        )
        return classroom
    except :
        raise HTTPException(status_code=404, detail="Error while deleting classroom")