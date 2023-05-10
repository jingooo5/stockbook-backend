from sqlalchemy.orm import Session
from . import models, schemas


def get_stock(db: Session, stock_id: int):
    return db.query(models.Stocks).filter(models.Stocks.id == stock_id).first()
