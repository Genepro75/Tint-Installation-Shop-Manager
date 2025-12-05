from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Vehicle(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    license_plate = Column(String)
    
    customer = relationship("Customer", back_populates="vehicles")
    tint_jobs = relationship("TintJob", back_populates="vehicle", cascade="all, delete-orphan")

