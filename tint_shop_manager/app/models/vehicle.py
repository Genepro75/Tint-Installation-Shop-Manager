from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    license_plate = Column(String)
    customer = relationship('Customer', backref='vehicles')