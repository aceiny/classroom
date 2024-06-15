from fastapi import HTTPException
from src.prisma import prisma

async def check_if_user_is_classroom_professor(classroomId: str, userId: str):
    classroom = await prisma.classroom.find_unique(
        where={
            "id": classroomId
        }
    )
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    if classroom.professorId != userId:
        raise HTTPException(status_code=404, detail="User is not the professor of this classroom")
    return classroom

async def check_if_user_enrolleed_in_classroom(classroomId : str , userId : str) :
    enrollment = await prisma.enrollment.find_first(
        where=
                {
                "classroomId": classroomId,
                "membreId": userId
                }
    )
    if not enrollment :
        raise HTTPException(status_code=404, detail="User not entolled in this classroom")
    return enrollment