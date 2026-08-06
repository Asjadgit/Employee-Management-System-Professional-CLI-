from employee_manager import enter_employee_details

def main():
    employees = []

    while True:
        employee = enter_employee_details()
        employees.append(employee)

        again = input("Add another employee? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\n--------All Employees---------")
    for e in employees:
        e.display_employee()

