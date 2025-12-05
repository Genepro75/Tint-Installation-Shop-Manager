from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from app.database.db import Base

class TintJob(Base):
    __tablename__ = 'tint_jobs'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    service_date = Column(DateTime)
    services_offered = Column(String)
    total_cost = Column(Float)
    vehicle = relationship('Vehicle', backref='tint_jobs')