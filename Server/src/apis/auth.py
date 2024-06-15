from enum import Enum
from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.types.user_types import Gender
from src.prisma import prisma
from src.utils.auth import (
    encryptPassword,
    signJWT,
    validatePassword,
)
from src.types.user_types import SignInOut, UserLoginDto, UserRegisterDto

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/sign-in", tags=["auth/signin"])
async def sign_in(signIn: UserLoginDto):
    user = await prisma.user.find_first(
            where={
                "email": signIn.email,
            }
        )
    if user is None:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    validated = validatePassword(signIn.password, user.password)
    del user.password

    if not validated:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    token = signJWT(user.id)
    return SignInOut(token=token, id=user.id)
    




@router.post("/sign-up", tags=["auth/signup"])
async def sign_up(user: UserRegisterDto):
    user_exists = await prisma.user.find_first(
        where={
            "email": user.email,
        }
    )
    if user_exists:
        raise HTTPException(status_code=400, detail="User already exists")
    password = encryptPassword(user.password)
    created = await prisma.user.create(
        {
            "name" : user.name,
            "email": user.email,  
            "gender": user.gender.value,
            "role": user.role.value,
            "password": encryptPassword(user.password),
        }
    )
    if created : 
        token = signJWT(created.id)
        return SignInOut(token=token, id=created.id)
        


@router.get("/", tags=["auth"])
async def auth():
    users = await prisma.user.find_many()

    for user in users:
        del user.password

    return users
