from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLITE_URL = "sqlite:///tint_shop.db"

engine = create_engine(SQLITE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from .customer import Customer
from .vehicle import Vehicle
from .tint_job import TintJob
from .payment import Payment

