from pydantic import BaseModel


class BookModel(BaseModel):
    rate:int
    image:str
    title:str
    price:float
    category:str
    availability:str


    