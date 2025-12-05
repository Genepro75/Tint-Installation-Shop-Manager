# Tint Installation Shop Manager

A command-line interface (CLI) application for managing a tint installation shop. This application helps track customers, vehicles, tint jobs, and payments using a SQLite database with SQLAlchemy ORM.

## Learning Goals Demonstrated

This project demonstrates all Phase 3 learning objectives:

1. **CLI Application**: Interactive command-line interface that solves the real-world problem of managing a tint installation business
2. **SQLAlchemy ORM**: Database with 4 related tables using proper foreign key relationships
3. **Pipenv Environment**: Well-maintained virtual environment with dependency management
4. **Package Structure**: Organized code following separation of concerns principle
5. **Data Structures**: Implementation of lists, dictionaries, and tuples throughout the application

## Features

- **Customer Management**: Add and track customer information
- **Vehicle Registration**: Register vehicles for customers
- **Job Tracking**: Create and manage tint installation jobs with different tint types and coverage options
- **Payment Processing**: Record payments and track outstanding balances
- **Reporting**: Generate sales reports and view business metrics
- **Database Integration**: Persistent data storage with SQLAlchemy ORM

## Project Structure

```
tint_shop_cli/
├── Pipfile                 # Dependencies and Python version
├── README.md               # Project documentation
└── lib/
    ├── models/
    │   ├── __init__.py     # Database configuration and constants
    │   ├── customer.py     # Customer model class
    │   ├── vehicle.py      # Vehicle model class
    │   ├── tint_job.py     # TintJob model class
    │   └── payment.py      # Payment model class
    ├── cli.py              # Main CLI interface and menu system
    ├── helpers.py          # Helper functions for CRUD operations
    └── debug.py            # Debug script with sample data
```

## Database Schema

The application uses SQLite with four related tables:

### 1. customers
- `id` (Integer, Primary Key)
- `name` (String, Required)
- `phone` (String, Optional)
- `email` (String, Optional)

### 2. vehicles
- `id` (Integer, Primary Key)
- `customer_id` (Integer, Foreign Key -> customers.id)
- `make` (String, Required)
- `model` (String, Required)
- `year` (Integer, Optional)
- `license_plate` (String, Optional)

### 3. tint_jobs
- `id` (Integer, Primary Key)
- `vehicle_id` (Integer, Foreign Key -> vehicles.id)
- `service_date` (DateTime, Default: now)
- `tint_type` (String, Required) - "Ceramic", "Carbon", or "Dyed"
- `window_coverage` (String, Required) - "Full", "Front Only", or "Rear Only"
- `cost` (Float, Required)
- `status` (String, Default: "Pending") - "Pending", "In Progress", or "Completed"

### 4. payments
- `id` (Integer, Primary Key)
- `tint_job_id` (Integer, Foreign Key -> tint_jobs.id)
- `amount` (Float, Required)
- `payment_date` (DateTime, Default: now)
- `payment_method` (String, Default: "Cash") - "Cash", "Credit Card", or "Check"

### Relationships
- **Customer → Vehicles**: One-to-Many (one customer can have many vehicles)
- **Vehicle → TintJobs**: One-to-Many (one vehicle can have many tint jobs)
- **TintJob → Payments**: One-to-Many (one job can have multiple payments)

## Installation and Setup

1. **Navigate to project directory:**
   ```bash
   cd tint_shop_cli
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   ```

3. **Activate virtual environment:**
   ```bash
   pipenv shell
   ```

4. **Create sample data (optional):**
   ```bash
   python lib/debug.py
   ```

## Usage

### Running the Application

```bash
python lib/cli.py
```

Or make it executable:
```bash
chmod +x lib/cli.py
./lib/cli.py
```

### Available Menu Options

