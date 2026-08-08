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

def add_salary():
    while True:
        try:
            salary = int(input("Enter Employee Salary: "))
            break
        except ValueError as error:
            print(f"Invalid input: {error} Please try again.")
    return salary

def enter_employee_details():
    print("--------Enter Employee Details---------")
    id   = get_valid_int("Enter Employee ID: ")
    name = get_non_empty_input("Enter Employee Name: ")
    age  = get_valid_int("Enter Employee Age: ")
    department  = get_non_empty_input("Enter Employee Department: ")
    skills  = add_skills()
    while True:
        try:
            salary   = add_salary()
            employee = Employee(id, name, age, department, salary, skills)
            break
        except ValueError as error:
            print(f"Invalid input: {error} Please try again.")
    employee = Employee(id, name, age, department, salary, skills)
    employees.append(employee)
    # employee.display_employee()
    save_employees(employees)
    print(f"{name} added.\n")


def show_all_employees():
    if not employees:
        print("No employees added yet.")
        return
    for employee in employees:
        employee.display_employee()


def update_employee_details():
    print("--------Update Employee---------")
    searched_id = get_valid_int("Enter Employee ID to update: ")
    found = False
    
    for employee in employees:
        if searched_id == employee.employee_id:
            employee.display_employee()
            found = True

            print("\nWhat would you like to update?")
            print("1. Department")
            print("2. Salary")
            print("3. Skills")
            choice = get_non_empty_input("Choice: ")

            if choice == "1":
                new_employee_department      = get_non_empty_input("Enter New Department Name: ")
                employee.employee_department = new_employee_department
                print(f"Department updated for {employee.employee_name}")
            elif choice == "2":
                while True:
                        try:
                            new_salary   = add_salary()
                            employee.salary = new_salary
                            break
                        except ValueError as error:
                            print(f"Invalid input: {error} Please try again.")
                print(f"Salary updated for {employee.employee_name}")

            elif choice == "3":
                new_skills  = add_skills()
                employee.employee_skills =  new_skills
                print(f"Skills updated for {employee.employee_name}")
            
            else:
                print("Invalid choice.\n")

            employee.display_employee()
            save_employees(employees)
            break

    if not found:       
            print("No Employee Found with searched id")


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


def delete_employee():
    print("--------Delete Employee---------")
    delete_id = get_valid_int("Enter Employee ID to Delete record: ")
    found = False
    
    for employee in employees:
        if delete_id == employee.employee_id:
            employee.display_employee()
            found = True

            confirm = get_non_empty_input("You really want to delete ths record? (y/n)")
            confirm = confirm.lower()

            if confirm == "y":
                employees.remove(employee)
                save_employees(employees)
                print("Record Deleted")
            else: 
                print(f"Deletion Cancelled!")
            break

    if not found:       
            print("No Employee Found with searched id")
