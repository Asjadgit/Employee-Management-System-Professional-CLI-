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
        else:
            self.__salary = value


    def display_employee(self):
        print("--------Employee Details---------")
        print(f"id             :    {self.employee_id} ")
        print(f"Name           :    {self.employee_name} ")
        print(f"Age            :    {self.employee_age} ")
        print(f"Department     :    {self.employee_department} ")
        print(f"Salary         :    {self.salary} ")


def enter_employee_details():
    print("--------Enter Employee Details---------")
    id   = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age  = int(input("Enter Employee Age: "))
    department  = input("Enter Employee Department: ")
    while True:
        try:
            salary      = int(input("Enter Employee Salary: "))
            employee = Employee(id, name, age, department, salary)
            break
        except ValueError as error:
            print(f"Invalid input: {error} Please try again.")
    # students.append(student)
    # save_student(student)
    print(f"{name} added.\n")
    employee.display_employee()

enter_employee_details()