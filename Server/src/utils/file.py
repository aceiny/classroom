import datetime
from fastapi import UploadFile, HTTPException
from pathlib import Path
from src.prisma import prisma
import shutil
import os

UPLOAD_DIRECTORY = Path("uploads/")
UPLOAD_DIRECTORY.mkdir(exist_ok=True)

async def add_file(file: UploadFile, userId: str, coursworkId: str = None, submissionId: str = None):
    userId = "clxgdek8c00007q5axo4hg1dc"
    try:
        file_path = os.path.join(UPLOAD_DIRECTORY, datetime.datetime.now().strftime("%Y%m%d%H%M%S") + file.filename)        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_obj = await prisma.file.create(
            {
                "name": file.filename,
                "path": file_path,
                "type": file.content_type,
                "size": str(file.size),
                "userId": userId,
                "submissionId": submissionId,  # Nullable field
                "coursworkId": coursworkId,    # Nullable field
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while saving the file: {str(e)}")
