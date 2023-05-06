from decimal import Decimal
from typing import Dict, Type, Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import sessionmaker, registry
from typing_extensions import Annotated

str_30 = Annotated[str, 30]
str_50 = Annotated[str, 50]
num_12_4 = Annotated[Decimal, 12]
num_6_2 = Annotated[Decimal, 6]
num_8_4 = Annotated[Decimal, 8]

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    # only for sqlite
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base = declarative_base()

class Base(declarative_base):
    registry = registry(
        type_annotation_map={
            str_30: String(30),
            str_50: String(50),
            num_12_4: Numeric(12, 4),
            num_6_2: Numeric(6, 2),
            num_8_4: Numeric(8,4)
        }
    )
