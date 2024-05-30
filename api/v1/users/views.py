from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.users.models import User, Token
from api.v1.users.schemas import SRegisterUser
from core.database import get_db

router = APIRouter(prefix='/api/v1/users')


async def create_user_token(db: AsyncSession, user: User):
    expiration = datetime.utcnow() + timedelta(days=356)
    token = Token(user=user, expires=expiration)
    db.add(token)
    await db.commit()
    await db.refresh(token)
    return token


@router.post("/register/")
async def register_user(user: SRegisterUser, db: AsyncSession = Depends(get_db)):
    registered_user = User(**user.dict())
    db.add(registered_user)
    await db.commit()
    await db.refresh(registered_user)
    token = await create_user_token(db, registered_user)
    return token




@router.post("/login/")
async def login_user():
    pass


@router.post("/logout/")
async def logout_user():
    pass


@router.get("/me/")
async def get_myself():
    pass
