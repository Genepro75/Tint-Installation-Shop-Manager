from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String)
    
    vehicles = relationship("Vehicle", back_populates="customer", cascade="all, delete-orphan")

