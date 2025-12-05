import sys, os
# ensure tint_shop_cli directory is on sys.path so we can import lib package
pkg_root = os.path.dirname(os.path.dirname(__file__))
if pkg_root not in sys.path:
    sys.path.insert(0, pkg_root)

from lib.models import SessionLocal, Base, engine
from lib.models.customer import Customer
from lib.models.vehicle import Vehicle
from lib.models.tint_job import TintJob
from lib.models.payment import Payment
from datetime import datetime

def get_session():
    return SessionLocal()

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✓ Database tables created successfully!")

def add_customer(name, phone=None, email=None):
    session = get_session()
    try:
        customer = Customer(name=name, phone=phone, email=email)
        session.add(customer)
        session.commit()
        print(f"✓ Customer '{name}' added successfully! (ID: {customer.id})")
        return customer
    except Exception as e:
        session.rollback()
        print(f"✗ Error adding customer: {e}")
        return None
    finally:
        session.close()

def list_customers():
    session = get_session()
    try:
        customers = session.query(Customer).all()
        if not customers:
            print("\nNo customers found.")
            return []
        
        print("\n" + "="*70)
        print("CUSTOMERS")
        print("="*70)
        print(f"{'ID':<5} {'Name':<25} {'Phone':<15} {'Email':<25}")
        print("-"*70)
        for customer in customers:
            print(f"{customer.id:<5} {customer.name:<25} {str(customer.phone or ''):<15} {str(customer.email or ''):<25}")
        print("="*70)
        return customers
    finally:
        session.close()

def find_customer_by_id(customer_id):
    session = get_session()
    try:
        return session.query(Customer).filter(Customer.id == customer_id).first()
    finally:
        session.close()

def add_vehicle(customer_id, make, model, year=None, license_plate=None):
    session = get_session()
    try:
        customer = find_customer_by_id(customer_id)
        if not customer:
            print(f"✗ Customer with ID {customer_id} not found!")
            return None
        
        vehicle = Vehicle(
            customer_id=customer_id,
            make=make,
            model=model,
            year=year,
            license_plate=license_plate
        )
        session.add(vehicle)
        session.commit()
        year_str = f"{year} " if year else ""
        print(f"✓ Vehicle '{year_str}{make} {model}' added successfully! (ID: {vehicle.id})")
        return vehicle
    except Exception as e:
        session.rollback()
        print(f"✗ Error adding vehicle: {e}")
        return None
    finally:
        session.close()

def list_vehicles():
    session = get_session()
    try:
        vehicles = session.query(Vehicle).all()
        if not vehicles:
            print("\nNo vehicles found.")
            return []
        
        print("\n" + "="*90)
        print("VEHICLES")
        print("="*90)
        print(f"{'ID':<5} {'Customer':<20} {'Make':<15} {'Model':<15} {'Year':<6} {'License':<12}")
        print("-"*90)
        for vehicle in vehicles:
            customer_name = vehicle.customer.name if vehicle.customer else "N/A"
            print(f"{vehicle.id:<5} {customer_name:<20} {vehicle.make:<15} {vehicle.model:<15} {str(vehicle.year or ''):<6} {str(vehicle.license_plate or ''):<12}")
        print("="*90)
        return vehicles
    finally:
        session.close()

def find_vehicle_by_id(vehicle_id):
    session = get_session()
    try:
        return session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    finally:
        session.close()

def create_tint_job(vehicle_id, tint_type, window_coverage, cost, status="Pending"):
    session = get_session()
    try:
        vehicle = find_vehicle_by_id(vehicle_id)
        if not vehicle:
            print(f"✗ Vehicle with ID {vehicle_id} not found!")
            return None
        
        job = TintJob(
            vehicle_id=vehicle_id,
            tint_type=tint_type,
            window_coverage=window_coverage,
            cost=cost,
            status=status
        )
        session.add(job)
        session.commit()
        print(f"✓ Tint job created successfully! (ID: {job.id})")
        return job
    except Exception as e:
        session.rollback()
        print(f"✗ Error creating tint job: {e}")
        return None
    finally:
        session.close()

def list_tint_jobs():
    session = get_session()
    try:
        jobs = session.query(TintJob).all()
        if not jobs:
            print("\nNo tint jobs found.")
            return []
        
        print("\n" + "="*110)
        print("TINT JOBS")
        print("="*110)
        print(f"{'ID':<5} {'Customer':<15} {'Vehicle':<20} {'Tint Type':<12} {'Coverage':<15} {'Cost':<10} {'Status':<12}")
        print("-"*110)
        for job in jobs:
            customer_name = job.vehicle.customer.name if job.vehicle and job.vehicle.customer else "N/A"
            vehicle_info = f"{job.vehicle.make} {job.vehicle.model}" if job.vehicle else "N/A"
            print(f"{job.id:<5} {customer_name:<15} {vehicle_info:<20} {job.tint_type:<12} {job.window_coverage:<15} ${job.cost:<9.2f} {job.status:<12}")
        print("="*110)
        return jobs
    finally:
        session.close()

