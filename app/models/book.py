from sqlalchemy import Column, Integer, String, Float
from app.services.db_service import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    rate = Column(Integer)
    image = Column(String)
    title = Column(String)
    price = Column(Float)
    category = Column(String)
    availability = Column(String)
