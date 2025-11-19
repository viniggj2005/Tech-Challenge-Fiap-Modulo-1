import pandas as pd
from fastapi import HTTPException,status
from app.services.data_service import get_csv_data

def get_all_categories():
    data=get_csv_data()
    result= data["category"].unique()
    if len(result)==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Nenhuma ctegoria foi encontrada!")
    return {"categories":result.tolist()}
