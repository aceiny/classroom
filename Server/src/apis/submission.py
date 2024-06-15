from typing import List
from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.utils.auth import JWTBearer, decodeJWT
from src.apis.auth import router
from src.types.submission_types import CreateSubmissionDto
from src.utils.classroom import check_if_user_is_classroom_professor , check_if_user_enrolleed_in_classroom
router = APIRouter(
    prefix="/submission",
    tags=["submission"],
    responses={404: {"description": "Not found"}},
)

@router.get('/{classroomId}')
async def get_classroom_all_submissions(classroomId : str,submission : CreateSubmissionDto):
    userId = "clxgdek8c00007q5axo4hg1dc"
    await check_if_user_is_classroom_professor(classroomId, userId)
    submissions = await prisma.submission.find_many(
        where = {
            "classroomId" : classroomId
        }
    ) 
    return submissions

@router.post('/{classroomId}')
async def add_submission( classroomId : str , submission : CreateSubmissionDto):
    userId = "clxgdek8c00007q5axo4hg1"
    await check_if_user_enrolleed_in_classroom(classroomId, userId)
    created = await prisma.submission.create(
        {
            "content" : submission.content,
            "CoursworkId": submission.coursworkId,
            "files" : submission.files
        ,        }
    )