# Employee Management System

A simple command-line Employee Management System built in Python. It lets you add, view, search, update, and delete employee records, view salary/department statistics, and persists all data to a local JSON file so nothing is lost between runs.

## Features

- **Add Employee** — enter ID, name, age, department, salary, and a list of skills
- **View Employees** — display all stored employee records
- **Search Employee** — search by ID or by name
- **Update Employee** — update department, salary, or skills without recreating the record
- **Delete Employee** — remove an employee record (with confirmation)
- **Show Statistics** — total employees, average/highest/lowest salary, and employee count per department
- **Data Persistence** — all changes are saved to `employees.json` automatically
- **Input Validation** — rejects invalid IDs/ages (non-numeric), empty names/departments, and negative or zero salaries

## Project Structure

```
Employee Management System/
├── index.py              # Entry point — runs the menu loop
├── employee.py            # Employee class (data model, validation, JSON conversion)
├── employee_manager.py     # Business logic — add, view, search, update, delete, statistics
├── utils.py                # Reusable helpers — input validation, save/load JSON
└── employees.json          # Auto-generated data file (created on first save)
```

## How It Works

- **`employee.py`** defines the `Employee` class. Salary is managed through a Python `@property`, so any attempt to set a negative or zero salary raises a `ValueError`, whether it happens during creation or an update.
- **`employee_manager.py`** holds the in-memory list of employees and all the CRUD operations that act on it.
- **`utils.py`** contains input-validation helpers (`get_valid_int`, `get_non_empty_input`) and the JSON save/load functions, so validation logic isn't duplicated across the app.
- **`index.py`** is the only file that runs the menu loop — it loads saved data on startup and dispatches each menu choice to the right function in `employee_manager.py`.

## Requirements

- Python 3.x (no external libraries required — uses only the standard library: `json`, `os`)

## Running the Project

```bash
git clone <your-repo-url>
cd "Employee Management System"
python index.py
```

## Example Usage

```
========== Operations =========
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Show Statistics
7. Exit
Choice: 1

--------Enter Employee Details---------
Enter Employee ID: 1
Enter Employee Name: Asjad
Enter Employee Age: 26
Enter Employee Department: Computer Science
Enter Employee Skills: Python
Enter Employee Skills: Django
Enter Employee Skills: done
Enter Employee Salary: 90000

--------Employee Details---------
id             :    1
Name           :    Asjad
Age            :    26
Department     :    Computer Science
Salary         :    90000
Skills         :    Python, Django
Asjad added.
```

## Statistics Example

```
========== Employee Statistics ==========
Total Employees : 5
Average Salary  : 72,500
Highest Salary  : 100,000
Lowest Salary   : 45,000

Departments:
  Software Development : 3
  IT                   : 1
  HR                   : 1
```

## Data Storage

All employee data is stored in `employees.json`, in the same folder as the project, and is automatically created the first time you add an employee. The file is re-read on every startup, so your data persists across sessions.

## Possible Future Improvements

- Export statistics or employee lists to CSV
- Add sorting (by salary, age, department) when viewing employees
- Add case-insensitive / partial-match name search
- Move from a flat JSON file to a lightweight database (e.g. SQLite) as the dataset grows

## Author

Built as a learning project to practice Python fundamentals: object-oriented programming, properties/setters, input validation, JSON persistence, and building a menu-driven CLI application.
