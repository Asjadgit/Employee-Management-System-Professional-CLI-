from utils import get_valid_int, get_non_empty_input, save_employees
from employee import Employee


employees = []
def enter_employee_details():
    print("--------Enter Employee Details---------")
    id   = get_valid_int("Enter Employee ID: ")
    name = get_non_empty_input("Enter Employee Name: ")
    age  = get_valid_int("Enter Employee Age: ")
    department  = get_non_empty_input("Enter Employee Department: ")
    while True:
        try:
            salary      = int(input("Enter Employee Salary: "))
            employee = Employee(id, name, age, department, salary)
            employees.append(employee)
            save_employees(employees)
            break
        except ValueError as error:
            print(f"Invalid input: {error} Please try again.")
    print(f"{name} added.\n")


def show_all_employees():
    if not employees:
        print("No employees added yet.")
        return
    for employee in employees:
        employee.display_employee()


def update_employee_details():
    print("--------Enter Employee ID for Updating---------")
    employee_id   = get_valid_int("Enter Employee ID: ")


