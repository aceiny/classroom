from typing import List , Annotated
from fastapi import APIRouter, Depends , HTTPException, UploadFile , Form 
from src.prisma import prisma
from src.apis.auth import router
from src.utils.classroom import check_if_user_is_classroom_professor , check_if_user_enrolleed_in_classroom
from src.utils.file import add_file
from src.utils.user import get_current_user
router = APIRouter(
    prefix="/submission",
    tags=["submission"],
    responses={404: {"description": "Not found"}},
)

@router.get('/{classroomId}')
async def get_classroom_all_submissions(classroomId : str ,  userId=Depends(get_current_user)):
    await check_if_user_is_classroom_professor(classroomId, userId)
    submissions = await prisma.submission.find_many(
        where = {
            "classroomId" : classroomId
        }
    ) 
    return submissions

@router.get('/{submissionId}')
async def get_submission_by_id(submissionId : str ,  userId=Depends(get_current_user)):
    submission = await prisma.submission.find_unique(
        where = {
            "id": submissionId
        }
    )
    if not submission :
        raise HTTPException(status_code=404, detail="Submission not found")
    files = await prisma.file.find_many(
        where = {
            "submissionId" : submissionId
        }
    )
    if files :
        submission.files = files
    return submission

@router.post('/{coursworkId}')
async def add_submission( coursworkId : str , content : Annotated[str , Form()] , files : List[UploadFile] ,  userId=Depends(get_current_user)):
    courswork = await prisma.courswork.find_unique(
        where = {
            "id" : coursworkId
        }
    )
    if not courswork : 
        raise HTTPException(status_code=404, detail="Courswork not found")
    await check_if_user_enrolleed_in_classroom(courswork.classroomId, userId)
    submissionObj = await prisma.submission.create(
        {
            "content" : content,
            "CoursworkId": coursworkId,
            "studentId" : userId
        }
    )
    if not submissionObj : 
        raise HTTPException(status_code=404, detail="Submission failed")
    for file in files:
         await add_file(file , userId ,submissionId = submissionObj.id )
    return submissionObj