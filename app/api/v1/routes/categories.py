from fastapi import APIRouter, Depends
from app.services.categories_service import get_all_categories
from app.services.jwt_authentication_service import get_current_user

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/",dependencies=[Depends(get_current_user)])
def list_categories():
    return get_all_categories()
