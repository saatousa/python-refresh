employee = {
    "name": "Jessica",
    "age": 32,
    "role": "Data Analyst"
}

print(employee['role'])

employee['salary'] = 5000
print(employee)


employee['age'] = 31
print(employee)

del employee["salary"]
print(employee)


for key, value in employee.items():
    print(key)
    print(value)


employees = [
    {"name": "Sara", "salary": 50000},
    {"name": "John", "salary": 60000},
    {"name": "Emma", "salary": 55000}
]

# for employee in employees:
#     print(employee["name"])
#     print(employee["salary"])

def calculate_salary(employees):
    total_salary = 0
    for employee in employees:
        total_salary += employee["salary"]

    return total_salary

print(calculate_salary(employees))


def avg_salary(employees):
    total_employees = len(employees)
    salary_sum = 0 
    for employee in employees:
        salary_sum += employee["salary"]
    
    avg = salary_sum / total_employees
    return avg

print(avg_salary(employees))
