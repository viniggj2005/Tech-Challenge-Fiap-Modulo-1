import pandas as pd
from fastapi import HTTPException, status
from app.services.db_service import SessionLocal
from app.services.data_service import get_csv_data,get_db_data
def get_books():
    # data = get_csv_data()
    data = get_db_data()
    data = data[["id", "title"]]
    if data.empty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum livro foi encontrado!"
        )
    return data.to_dict(orient="records")


def get_book_by_id(id: int):
    # data = get_csv_data()
    data = get_db_data()
    data = data[data["id"] == id]
    if data.empty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum livro foi encontrado!"
        )
    return data.to_dict(orient="records")


from app.models.book import Book

def get_books_by_search(title: str | None = None, category: str | None = None):
    db = SessionLocal()
    try:
        query = db.query(Book)

        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))
        if category:
            query = query.filter(Book.category.ilike(f"%{category}%"))

        result = pd.read_sql(query.statement, db.bind)

        if result.empty:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum livro foi encontrado!"
            )
        
        return result.to_dict(orient="records")
    finally:
        db.close()


def get_top_rated_books(amount:int):
    # data=get_csv_data()
    data=get_db_data()
    data=data.sort_values(by=["rate"],ascending=False)
    result = data.head(amount).to_dict(orient="records")
    return {"top_rated_books":result}

def get_books_by_price_range(min_price:float,max_price:float):
    # data=get_csv_data()
    data=get_db_data()
    data["price"] = data["price"].astype(float)
    books = data[(data["price"] >= min_price) & (data["price"] <= max_price)]
    return books.sort_values(by="price",ascending=True).to_dict(orient="records")