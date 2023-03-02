employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter number of hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

gross_salary = hours_worked * hourly_rate


print(f"Employee name: {employee_name}")
print(f"Gross salary: {gross_salary:.2f}")
