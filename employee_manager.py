from utils import get_valid_int, get_non_empty_input, save_employees

class Employee:
    def __init__(self, employee_id, employee_name, employee_age, employee_department, employee_salary):
        self.employee_id          = employee_id
        self.employee_name        = employee_name
        self.employee_age         = employee_age
        self.employee_department  = employee_department
        self.salary      = employee_salary

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        elif value == 0:
            raise ValueError("Salary cannot be zero.")
        else:
            self.__salary = value

    def to_dict(self):
        return {
            "employee_id"         : self.employee_id,
            "employee_name"       : self.employee_name,
            "employee_age"        : self.employee_age,
            "employee_department" : self.employee_department,
            "employee_salary"     : self.salary
        }

    @classmethod
    def from_dict(cls, data):
         return cls(
            data["employee_id"],
            data["employee_name"],
            data["employee_age"],
            data["employee_department"],
            data["employee_salary"]
        )


    def display_employee(self):
        print("--------Employee Details---------")
        print(f"id             :    {self.employee_id} ")
        print(f"Name           :    {self.employee_name} ")
        print(f"Age            :    {self.employee_age} ")
        print(f"Department     :    {self.employee_department} ")
        print(f"Salary         :    {self.salary} ")

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


