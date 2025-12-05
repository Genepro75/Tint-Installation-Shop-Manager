from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base

class TintJob(Base):
    __tablename__ = 'tint_jobs'
    
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    service_date = Column(DateTime, default=datetime.now)
    tint_type = Column(String, nullable=False)
    window_coverage = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    status = Column(String, default="Pending")
    
    vehicle = relationship("Vehicle", back_populates="tint_jobs")
    payments = relationship("Payment", back_populates="tint_job", cascade="all, delete-orphan")

