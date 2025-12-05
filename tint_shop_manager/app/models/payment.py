from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from app.database.db import Base

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    tint_job_id = Column(Integer, ForeignKey('tint_jobs.id'))
    payment_date = Column(DateTime)
    amount_paid = Column(Float)
    tint_job = relationship('TintJob', backref='payments')