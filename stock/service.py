from sqlalchemy.orm import Session
from .models import Stock

def get(db_session, stock_id: int):
    return db_session.query(Stock).filter(Stock.id == stock_id).first()
