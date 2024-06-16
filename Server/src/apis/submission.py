import src.apis
from typing import List
from fastapi import APIRouter, Depends , HTTPException, UploadFile
from src.prisma import prisma
from src.utils.auth import JWTBearer, decodeJWT
from src.apis.auth import router
from src.types.submission_types import CreateSubmissionDto
from src.utils.classroom import check_if_user_is_classroom_professor , check_if_user_enrolleed_in_classroom
from src.utils.file import add_file
router = APIRouter(
    prefix="/submission",
    tags=["submission"],
    responses={404: {"description": "Not found"}},
)

@router.get('/{classroomId}')
async def get_classroom_all_submissions(classroomId : str):
    userId = "clxgdek8c00007q5axo4hg1dc"
    await check_if_user_is_classroom_professor(classroomId, userId)
    submissions = await prisma.submission.find_many(
        where = {
            "classroomId" : classroomId
        }
    ) 
    return submissions

@router.post('/{coursworkId}')
async def add_submission( coursworkId : str , submission : CreateSubmissionDto , files : List[UploadFile]):
    userId = "clxgdek8c00007q5axo4hg1"
    classroomId = await prisma.courswork.find_unique(
        where = {
            "id" : coursworkId
        }
    ).classroomId
    await check_if_user_enrolleed_in_classroom(classroomId, userId)
    submissionObj = await prisma.submission.create(
        {
            "content" : submission.content,
            "CoursworkId": submission.coursworkId,
            "files" : submission.files
        }
    )
    for file in files:
        await add_file(file , userId ,submissionId = submissionObj.id ) 
    return submissionObj