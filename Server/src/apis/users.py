from typing import List
from fastapi import APIRouter, Depends , HTTPException
from src.prisma import prisma
from src.utils.auth import JWTBearer, decodeJWT

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["users"])
async def read_users():
    users = await prisma.user.find_many()
    for user in users:
        del user.password

    return users


@router.get("/me", tags=["users"])
async def read_user_me(token=Depends(JWTBearer())):
    decoded = decodeJWT(token)

    if "userId" in decoded:
        userId = decoded["userId"]
        return await prisma.user.find_unique(where={"id": userId})
    return None


@router.get("/{userId}", tags=["users"])
async def read_user(userId: str):
    user = await prisma.user.find_unique(where={"id": userId})
    if not user : 
        raise HTTPException(status_code=404, detail="User not found")
    return user
