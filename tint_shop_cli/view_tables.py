#!/usr/bin/env python3
"""Simple script to view all database tables"""

import sys, os
# when run as a script, make sure the repo root is available so 'lib' package imports work
repo_root = os.path.dirname(os.path.dirname(__file__))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from lib.models import SessionLocal
from lib.models.customer import Customer
from lib.models.vehicle import Vehicle
from lib.models.tint_job import TintJob
from lib.models.payment import Payment

def view_all_tables():
    session = SessionLocal()
    
    print("="*60)
    print("DATABASE TABLES VIEWER")
    print("="*60)
    
    # Customers
    customers = session.query(Customer).all()
    print(f"\nCUSTOMERS ({len(customers)} records):")
    print("-" * 40)
    for c in customers:
        print(f"ID: {c.id} | Name: {c.name} | Phone: {c.phone} | Email: {c.email}")
    
    # Vehicles
    vehicles = session.query(Vehicle).all()
    print(f"\nVEHICLES ({len(vehicles)} records):")
    print("-" * 40)
    for v in vehicles:
        owner = v.customer.name if v.customer else "Unknown"
        print(f"ID: {v.id} | Owner: {owner} | {v.year} {v.make} {v.model} | License: {v.license_plate}")
    
    # Tint Jobs
    jobs = session.query(TintJob).all()
    print(f"\nTINT JOBS ({len(jobs)} records):")
    print("-" * 40)
    for j in jobs:
        vehicle_info = f"{j.vehicle.make} {j.vehicle.model}" if j.vehicle else "Unknown"
        # model fields: tint_type and cost
        print(f"ID: {j.id} | Vehicle: {vehicle_info} | Service: {j.tint_type} | Cost: ${j.cost}")
    
    # Payments
    payments = session.query(Payment).all()
    print(f"\nPAYMENTS ({len(payments)} records):")
    print("-" * 40)
    for p in payments:
        # model field is 'amount' and 'payment_method'
        print(f"ID: {p.id} | Job ID: {p.tint_job_id} | Amount: ${p.amount} | Method: {p.payment_method} | Date: {p.payment_date}")
    
    session.close()
    print("\n" + "="*60)

if __name__ == "__main__":
    view_all_tables()