from __future__ import annotations

from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from database import Base, num_12_4, num_8_4


# class IdBase(Base):
#     id : Mapped[int] = mapped_column(primary_key=True, index=True)
#
#
# class TimeBase(Base):
#     create_time: Mapped[datetime] = mapped_column(default=datetime.now())
#     update_time: Mapped[datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())
#     delete_time: Mapped[datetime] = mapped_column(nullable=True)


class Quote(Base):
    __tablename__ = 'quote'

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    symbol: Mapped[str]
    update_time: Mapped[datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())
    kr_rate : Mapped[float]


class Market(Base):
    __tablename__ = 'market'

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    name : Mapped[str]
    country : Mapped[str]
    quote_id : Mapped[int] = mapped_column(ForeignKey('quote.id'))

    # stocks : Mapped[List["Stock"]] = relationship(back_populates='stock')

class Stock(Base):
    __tablename__ = 'stock'

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    name : Mapped[str]
    symbol: Mapped[str]
    code : Mapped[str] = mapped_column(unique=True, index=True)
    market_id : Mapped[int] = mapped_column(ForeignKey('market.id'))
    interested : Mapped[bool]

    trading_histories: Mapped[List["TradingHistory"]] = relationship()
    # market : Mapped["Market"] = relationship(back_populates='market')


# class StockDetail(Base):
#     __tablename__ = 'stock_detail'
#
#     id : Mapped[]

class Account(Base):
    __tablename__ = 'account'

    id : Mapped[int] = mapped_column( primary_key=True, index=True)
    nickname: Mapped[str]
    balance: Mapped[float]
    quote_id : Mapped[int] = mapped_column(ForeignKey('quote.id'))


class TradingHistory(Base):
    __tablename__ = 'trading_history'

    id : Mapped[int] = mapped_column( primary_key=True, index=True)
    stock_id: Mapped[int] = mapped_column(ForeignKey("stock.id"))
    create_time: Mapped[datetime] = mapped_column(default=datetime.now())
    update_time: Mapped[datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())
    date : Mapped[datetime]
    price: Mapped[num_8_4]
    number: Mapped[int]
    quote_id : Mapped[int] = mapped_column(ForeignKey('quote.id'))
    type : Mapped[int]
    account_id: Mapped[int] = mapped_column(ForeignKey('account.id'))

    # stock : Mapped["Stock"] = relationship(back_populates='stock')