from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import DbSession
from stock.models import Stock
from stock.schemas import StockOut, StockIn
from stock.service import get_by_id, create

router = APIRouter()


# async def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@router.get(
    "/{stock_id}",
    response_model=StockOut,
)
async def get_stock(stock_id: int, db: DbSession) -> StockOut:
    db_stock = await get_by_id(db, stock_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock

@router.post(
    "",
    response_model=StockOut
)
async def create_stock(stock_in : StockIn, db: DbSession):
    return await create(db, stock_in)

# @router.put(
#     "/{stock_id}",
#     response_model=StockOut
# )
# async def update_stock(stock_in)