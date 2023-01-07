employees = []

for i in range(5):
    id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    DOB = input("Enter employee DOB (mm/dd/yyyy): ")
    salary = float(input("Enter employee salary: "))
    employee = (id, name, age, DOB, salary)
    employees.append(employee)

id, name, age, DOB, salary = employees[0]

print("ID:", id)
print("Name:", name)
print("Age:", age)
print("DOB:", DOB)
print("Salary:", salary)
