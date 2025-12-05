import click
from datetime import datetime
from app.models.customer import Customer
from app.models.vehicle import Vehicle
from app.models.tint_job import TintJob
from app.models.payment import Payment
from app.database.db import session, engine, Base

@click.group()
def cli():
    """Tint Installation Shop Manager CLI"""
    Base.metadata.create_all(engine)

@cli.command()
@click.option('--name', prompt='Customer name', help='Customer full name')
@click.option('--phone', prompt='Phone number', help='Customer phone number')
@click.option('--email', prompt='Email address', help='Customer email')
def add_customer(name, phone, email):
    """Add a new customer"""
    customer = Customer(name=name, phone_number=phone, email=email)
    session.add(customer)
    session.commit()
    click.echo(f"Customer {name} added successfully!")

@cli.command()
@click.option('--customer-id', prompt='Customer ID', type=int, help='Customer ID')
@click.option('--make', prompt='Vehicle make', help='Vehicle make')
@click.option('--model', prompt='Vehicle model', help='Vehicle model')
@click.option('--year', prompt='Vehicle year', type=int, help='Vehicle year')
@click.option('--license', prompt='License plate', help='License plate number')
def add_vehicle(customer_id, make, model, year, license):
    """Add a new vehicle"""
    vehicle = Vehicle(customer_id=customer_id, make=make, model=model, year=year, license_plate=license)
    session.add(vehicle)
    session.commit()
    click.echo(f"Vehicle {make} {model} added successfully!")

@cli.command()
@click.option('--vehicle-id', prompt='Vehicle ID', type=int, help='Vehicle ID')
@click.option('--services', prompt='Services offered', help='Services provided')
@click.option('--cost', prompt='Total cost', type=float, help='Total cost')
def add_tint_job(vehicle_id, services, cost):
    """Add a new tint job"""
    tint_job = TintJob(vehicle_id=vehicle_id, service_date=datetime.now(), services_offered=services, total_cost=cost)
    session.add(tint_job)
    session.commit()
    click.echo(f"Tint job added successfully!")

@cli.command()
@click.option('--job-id', prompt='Tint job ID', type=int, help='Tint job ID')
@click.option('--amount', prompt='Payment amount', type=float, help='Payment amount')
def record_payment(job_id, amount):
    """Record a payment"""
    payment = Payment(tint_job_id=job_id, payment_date=datetime.now(), amount_paid=amount)
    session.add(payment)
    session.commit()
    click.echo(f"Payment of ${amount} recorded successfully!")

@cli.command()
def list_customers():
    """List all customers"""
    customers = session.query(Customer).all()
    for customer in customers:
        click.echo(f"ID: {customer.id}, Name: {customer.name}, Phone: {customer.phone_number}, Email: {customer.email}")

@cli.command()
def list_vehicles():
    """List all vehicles"""
    vehicles = session.query(Vehicle).all()
    for vehicle in vehicles:
        click.echo(f"ID: {vehicle.id}, Customer ID: {vehicle.customer_id}, {vehicle.year} {vehicle.make} {vehicle.model}, License: {vehicle.license_plate}")

@cli.command()
@click.argument('customer_id', type=int)
def delete_customer(customer_id):
    """Delete a customer by ID"""
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        click.echo(f"Customer {customer.name} deleted successfully!")
    else:
        click.echo("Customer not found!")

@cli.command()
@click.argument('vehicle_id', type=int)
def delete_vehicle(vehicle_id):
    """Delete a vehicle by ID"""
    vehicle = session.query(Vehicle).filter_by(id=vehicle_id).first()
    if vehicle:
        session.delete(vehicle)
        session.commit()
        click.echo(f"Vehicle {vehicle.make} {vehicle.model} deleted successfully!")
    else:
        click.echo("Vehicle not found!")

@cli.command()
def list_jobs():
    """List all tint jobs"""
    jobs = session.query(TintJob).all()
    for job in jobs:
        vehicle = session.query(Vehicle).filter_by(id=job.vehicle_id).first()
        click.echo(f"Job ID: {job.id}, Vehicle: {vehicle.make} {vehicle.model}, Services: {job.services_offered}, Cost: ${job.total_cost}")

@cli.command()
def outstanding_payments():
    """Show jobs with outstanding payments"""
    jobs = session.query(TintJob).all()
    for job in jobs:
        payments = session.query(Payment).filter_by(tint_job_id=job.id).all()
        total_paid = sum(p.amount_paid for p in payments)
        outstanding = job.total_cost - total_paid
        if outstanding > 0:
            vehicle = session.query(Vehicle).filter_by(id=job.vehicle_id).first()
            customer = session.query(Customer).filter_by(id=vehicle.customer_id).first()
            click.echo(f"Customer: {customer.name}, Vehicle: {vehicle.make} {vehicle.model}, Outstanding: ${outstanding}")

@cli.command()
def sales_report():
    """Generate comprehensive sales report"""
    jobs = session.query(TintJob).all()
    payments = session.query(Payment).all()
    
    total_sales = sum(job.total_cost for job in jobs)
    total_payments = sum(payment.amount_paid for payment in payments)
    outstanding = total_sales - total_payments
    
    click.echo("=== SALES REPORT ===")
    click.echo(f"Total Jobs: {len(jobs)}")
    click.echo(f"Total Sales: ${total_sales:.2f}")
    click.echo(f"Total Payments Received: ${total_payments:.2f}")
    click.echo(f"Outstanding Balance: ${outstanding:.2f}")
    click.echo(f"Average Job Value: ${total_sales/len(jobs):.2f}" if jobs else "No jobs recorded")

@cli.command()
def customer_loyalty():
    """Show customer loyalty report"""
    customers = session.query(Customer).all()
    customer_data = []
    
    for customer in customers:
        vehicles = session.query(Vehicle).filter_by(customer_id=customer.id).all()
        total_jobs = 0
        total_spent = 0
        
        for vehicle in vehicles:
            jobs = session.query(TintJob).filter_by(vehicle_id=vehicle.id).all()
            total_jobs += len(jobs)
            total_spent += sum(job.total_cost for job in jobs)
        
        customer_data.append((customer.name, total_jobs, total_spent))
    
    # Sort by total spent (descending)
    customer_data.sort(key=lambda x: x[2], reverse=True)
    
    click.echo("=== CUSTOMER LOYALTY REPORT ===")
    for name, jobs, spent in customer_data:
        click.echo(f"{name}: {jobs} jobs, ${spent:.2f} total spent")

if __name__ == '__main__':
    cli()