def find_tint_job_by_id(job_id):
    session = get_session()
    try:
        return session.query(TintJob).filter(TintJob.id == job_id).first()
    finally:
        session.close()

def record_payment(tint_job_id, amount, payment_method="Cash"):
    session = get_session()
    try:
        job = find_tint_job_by_id(tint_job_id)
        if not job:
            print(f"✗ Tint job with ID {tint_job_id} not found!")
            return None
        
        payment = Payment(
            tint_job_id=tint_job_id,
            amount=amount,
            payment_method=payment_method
        )
        session.add(payment)
        session.commit()
        print(f"✓ Payment of ${amount:.2f} recorded successfully! (ID: {payment.id})")
        return payment
    except Exception as e:
        session.rollback()
        print(f"✗ Error recording payment: {e}")
        return None
    finally:
        session.close()

def list_payments():
    session = get_session()
    try:
        payments = session.query(Payment).all()
        if not payments:
            print("\nNo payments found.")
            return []
        
        print("\n" + "="*90)
        print("PAYMENTS")
        print("="*90)
        print(f"{'ID':<5} {'Job ID':<8} {'Customer':<20} {'Amount':<12} {'Method':<15} {'Date':<20}")
        print("-"*90)
        for payment in payments:
            customer_name = payment.tint_job.vehicle.customer.name if payment.tint_job and payment.tint_job.vehicle and payment.tint_job.vehicle.customer else "N/A"
            date_str = payment.payment_date.strftime('%Y-%m-%d %H:%M') if payment.payment_date else "N/A"
            print(f"{payment.id:<5} {payment.tint_job_id:<8} {customer_name:<20} ${payment.amount:<11.2f} {payment.payment_method:<15} {date_str:<20}")
        print("="*90)
        return payments
    finally:
        session.close()

def sales_report():
    session = get_session()
    try:
        jobs = session.query(TintJob).all()
        payments = session.query(Payment).all()
        
        total_revenue = sum(p.amount for p in payments)
        total_jobs_cost = sum(j.cost for j in jobs)
        total_paid = sum(p.amount for p in payments)
        outstanding_balance = total_jobs_cost - total_paid
        
        print("\n" + "="*60)
        print("SALES REPORT")
        print("="*60)
        print(f"Total Jobs: {len(jobs)}")
        print(f"Total Job Value: ${total_jobs_cost:.2f}")
        print(f"Total Payments Received: ${total_paid:.2f}")
        print(f"Outstanding Balance: ${outstanding_balance:.2f}")
        print("="*60)
        
        return {
            'total_jobs': len(jobs),
            'total_value': total_jobs_cost,
            'total_paid': total_paid,
            'outstanding': outstanding_balance
        }
    finally:
        session.close()

def outstanding_payments():
    session = get_session()
    try:
        jobs = session.query(TintJob).all()
        outstanding = []
        
        for job in jobs:
            total_paid = sum(p.amount for p in job.payments)
            balance = job.cost - total_paid
            if balance > 0:
                outstanding.append({
                    'job': job,
                    'balance': balance,
                    'paid': total_paid
                })
        
        if not outstanding:
            print("\n✓ No outstanding payments!")
            return []
        
        print("\n" + "="*90)
        print("OUTSTANDING PAYMENTS")
        print("="*90)
        print(f"{'Job ID':<8} {'Customer':<20} {'Vehicle':<20} {'Total Cost':<12} {'Paid':<12} {'Balance':<12}")
        print("-"*90)
        for item in outstanding:
            job = item['job']
            customer_name = job.vehicle.customer.name if job.vehicle and job.vehicle.customer else "N/A"
            vehicle_info = f"{job.vehicle.make} {job.vehicle.model}" if job.vehicle else "N/A"
            print(f"{job.id:<8} {customer_name:<20} {vehicle_info:<20} ${job.cost:<11.2f} ${item['paid']:<11.2f} ${item['balance']:<11.2f}")
        print("="*90)
        return outstanding
    finally:
        session.close()

def exit_program():
    print("\nThank you for using Tint Installation Shop Manager!")
    print("Goodbye!")
    exit()

