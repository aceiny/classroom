from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.apis.auth import router
from src.utils.user import get_current_user
router = APIRouter(
    prefix="/file",
    tags=["file"],
    responses={404: {"description": "Not found"}},
)

@router.get('/{fileId}')
async def get_file_by_id(fileId : str , userId=Depends(get_current_user) ):
    file = await prisma.file.find_unique(
        where = {
            "id" : fileId
        }
    )
    if not file : 
        raise HTTPException(status_code=404, detail="File not found")
    return file

@router.get('/submission/{submissionId}')
async def get_submission_file(submissionId : str , userId=Depends(get_current_user)) :
    userId= "clxgdek8c00007q5axo4hg1dc"
    files = await prisma.file.find_many(
        where = {
            "submissionId" : submissionId,
        }
    )
    return files

@router.get('/courswork/{coursworkId}')
async def get_courswork_files(coursworkId : str , userId=Depends(get_current_user)):
    files = await prisma.file.find_many(
        where = {
            "coursworkId" : coursworkId,
        }
    )
    return files