from fastapi import APIRouter, Depends , HTTPException , UploadFile
from src.prisma import prisma
from src.utils.auth import JWTBearer, decodeJWT
from src.apis.auth import router
router = APIRouter(
    prefix="/file",
    tags=["file"],
    responses={404: {"description": "Not found"}},
)

@router.get('/{fileId}')
async def get_file(fileId : str):
    file = await prisma.file.find_unique(
        where = {
            "id" : fileId
        }
    )
    if not file : 
        raise HTTPException(status_code=404, detail="File not found")
    return file

@router.get('/submission/{submissionId}')
async def add_file(submissionId : str):
    userId= "clxgdek8c00007q5axo4hg1dc"
    files = await prisma.file.find_many(
        where = {
            "submissionId" : submissionId,
            "userId" : userId
        }
    )
    return files

@router.get('/courswork/{coursworkId}')
async def get_courswork_files(coursworkId : str):
    userId = "clxgdek8c00007q5axo4hg1dc"
    courswork = await prisma.courswork.find_unique(
        where = {
            "id" : coursworkId
        }
    )