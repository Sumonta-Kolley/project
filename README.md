# 📱 Mobile Shop Management System (CRUD)

A beginner-friendly console-based CRUD (Create, Read, Update, Delete) application built using Python to manage mobile store inventory efficiently.

---

## 📌 Features

- **Add Mobile:** Insert new mobile records with unique IDs, brand, model, price, and stock quantity.
- **Display Mobiles:** View all stored mobiles in a clean, formatted table.
- **Search Mobile:** Quickly search for any mobile phone using its unique ID.
- **Update Mobile:** Modify existing mobile details such as brand, model, price, or quantity.
- **Delete Mobile:** Remove records from inventory with a confirmation prompt.
- **Interactive Menu:** Simple number-based console menu to navigate through features.

---

## 🛠️ Tech Stack & Concepts Used

- **Language:** Python 3.x
- **Data Structure:** Python Lists (Nested list structure: `[id, brand, model, price, quantity]`)
- **Key Concepts:**
  - Functions (`def`)
  - Loops (`while`, `for`)
  - Conditional Statements (`if-elif-else`)
  - User Input & String Formatting (`f-strings`)

---

## 📂 Data Structure Representation

Each mobile record is saved as a list inside the primary `mobiles` list:

```python
mobiles = [
    [101, "Samsung", "Galaxy A55", 35000.0, 5],
    [102, "Apple", "iPhone 15", 65000.0, 3],
    [103, "OnePlus", "Nord 4", 30000.0, 7]
]
