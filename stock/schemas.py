from enum import Enum
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Country(str, Enum):
   KR = "KR"
   US = "US"

class TradeType(Enum):
    BUY = 1
    SELL = 2
    DEPOSIT = 3
    WITHDRAW = 4

class StockBase(BaseModel):
    name : str = Field(min_length=1, max_length=32)
    symbol : str = Field(min_length=1, max_length=10)
    code : str = Field(min_length=1, max_length=10)
    market_id: int
    kr_rate : float


class MarketBase(BaseModel):
    name :