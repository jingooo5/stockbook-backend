from sqlalchemy.orm import Session
from .models import Stock

def get_stock(db_session, stock_id: int):
    return db_session.query(Stock).filter(Stock.id == stock_id).first()

# def create_stock(db_session, stock : StockIn)