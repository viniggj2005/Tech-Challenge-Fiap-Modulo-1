from fastapi import APIRouter, Depends
from app.schemas.authentication import LoginModel,RefreshTokenModel
from app.services.jwt_authentication_service import (
    get_current_user,
    refresh_access_token,
    login_for_access_token,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def login(body: LoginModel):
    return await login_for_access_token(body)


@router.get("/user-info")
async def read_user_info(current_user: dict = Depends(get_current_user)):
    return current_user


@router.post("/refresh")
async def refresh_token(body: RefreshTokenModel):
    return await refresh_access_token(body.refresh_token)
