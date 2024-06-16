import datetime
from fastapi import UploadFile, HTTPException
from pathlib import Path
from src.prisma import prisma
import shutil

UPLOAD_DIRECTORY = Path("uploads/")
UPLOAD_DIRECTORY.mkdir(exist_ok=True)

async def add_file(file : UploadFile , userId : str , coursworkId : str | None = None , submissionId : str | None = None):
    print(file , userId , coursworkId , submissionId)
    userId = "clxgdek8c00007q5axo4hg1dc"
    try : 
        file_path = UPLOAD_DIRECTORY / datetime.datetime.now().strftime("%Y%m%d%H%M%S") + file.filename
        with file_path.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        file_Obj = await prisma.file.create(
                {
                    "name" : file.filename,
                    "path" : file_path,
                    "type" : file.content_type,
                    "size" : file.size,
                    "userId" : userId,
                    "submissionId": submissionId,  # Nullable field
                    "coursworkId": coursworkId,    # Nullable field
                }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while saving the file: {str(e)}")
