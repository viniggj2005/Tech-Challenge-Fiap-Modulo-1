from fastapi import APIRouter, Depends
from app.services.data_service import check_data_connection

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health_check():
    data_connection=check_data_connection()
    return {"message":"Conexão com os dados OK, Api saudável"}