- **0. Exit the program** - Exit the CLI application
- **1. Add new customer** - Register customer information (name, phone, email)
- **2. List all customers** - View customer directory
- **3. Add new vehicle** - Register vehicles for existing customers
- **4. List all vehicles** - View vehicle inventory with customer information
- **5. Create tint job** - Create new tint installation jobs with type and coverage options
- **6. List all tint jobs** - View all jobs with customer and vehicle details
- **7. Record payment** - Process payments for jobs with payment method selection
- **8. List all payments** - View payment history
- **9. View sales report** - Generate business metrics (total jobs, revenue, outstanding balance)
- **10. View outstanding payments** - Show jobs with remaining balances

## File Descriptions

### lib/cli.py
The main CLI interface that provides the interactive menu system. This file imports helper functions and creates a user-friendly command-line experience. It handles user input validation and menu navigation. The `main()` function runs the primary loop, displaying the menu and processing user choices. Helper menu functions like `add_customer_menu()`, `add_vehicle_menu()`, `create_tint_job_menu()`, and `record_payment_menu()` provide interactive prompts for data entry.

### lib/helpers.py
Contains all the helper functions that perform CRUD (Create, Read, Update, Delete) operations on the database. Each function handles a specific business operation:

- **Customer operations**: `add_customer()`, `list_customers()`, `find_customer_by_id()`
- **Vehicle operations**: `add_vehicle()`, `list_vehicles()`, `find_vehicle_by_id()`
- **Tint Job operations**: `create_tint_job()`, `list_tint_jobs()`, `find_tint_job_by_id()`
- **Payment operations**: `record_payment()`, `list_payments()`
- **Reporting functions**: `sales_report()`, `outstanding_payments()`
- **Utility functions**: `get_session()`, `create_tables()`, `exit_program()`

These functions use SQLAlchemy sessions to interact with the database and include proper error handling and user feedback.

### lib/models/
This directory contains all the database model classes:

- **__init__.py**: Sets up database connection, engine, and session configuration. Imports all models to ensure they're registered with the Base declarative class.
- **customer.py**: Defines the Customer model with a one-to-many relationship to vehicles. Includes cascade delete to remove vehicles when a customer is deleted.
- **vehicle.py**: Defines the Vehicle model linking customers to tint jobs. Contains foreign key to customers and relationships to both customers and tint jobs.
- **tint_job.py**: Defines the TintJob model for tracking services, costs, and status. Includes relationships to vehicles and payments.
- **payment.py**: Defines the Payment model for financial transactions. Links to tint jobs and tracks payment method and date.

### lib/debug.py
A utility script that creates sample data for testing the application. The `debug()` function populates the database with example customers, vehicles, jobs, and payments. Run this to quickly set up test data without manual entry.

## Data Structures Used

- **Lists**: Used extensively for displaying multiple database records (customers, vehicles, jobs, payments). Functions like `list_customers()`, `list_vehicles()`, and `list_tint_jobs()` return lists of model instances.
- **Dictionaries**: Utilized in SQLAlchemy model relationships and query results. The `sales_report()` function returns a dictionary with report metrics.
- **Tuples**: Employed for data validation and database operation results. Used implicitly in SQLAlchemy query results and relationship mappings.

## Testing

To test the application with sample data:

```bash
python lib/debug.py
python lib/cli.py
```

The debug script will create sample records that you can interact with through the CLI.

## Technical Implementation

- **Database**: SQLite with SQLAlchemy ORM
- **Python Version**: 3.8+
- **Dependencies**: SQLAlchemy for database operations
- **Architecture**: Modular design with separation of concerns
- **Error Handling**: Input validation and graceful error management
- **Cascade Deletes**: Properly configured to maintain referential integrity

## Example Workflow

1. Add a customer: "John Smith" with phone and email
2. Add a vehicle for that customer: "2020 Toyota Camry" with license plate
3. Create a tint job: Ceramic tint, Full coverage, $450.00
4. Record a payment: $200.00 partial payment via Credit Card
5. View sales report to see total revenue and outstanding balance
6. View outstanding payments to see remaining balance ($250.00)

This project demonstrates practical application of Python programming concepts in a real-world business scenario, making it an excellent learning tool for understanding CLI development, database design, and object-relational mapping.

