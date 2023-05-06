from __future__ import annotations

import datetime
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from database import Base

class Quote(Base):
    __tablename__ = 'quote'

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    symbol: Mapped[str]
    update_time: Mapped[datetime.datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())
    kr_rate : Mapped[float]


class Markets(Base):
    __tablename__ = 'markets'

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    name : Mapped[str]
    country : Mapped[str]
    quote_id : Mapped[int] = mapped_column(ForeignKey('quote.id'))


class Stocks(Base):
    __tablename__ = 'stocks'

    id : Mapped[int] = mapped_column( primary_key=True, index=True)
    name : Mapped[str]
    symbol: Mapped[str]
    code : Mapped[str] = mapped_column(unique=True, index=True)
    market_id : Mapped[int] = mapped_column(ForeignKey('markets.id'))
    trading_history: Mapped[List["TradingHistory"]] = relationship()

class TradingHistory(Base):
    __tablename__ = 'trading_history'

    id : Mapped[int] = mapped_column( primary_key=True, index=True)
    stock_id: Mapped[int] = mapped_column(ForeignKey("stocks.id"))
    create_time: Mapped[datetime.datetime] = mapped_column(default=datetime.now())
    update_time: Mapped[datetime.datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())
    price: Mapped[str]
    quote: Mapped[str]