import json
import os

DATA_FILE = "employees.json"

def get_valid_int(prompt, allow_negative=True, min_value=None):
    """Keep asking until the user enters a valid integer (optionally with constraints)."""

    while True:
        try:
            value = int(input(prompt))
            if not allow_negative and value < 0:
                print("Value cannot be negative.")
                continue
            elif min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}. Please try again.")
                continue
            return value
                
        except ValueError:
            print(f"Invalid input: Please try again.")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please Try again")

def save_employees(employees):
    """Save a list of Employee objects to a JSON file."""
    data = [employee.to_dict() for employee in employees]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_employees():
    """Load employees from JSON file, returning a list of Employee objects."""
    from employee import Employee

    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return [Employee.from_dict(item) for item in data]
