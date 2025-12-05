from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base

class Payment(Base):
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True)
    tint_job_id = Column(Integer, ForeignKey('tint_jobs.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.now)
    payment_method = Column(String, default="Cash")
    
    tint_job = relationship("TintJob", back_populates="payments")

