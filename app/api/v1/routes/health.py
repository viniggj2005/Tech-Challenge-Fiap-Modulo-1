from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.services.db_service import get_db

router = APIRouter(prefix="/health", tags=["Health"])




@router.get("/")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"message": "Conexão com os dados OK, Api saudável", "db_status": "Connected"}
    except Exception as e:
        return {"message": "Erro na conexão com o banco de dados", "db_status": str(e)}

