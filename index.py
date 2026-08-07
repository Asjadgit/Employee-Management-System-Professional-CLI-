from employee_manager import enter_employee_details, show_all_employees
import employee_manager
from utils import get_non_empty_input, load_employees

def show_menu():
    employees = load_employees()
    print("\n========== Operations =========")
    print("1. Add Employee")

    print("2. View Employees")

    print("3. Search Employee")

    print("4. Update Employee")

    print("5. Delete Employee")

    print("6. Show Statistics")

    print("7. Save Data")

    print("8. Load Data")

    print("9. Exit")

employee_manager.employees = load_employees()

while True:
    show_menu()
    choice = get_non_empty_input("Choice: ")

    if choice == "1":
        enter_employee_details()
    elif choice == "2":
        show_all_employees()