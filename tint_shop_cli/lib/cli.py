#!/usr/bin/env python3

import sys, os
# ensure repo root is on sys.path so 'lib' package imports resolve when running this script directly
repo_root = os.path.dirname(os.path.dirname(__file__))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from lib.helpers import (
    create_tables,
    add_customer,
    list_customers,
    add_vehicle,
    list_vehicles,
    create_tint_job,
    list_tint_jobs,
    record_payment,
    list_payments,
    sales_report,
    outstanding_payments,
    exit_program
)

def main():
    create_tables()
    
    while True:
        menu()
        choice = input("\n> ")
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_customer_menu()
        elif choice == "2":
            list_customers()
        elif choice == "3":
            add_vehicle_menu()
        elif choice == "4":
            list_vehicles()
        elif choice == "5":
            create_tint_job_menu()
        elif choice == "6":
            list_tint_jobs()
        elif choice == "7":
            record_payment_menu()
        elif choice == "8":
            list_payments()
        elif choice == "9":
            sales_report()
        elif choice == "10":
            outstanding_payments()
        else:
            print("\n✗ Invalid choice. Please try again.")

def menu():
    print("\n" + "="*60)
    print("TINT INSTALLATION SHOP MANAGER")
    print("="*60)
    print("0. Exit the program")
    print("1. Add new customer")
    print("2. List all customers")
    print("3. Add new vehicle")
    print("4. List all vehicles")
    print("5. Create tint job")
    print("6. List all tint jobs")
    print("7. Record payment")
    print("8. List all payments")
    print("9. View sales report")
    print("10. View outstanding payments")
    print("="*60)

def add_customer_menu():
    print("\n--- Add New Customer ---")
    name = input("Customer name: ").strip()
    if not name:
        print("✗ Name is required!")
        return
    
    phone = input("Phone number (optional): ").strip() or None
    email = input("Email (optional): ").strip() or None
    
    add_customer(name, phone, email)

def add_vehicle_menu():
    print("\n--- Add New Vehicle ---")
    
    customers = list_customers()
    if not customers:
        print("\n✗ No customers found. Please add a customer first.")
        return
    
    try:
        customer_id = int(input("\nCustomer ID: ").strip())
        make = input("Vehicle make: ").strip()
        if not make:
            print("✗ Make is required!")
            return
        
        model = input("Vehicle model: ").strip()
        if not model:
            print("✗ Model is required!")
            return
        
        year_input = input("Year (optional): ").strip()
        year = int(year_input) if year_input else None
        
        license_plate = input("License plate (optional): ").strip() or None
        
        add_vehicle(customer_id, make, model, year, license_plate)
    except ValueError:
        print("✗ Invalid input. Please enter a valid number for Customer ID and Year.")

def create_tint_job_menu():
    print("\n--- Create Tint Job ---")
    
    vehicles = list_vehicles()
    if not vehicles:
        print("\n✗ No vehicles found. Please add a vehicle first.")
        return
    
    try:
        vehicle_id = int(input("\nVehicle ID: ").strip())
        
        print("\nTint Types:")
        print("1. Ceramic")
        print("2. Carbon")
        print("3. Dyed")
        tint_choice = input("Select tint type (1-3): ").strip()
        tint_types = {"1": "Ceramic", "2": "Carbon", "3": "Dyed"}
        tint_type = tint_types.get(tint_choice, "Ceramic")
        
        print("\nWindow Coverage:")
        print("1. Full (all windows)")
        print("2. Front Only")
        print("3. Rear Only")
        coverage_choice = input("Select coverage (1-3): ").strip()
        coverage_options = {"1": "Full", "2": "Front Only", "3": "Rear Only"}
        window_coverage = coverage_options.get(coverage_choice, "Full")
        
        cost = float(input("Total cost: $").strip())
        
        create_tint_job(vehicle_id, tint_type, window_coverage, cost)
    except ValueError:
        print("✗ Invalid input. Please enter valid numbers.")

def record_payment_menu():
    print("\n--- Record Payment ---")
    
    jobs = list_tint_jobs()
    if not jobs:
        print("\n✗ No tint jobs found. Please create a tint job first.")
        return
    
    try:
        job_id = int(input("\nTint Job ID: ").strip())
        amount = float(input("Payment amount: $").strip())
        
        print("\nPayment Method:")
        print("1. Cash")
        print("2. Credit Card")
        print("3. Check")
        method_choice = input("Select method (1-3): ").strip()
        methods = {"1": "Cash", "2": "Credit Card", "3": "Check"}
        payment_method = methods.get(method_choice, "Cash")
        
        record_payment(job_id, amount, payment_method)
    except ValueError:
        print("✗ Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    # allow running from project root: ensure repo root is on sys.path
    import sys, os
    repo_root = os.path.dirname(os.path.dirname(__file__))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
    main()

