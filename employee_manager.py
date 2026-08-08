from utils import get_valid_int, get_non_empty_input, save_employees
from employee import Employee


employees = []

def add_skills():
    skills    = []
    while True:
        skill = get_non_empty_input("Enter Employee Skills: ")
        if skill == "done":
            break
        skills.append(skill)
    return skills

def enter_employee_details():
    print("--------Enter Employee Details---------")
    id   = get_valid_int("Enter Employee ID: ")
    name = get_non_empty_input("Enter Employee Name: ")
    age  = get_valid_int("Enter Employee Age: ")
    department  = get_non_empty_input("Enter Employee Department: ")
    skills  = add_skills()
    while True:
        try:
            salary      = int(input("Enter Employee Salary: "))
            employee = Employee(id, name, age, department, salary, skills)
            employees.append(employee)
            # employee.display_employee()
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


def search_employee():
    print("--------Search Employee---------")
    query = get_non_empty_input("Enter Employee ID or Name to search: ")

    found = False

    if query.isdigit():
        employee_id = int(query)
        for employee in employees:
            if employee_id == employee.employee_id:
                # print("No employees added yet.")
                employee.display_employee()
                found = True
            
    else:
        for employee in employees:
            if query == employee.employee_name:
            # print("No employees added yet.")
                employee.display_employee()
                found = True

    if not found:       
        print("No Employee Found with searched id or name")
