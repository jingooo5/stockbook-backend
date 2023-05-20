from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from sqlalchemy.orm import Session
from .models import Stock
from .schemas import StockIn


async def get_by_id(db_session, stock_id: int):
    return db_session.query(Stock).filter(Stock.id == stock_id).first()

async def create(db_session, stock_data : StockIn):
    try:
        db_stock = Stock(**stock_data.dict())
    except ValidationError as e:
        print("error in create", e.json())
        raise e

    db_session.add(db_stock)
    db_session.commit()
    return stock_data