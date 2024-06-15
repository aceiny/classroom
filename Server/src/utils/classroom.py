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