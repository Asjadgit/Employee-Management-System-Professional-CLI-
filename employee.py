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