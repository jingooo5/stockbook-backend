from decimal import Decimal
from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr


class Country(str, Enum):
    KR = "KR"
    US = "US"


class TradeType(Enum):
    BUY = 1
    SELL = 2
    DEPOSIT = 3
    WITHDRAW = 4


class TradingHistoryBase(BaseModel):
    stock_id: int
    date: datetime
    price: Optional[Decimal] = Field(decimal_places=4)
    number: int
    type: TradeType = None


class StockBase(BaseModel):
    name: str = Field(min_length=1, max_length=32)
    symbol: Optional[str] = Field(min_length=1, max_length=10)
    code: str = Field(min_length=1, max_length=10)
    market_id: int


class StockOut(StockBase):
    id: int
    interested: bool

    class Config:
        orm_mode = True


class StockIn(StockBase):
    interested : Optional[bool]


# class MarketBase(BaseModel):
#     name :
