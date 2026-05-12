# Market Management System

## Overview

This project is a command-line Python application for managing sellers, products, orders, schedules, and sessions. It provides a simple marketplace-style management system where sellers can:

* Manage inventory and stock
* Create and process customer orders
* Manage seller records
* Create schedules
* Assign sessions to schedules
* Persist data using JSON files

The application is modular and organized into multiple Python files, each responsible for a specific feature.

---

# Project Structure

```text
src/
│
├── main.py                 # Main application menu and navigation
├── general_functions.py    # Shared validation and utility functions
├── product.py              # Product and inventory management
├── orders_module.py        # Shopping cart and order handling
├── sellers.py              # Seller management
├── schedule.py             # Weekly schedule creation and handling
├── sessions.py             # Session booking and management
├── saves/                  # Save directory (currently empty)
└── __pycache__/            # Python cache files
```

---

# Features

## 1. Seller Management

The system allows you to:

* Create sellers
* Read seller information
* Update seller data
* Delete sellers
* Assign product types and descriptions

Seller data is stored in:

```text
sellers.json
```

---

## 2. Product Management

Each seller can manage their own inventory.

### Available Operations

* Create products
* Update product details
* Delete products
* Read products by ID
* Track stock quantity
* Organize products by class/category

### Product Data Includes

* Product ID
* Product name
* Product class
* Price
* Quantity

Product data is stored in:

```text
products.json
```

---

## 3. Order Management

The order module works like a shopping cart system.

### Features

* Add items to cart
* Update cart quantities
* Remove items from cart
* Read current cart contents
* Automatically update stock quantities

Order data is stored in:

```text
orders.json
```

---

## 4. Schedule Management

The schedule system creates weekly schedules.

### Features

* Create schedules
* Assign days of the week
* Store week ranges
* Update schedules
* Delete schedules

---

## 5. Session Management

Sessions are linked to schedules and sellers.

### Features

* Create sessions
* Assign sellers to time slots
* Assign days and hours
* Read session information
* Prevent overbooking

### Time Slots

Sessions are available from:

```text
8:00 - 18:00
```

with hourly intervals.

Session data is stored in:

```text
sessions.json
```

---

# Requirements

## Python Version

Recommended:

```text
Python 3.11+
```

---

## External Libraries

Install dependencies using:

```bash
pip install tabulate
```

---

# Running the Project

## Step 1 — Extract the Project

Extract the ZIP file.

---

## Step 2 — Open Terminal

Navigate to the project folder:

```bash
cd src
```

---

## Step 3 — Run the Application

```bash
python main.py
```

---

# Main Menu

When the application starts, you will see:

```text
======Menu======
1 - Select seller
2 - Edit sellers
3 - Sessions
4 - Schedule
5 - Leave
```

---

# Data Persistence

The application uses JSON files to save information between runs.

## Files Used

| File          | Purpose                   |
| ------------- | ------------------------- |
| sellers.json  | Stores seller information |
| products.json | Stores product inventory  |
| orders.json   | Stores order/cart data    |
| sessions.json | Stores session schedules  |

---

# Module Breakdown

## main.py

Controls:

* Menu navigation
* User interaction
* Module integration

This file acts as the application entry point.

---

## general_functions.py

Contains reusable helper functions:

* Input validation
* Float validation
* Range checking
* Pause functionality
* JSON save/load helpers

---

## product.py

Responsible for inventory management.

### Core Functions

```python
create_product()
update_product()
delete_product()
read_product_by_id()
```

---

## orders_module.py

Handles shopping cart logic and stock updates.

### Core Functions

```python
create_item_order()
update_item_order()
delete_item_order()
read_item_order()
```

---

## sellers.py

Manages seller records.

### Core Functions

```python
create_seller()
read_sellers()
update_seller()
delete_sellers()
```

---

## schedule.py

Creates and manages weekly schedules.

### Core Functions

```python
create_schedule()
update_schedule()
delete_schedule()
read_schedule()
```

---

## sessions.py

Controls seller session booking.

### Core Functions

```python
create_session()
read_session()
update_session()
delete_session()
```

---

# Example Workflow

## Example Usage

1. Create a seller
2. Add products for that seller
3. Create a schedule
4. Create sessions for the seller
5. Add products to an order
6. Finalize the order

---

# Known Issues / Improvements

The project works as a learning management system prototype, but several improvements can still be made:

## Suggested Improvements

* Add exception handling
* Improve variable naming consistency
* Add database support (SQLite/PostgreSQL)
* Create unit tests
* Improve menu organization
* Add authentication/login system
* Improve JSON structure
* Add order finalization receipts
* Add stock validation for insufficient quantity
* Improve session conflict checking

---

# Future Enhancements

Possible future upgrades:

* GUI interface using Tkinter or PyQt
* Web API using Flask or FastAPI
* Export reports to CSV/PDF
* Barcode scanning support
* Multi-user support
* Analytics dashboard

---

# Author Notes

This project demonstrates:

* Python modular programming
* File persistence using JSON
* CRUD operations
* CLI application structure
* Inventory and session management logic

It is a strong foundation for expanding into a complete marketplace or scheduling system.

---

# License

This project is for educational and personal development purposes.
