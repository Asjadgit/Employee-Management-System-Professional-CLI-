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

    print("7. Exit")

employee_manager.employees = load_employees()

while True:
    show_menu()
    choice = get_non_empty_input("Choice: ")

    if choice == "1":
        employee_manager.enter_employee_details()
    elif choice == "2":
        employee_manager.show_all_employees()
    elif choice == "3":
        employee_manager.search_employee()
    elif choice == "4":
        employee_manager.update_employee_details()
    elif choice == "5":
            employee_manager.delete_employee()
    elif choice == "6":
        employee_manager.statistics()
    elif choice == "7":
        print("Goodbye!")
        break