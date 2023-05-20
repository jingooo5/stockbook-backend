from decimal import Decimal
from typing import Dict, Type, Any

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import sessionmaker, registry
from starlette.requests import Request
from typing_extensions import Annotated

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE

str_30 = Annotated[str, 30]
str_50 = Annotated[str, 50]
num_12_4 = Annotated[Decimal, 12]
num_6_2 = Annotated[Decimal, 6]
num_8_4 = Annotated[Decimal, 8]

# SQLALCHEMY_DATABASE_URL = "sqlite:///db"
SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset=utf8'
print("url" , SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    # only for sqlite
    SQLALCHEMY_DATABASE_URL
)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            str_30: String(30),
            str_50: String(50),
            num_12_4: Numeric(12, 4),
            num_6_2: Numeric(6, 2),
            num_8_4: Numeric(8, 4)
        }
    )

# Base = declarative_base()


def get_db(request: Request):
    # print("request from connection")
    return request.state.db


DbSession = Annotated[Session, Depends(get_db)]