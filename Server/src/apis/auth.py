import datetime
from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.models.scalar import Gender
from src.prisma import prisma
from src.utils.auth import (
    encryptPassword,
    signJWT,
    validatePassword,
)
from src.types.user_types import SignInOut, UserLoginDto, UserRegisterDto

router = APIRouter()


@router.post("/auth/sign-in", tags=["auth"])
async def sign_in(signIn: UserLoginDto):
    try : 
            user = await prisma.user.find_first(
                where={
                    "username": signIn.username,
                }
            )
    except Exception as e : 
        raise HTTPException(status_code=404, detail="User not found")
    validated = validatePassword(signIn.password, user.password)
    del user.password

    if validated:
        token = signJWT(user.id)
        return SignInOut(token=token, id=user.id)

    return None




@router.post("/auth/sign-up", tags=["auth"])
async def sign_up(user: UserRegisterDto):
    password = encryptPassword(user.password)
    created = await prisma.user.create(
        {
            "username": user.username,
            "password": encryptPassword(user.password),
            "name": user.name,
            "gender": user.gender,
        }
    )

    return created


@router.get("/auth/", tags=["auth"])
async def auth():
    users = await prisma.user.find_many()

    for user in users:
        del user.password

    return users
