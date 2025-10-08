# 🏢 Student Dormitory Management System

This repository contains a simple, modular Python application designed to simulate the core administrative functions of a student dormitory. This includes user authentication, managing student records, tracking attendance, and handling leave applications.

---

## 🌟 Features

The system is broken down into separate, easy-to-manage Python modules, each handling a specific domain:

* **User Authentication (`auth.py`):** Secure user registration and login with basic password hashing (SHA-256). Supports different user roles (e.g., 'student', 'admin').
* **Student Database (`database.py`):** Stores and retrieves essential student records, including name and room number.
* **Attendance Tracking (`attendance.py`):** Logs student check-in and check-out times with automatic timestamps.
* **Leave Management (`leave.py`):** Allows students to submit leave requests and enables administrators to review and update the status of those requests.
* **Dashboard (`dashboard.py`):** Provides aggregated views of attendance logs and leave request statuses.

---

## 🛠️ Technology Stack

* **Language:** Python 3.x
* **Core Libraries:** `hashlib` (for password security), `datetime` (for attendance timestamps)
* **Data Storage:** In-memory Python Dictionaries (Data is non-persistent and reset on each run).

---

## 🚀 Getting Started

Follow these instructions to set up and run the system locally.

### Prerequisites

You must have **Python 3.x** installed on your machine.

### Installation

No external packages are required beyond the standard Python library.

1.  **Clone or Download:** Save all the provided code snippets into their corresponding files (`auth.py`, `attendance.py`, `leave.py`, `database.py`, `dashboard.py`, and `main.py`) in the same directory.
2.  **Ensure File Structure:** Your directory should look like this:

    ```
    /src
    ├── auth.py
    ├── attendance.py
    ├── leave.py
    ├── database.py
    ├── dashboard.py
    └── main.py
    ```

### Execution

Run the demonstration script using the Python interpreter:

```bash
python main.py
