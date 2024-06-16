from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.apis.auth import router
from src.utils.user import get_current_user

router = APIRouter(
    prefix="/enrollment",
    tags=["enrollment"],
    responses={404: {"description": "Not found"}},
)


@router.get('/me', tags=["enrollment"])
async def get_enrollments(userId=Depends(get_current_user)):
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
async def add_enrollment(classroomId : str , userId=Depends(get_current_user)):
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

@router.delete('/{classroomId}', tags=["enrollment"])
async def delete_enrollment(classroomId : str , userId=Depends(get_current_user))  :
    enrollment = await prisma.enrollment.find_first(
        where={
            "membreId": userId,
            "classroomId": classroomId
        }
    )
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    await prisma.enrollment.delete(
        where={
            "id": enrollment.id
        }
    )
    return enrollment