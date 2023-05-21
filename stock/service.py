from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy.sql import select, insert
from .models import Stock
from .schemas import StockIn, StockOut


async def get_by_id(db_session, stock_id: int) -> StockOut:
    query = select(Stock).where(Stock.id == stock_id)
    result = await db_session.execute(query)
    return result.scalar()
    # return db_session.query(Stock).filter(Stock.id == stock_id).first()

async def create(db_session, stock_data : StockIn) -> Stock:
    stock_dict = stock_data.dict()

    query = insert(Stock).values(**stock_dict)
    result = await db_session.execute(query)
    await db_session.commit()

    stock_dict['id'] = result.inserted_primary_key[0]
    return Stock(**stock_dict)
    # db_stock = Stock(**stock_data.dict())
    # db_session.add(db_stock)
    # db_session.commit()
    # return db_stock