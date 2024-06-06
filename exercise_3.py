employees = [
    ("John Doe", "Accounting", "john.doe@example.com"),
    ("Jane Smith", "Marketing", "jane.smith@example.com"),
    ("Emily Davis", "HR", "emily.davis@example.com"),
    ("Michael Brown", "IT", "michael.brown@example.com")
]

for i in range(len(employees)):
    print(f"Name: {employees[i][0]}, Department: {employees[i][1]}")

employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
# print(employees)
# employee_list = list(employees)
# print(employee_list)
# name_list = []
# for i in range(len(employees)):
#     name_list.append((employees[i][0]).split(' '))

# surname = []
# for i in range(len(name_list)):
#   surname.append(name_list[i][::-1])
#     surname[i] = surname[i][0] + " " + surname[i][1]
#     employee_list[i][0] = surname[i]
# print(type(employee_list))
# print(len(name_list), surname)
# print(employee_list[3][0])


def get_surname(employee):
    name_parts = employee[0].split(' ')
    return name_parts[1]


sorted_employees = sorted(employees, key=get_surname)

print("The list of employees emails organized by surname in ascending order is: ")
for employee in sorted_employees:
    print(f"{get_surname(employee)}, Email: {employee[2]}")

for i in range(len(employees)):
    if employees[i][0] == "Jane Smith":
        print(f"The Department of Jane Smith is : {employees[i][1]}")