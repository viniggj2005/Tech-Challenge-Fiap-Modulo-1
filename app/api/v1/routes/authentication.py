from fastapi import APIRouter,Depends
from app.schemas.authentication import LoginModel
from app.services.jwt_authentication_service import login_for_access_token,get_current_user
router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(body:LoginModel):
   return login_for_access_token(body.username,body.password)


@router.get("/user-info")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
