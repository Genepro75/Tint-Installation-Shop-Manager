#!/usr/bin/env python3
"""Demo script for the Tint Shop Manager CLI"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.models.customer import Customer
from app.models.vehicle import Vehicle
from app.models.tint_job import TintJob
from app.models.payment import Payment
from app.database.db import session, engine, Base
from datetime import datetime

def setup_demo_data():
    """Create demo data for testing"""
    # Create tables
    Base.metadata.create_all(engine)
    
    # Add sample customers
    customers_data = [
        ("John Doe", "555-1234", "john@example.com"),
        ("Jane Smith", "555-5678", "jane@example.com"),
        ("Bob Johnson", "555-9012", "bob@example.com")
    ]
    
    for name, phone, email in customers_data:
        customer = Customer(name=name, phone_number=phone, email=email)
        session.add(customer)
    
    session.commit()
    
    # Add sample vehicles
    vehicles_data = [
        (1, "Toyota", "Camry", 2020, "ABC123"),
        (1, "Honda", "Civic", 2019, "DEF456"),
        (2, "Ford", "F-150", 2021, "GHI789"),
        (3, "BMW", "X5", 2022, "JKL012")
    ]
    
    for customer_id, make, model, year, license in vehicles_data:
        vehicle = Vehicle(customer_id=customer_id, make=make, model=model, year=year, license_plate=license)
        session.add(vehicle)
    
    session.commit()
    
    # Add sample tint jobs
    jobs_data = [
        (1, "Full window tint package", 350.00),
        (2, "Front windows only", 150.00),
        (3, "Premium ceramic tint", 500.00),
        (4, "Basic tint package", 250.00)
    ]
    
    for vehicle_id, services, cost in jobs_data:
        job = TintJob(vehicle_id=vehicle_id, service_date=datetime.now(), services_offered=services, total_cost=cost)
        session.add(job)
    
    session.commit()
    
    # Add sample payments
    payments_data = [
        (1, 350.00),  # Full payment
        (2, 100.00),  # Partial payment
        (3, 250.00),  # Partial payment
        (4, 250.00)   # Full payment
    ]
    
    for job_id, amount in payments_data:
        payment = Payment(tint_job_id=job_id, payment_date=datetime.now(), amount_paid=amount)
        session.add(payment)
    
    session.commit()
    
    print("Demo data created successfully!")
    print("\\nYou can now test the CLI commands:")
    print("python test_app.py list-customers")
    print("python test_app.py list-vehicles") 
    print("python test_app.py list-jobs")
    print("python test_app.py sales-report")
    print("python test_app.py customer-loyalty")
    print("python test_app.py outstanding-payments")

if __name__ == '__main__':
    setup_demo_data()