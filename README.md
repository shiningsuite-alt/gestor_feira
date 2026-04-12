# gestor_feira
Feira
Here’s a clean, professional **README.md** for your project based on the code structure and functionality:

---

# 🛒 Market Management System

A command-line Python application for managing a small marketplace.
It allows you to handle **items, orders, sellers, and scheduling** in an organized way.

---

## 📦 Features

### 🧾 Order Management

* Add items to an order
* Remove items from an order
* Edit item quantities
* View current order
* Automatically updates item stock

### 📦 Item Management

* Store items with:

  * Name
  * Price
  * Quantity
  * ID
* Supports item classification (categories)

### 👨‍🌾 Seller Scheduling

* Add sellers to a timetable
* Assign:

  * Day
  * Time slot
  * Product type
  * Description
* View schedule in a table format
* Edit or remove sellers

### 📅 Weekly Schedule

* Covers:

  * Monday to Friday
  * Time slots from 08:00 to 17:10
* Displays:

  * Empty slots
  * Partially filled slots
  * Full slots

---

## 📁 Project Structure

```
src/
│── main.py               # Entry point of the program
│── general_functions.py # Utility & validation functions
│── items_file.py        # Item storage and definitions
│── orders_module.py     # Order logic (core functions)
│── order_item.py        # Interactive order handling
│── schedule.py          # Seller scheduling system
```

---

## ▶️ How to Run

1. Make sure you have Python 3 installed
2. Install required dependency:

```bash
pip install tabulate
```

3. Run the program:

```bash
python src/main.py
```

---

## 🧠 How It Works

### Orders

* Items are selected by:

  * Name
  * Class
  * ID
* Quantities are validated before adding
* Stock updates automatically when items are added/removed

### Schedule System

* Sellers are assigned to specific:

  * Days
  * Time slots
* Each seller gets a unique ID
* Schedule is displayed in a formatted table

---

## ⚠️ Known Limitations

* Data is stored **in memory only** (no database or file persistence)
* Some functions may have minor bugs (e.g., seller editing logic)
* No GUI (command-line only)

---

## 🚀 Possible Improvements

* Add file/database persistence (JSON, SQLite)
* Build a GUI (Tkinter, PyQt, or web app)
* Improve error handling
* Add authentication (admin/seller roles)
* Refactor duplicated logic in order modules

---

## 🛠️ Technologies Used

* Python 3
* `tabulate` (for table display)

---

## 📌 Author Notes

This project is a solid foundation for:

* Learning Python modular design
* Practicing CLI-based applications
* Understanding basic inventory & scheduling systems
