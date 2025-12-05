#!/usr/bin/env python3

from helpers import (
    create_tables,
    add_customer,
    add_vehicle,
    create_tint_job,
    record_payment
)

def debug():
    print("Creating database tables...")
    create_tables()
    
    print("\nAdding sample customers...")
    customer1 = add_customer("John Smith", "555-1234", "john@example.com")
    customer2 = add_customer("Jane Doe", "555-5678", "jane@example.com")
    customer3 = add_customer("Bob Johnson", "555-9012", "bob@example.com")
    
    print("\nAdding sample vehicles...")
    vehicle1 = add_vehicle(1, "Toyota", "Camry", 2020, "ABC123")
    vehicle2 = add_vehicle(1, "Honda", "Civic", 2019, "DEF456")
    vehicle3 = add_vehicle(2, "Ford", "F-150", 2021, "GHI789")
    vehicle4 = add_vehicle(3, "BMW", "X5", 2022, "JKL012")
    
    print("\nCreating sample tint jobs...")
    job1 = create_tint_job(1, "Ceramic", "Full", 450.00, "Completed")
    job2 = create_tint_job(2, "Carbon", "Front Only", 200.00, "Completed")
    job3 = create_tint_job(3, "Ceramic", "Full", 500.00, "In Progress")
    job4 = create_tint_job(4, "Dyed", "Full", 300.00, "Pending")
    
    print("\nRecording sample payments...")
    record_payment(1, 450.00, "Credit Card")
    record_payment(2, 100.00, "Cash")
    record_payment(3, 250.00, "Credit Card")
    
    print("\n" + "="*60)
    print("Sample data created successfully!")
    print("="*60)
    print("\nYou can now run the CLI with: python lib/cli.py")

if __name__ == "__main__":
    debug()

