# SmartStock — Supermarket Inventory Management System

A Python-based supermarket inventory management application built using Object-Oriented Programming (OOP).

## Project Overview

SmartStock is a command-line inventory management system designed to help supermarket staff track product availability, record sales, replenish shelves, and manage deliveries.

The project is inspired by practical supermarket stock management operations.

## Features

- **Product Management:** View product information and stock quantities.
- **Stock Tracking:** Calculate total inventory across shelves and backstock.
- **Sales Management:** Reduce shelf stock when products are sold.
- **Shelf Replenishment:** Transfer inventory from backstock to shelves.
- **Delivery Management:** Add incoming stock to backstock.
- **Product Search:** Find products using unique product codes.
- **Low-Stock Alerts:** Display warnings when total stock falls below 10 units.
- **Input Validation:** Reject invalid quantities and prevent selling more than the available shelf stock.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Python dictionaries
- Loops and conditional statements
- Exception handling

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run:

```bash
python smartstock.py
```

5. Follow the on-screen menu to manage products.

No external Python packages are required.

## Sample Menu

```text
===== SMARTSTOCK =====
1. View all products
2. Search product
3. Sell product
4. Replenish shelf
5. Receive delivery
6. Exit
```

## Example

Initial Whole Milk inventory:

- Shelf Stock: 20
- Backstock: 40
- Total Stock: 60

After selling 5 bottles:

- Shelf Stock: 15
- Backstock: 40
- Total Stock: 55

Replenishing 5 bottles moves stock from backstock to shelves without changing total inventory.

## Current Limitations

- Inventory is stored in memory and resets when the program restarts.
- Products are currently predefined in the Python code.
- The application uses a terminal interface rather than a graphical interface.

## Planned Improvements

- JSON or database storage
- Product pricing and sales reports
- Wastage and reduction tracking
- Automated testing
- Improved inventory reporting

## Project Status

**Version 1 — Prototype / In Development**

This is a personal learning project developed with AI-assisted guidance while practising Python and OOP concepts. Additional features and improvements are planned.

## Author

**Ashwin Purushothaman**

MSc Data Science & Analytics  
University of Hertfordshire
