import pandas as pd
from fastapi import HTTPException,status
from app.services.data_service import get_csv_data

def get_books():
    data=get_csv_data()
    data=data[["id","title"]]
    if data.empty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Nenhum livro foi encontrado!")
    return data.to_dict(orient="records")

def get_book_by_id(id:int):
    data=get_csv_data()
    data=data[data["id"]==id]
    if data.empty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Nenhum livro foi encontrado!")
    return data.to_dict(orient="records")

def get_books_by_search(title: str | None = None, category: str | None = None):
    data=get_csv_data()
    print(title,category)
    #mascára booleana do pandas.
    mask = pd.Series(True, index=data.index)

    if title:
        mask &= data["title"].astype(str).str.contains(title, case=False, na=False)
    if category:
        mask &= data["category"].astype(str).str.contains(category, case=False, na=False)
    result=data[mask]
    if result.empty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Nenhum livro foi encontrado!")
    return result.to_dict(orient="records")

    