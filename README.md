# Restaurant Management & Billing System

A modular Python command-line application designed for restaurant order management, automated bill calculation, itemized receipt generation, and flexible payment processing.

---

## Overview

The **Restaurant Management & Billing System** is a lightweight, terminal-based application built with Python. It provides a structured interface for managing restaurant orders, displaying menu items across multiple categories, calculating itemized sub-totals with automated GST (5%) and delivery charge calculations, and processing payments via Cash, UPI, or Card.

---

## Features

- **Categorized Menu Display:** Organizes 50 dishes across multiple food categories including Combos, Starters, Main Course, South Indian, Desserts, Beverages, and Special Items.
- **Flexible Order Input:** Allows ordering multiple item numbers at once by entering space-separated menu item codes.
- **Dynamic Bill Calculation:** Automatically computes subtotal, GST (5%), and fixed delivery charges (₹40) to determine the grand total.
- **Multi-Method Payment Handling:**
  - **Cash Payment:** Supports partial cash input and accurately calculates change to return.
  - **UPI Payment:** Interactive UPI terminal interface with ASCII QR display simulation.
  - **Card Payment:** Prompt-driven payment flow.
- **Itemized Receipts:** Outputs clean formatted invoices and final receipts for customer documentation.
- **Modular Code Architecture:** Structured across separate modules (`main.py`, `menu_display.py`, `menu_data.py`, `order_processing.py`, and `billing_and_payment.py`) for clean code separation and easy maintenance.

---

## Technologies/Tools Used

- **Language:** Python 3.x
- **Standard Libraries:** Native built-in functions (`input()`, `print()`, basic data structures)
- **Architecture:** Modular Python Programming

---

## File Structure

```text
├── main.py                 # Application entry point
├── menu_display.py         # Visual menu layout and formatting
├── menu_data.py            # Menu dictionary database and lookup functions
├── order_processing.py     # Functions handling order selection and quantity input
└── billing_and_payment.py  # Logic for billing calculations, payment, and receipt generation
```

---

## Steps to Install & Run the Project

### Prerequisites

Ensure you have Python installed on your system (Python 3.6 or higher recommended). You can verify your installation by running:

```bash
python --version
```

### Installation

1. **Clone or Download the Repository:**
   
   git clone: https://github.com/arpiitttxd/VITyarthi-project  
   Navigate into the project folder: cd VITyarthi-project

3. **Verify Project Files:**
   Ensure all `.py` files are located in the same directory:
   - `main.py`
   - `menu_data.py`
   - `menu_display.py`
   - `order_processing.py`
   - `billing_and_payment.py`

### Running the Application

Execute the main script from your terminal or command prompt:

```bash
python main.py
```

---

## Instructions for Testing

Follow these step-by-step cases to verify that the application operates correctly across different scenarios:

### Test Case 1: Standard Multi-Item Order (Cash Payment)
1. Launch the program: `python main.py`
2. Enter Customer Name when prompted: `Rahul`
3. When prompted `What You Want! :`, enter multiple menu item numbers separated by space: `1 23 48` *(Combo Shahi Thali, Masala Chai, Pizza)*
4. Enter quantities when prompted:
   - Quantity for Combo Shahi Thali: `1`
   - Quantity for Masala Chai: `2`
   - Quantity for Pizza: `1`
5. Review the generated bill breakdown (Subtotal, GST 5%, Delivery Charge ₹40).
6. Select Payment Method: `1` (Cash).
7. Enter Cash Amount: Enter an amount greater than the Grand Total (e.g., `1200`) and verify that the change returned is calculated correctly.

### Test Case 2: UPI / Card Payment
1. Run `python main.py`
2. Enter Customer Name: `Ananya`
3. Enter choice: `27 36` *(Paneer Tikka, Butter Naan)*
4. Enter quantities for each item.
5. Select Payment Method: `2` (UPI) or `3` (Card).
6. Confirm that the final receipt displays the accurate payment method and itemized total.

### Test Case 3: Invalid Item Handling
1. Run `python main.py`
2. Enter choice with an invalid menu number (e.g., `99` or `0`): `1 99 18`
3. Verify that the terminal displays `99 is NOT AVAILABLE` while continuing to process the valid items (`1` and `18`).

### Test Case 4: Zero Items / Empty Order
1. Run `python main.py`
2. Enter an invalid menu code or `0`.
3. Verify that the application gracefully displays `"No valid items were ordered. Thank you for visiting!"` without crashing.
