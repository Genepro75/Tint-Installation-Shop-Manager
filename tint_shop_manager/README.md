# Tint Installation Shop Manager

A CLI application for managing a tint installation shop with customer records, vehicle tracking, job management, and payment processing.

## Features

- Customer management (add, list)
- Vehicle tracking with customer relationships
- Tint job scheduling and tracking
- Payment recording and tracking
- Sales reporting
- SQLite database with SQLAlchemy ORM
- Command-line interface with Click

## Installation

1. Navigate to the project directory:
```bash
cd tint_shop_manager
```

2. Install dependencies:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

## Usage

Run the application:
```bash
python test_app.py [COMMAND] [OPTIONS]
```

### Available Commands

- `add-customer` - Add a new customer
- `add-vehicle` - Add a new vehicle for a customer
- `add-tint-job` - Create a new tint job
- `record-payment` - Record a payment for a job
- `list-customers` - List all customers
- `list-vehicles` - List all vehicles
- `sales-report` - Generate sales report

### Example Usage

```bash
# Add a customer
python test_app.py add-customer --name "John Doe" --phone "555-1234" --email "john@example.com"

# Add a vehicle
python test_app.py add-vehicle --customer-id 1 --make "Toyota" --model "Camry" --year 2020 --license "ABC123"

# Create a tint job
python test_app.py add-tint-job --vehicle-id 1 --services "Full tint package" --cost 350.00

# Record payment
python test_app.py record-payment --job-id 1 --amount 350.00

# View reports
python test_app.py sales-report
```

## Database Schema

The application uses SQLite with the following tables:
- `customers` - Customer information
- `vehicles` - Vehicle details linked to customers
- `tint_jobs` - Tint installation jobs
- `payments` - Payment records for jobs

## Project Structure

```
tint_shop_manager/
├── app/
│   ├── __init__.py
│   ├── cli.py              # CLI commands
│   ├── models/
│   │   ├── __init__.py
│   │   ├── customer.py     # Customer model
│   │   ├── vehicle.py      # Vehicle model
│   │   ├── tint_job.py     # TintJob model
│   │   └── payment.py      # Payment model
│   └── database/
│       ├── __init__.py
│       └── db.py           # Database configuration
├── Pipfile                 # Dependencies
├── test_app.py            # Application entry point
└── README.md              # This file
```