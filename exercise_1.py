students = {
    "Alice": [85, 78, 92],
    "Bob": [79, 74, 81],
    "Charlie": [91, 82, 85],
    "David": [76, 85, 83],
    "Eve": [88, 79, 92]
}

mean = []
for k, v in students.items():
    average = (sum(v) / len(v))
    mean.append({k: average})

print(mean)

print(max(students))
print(min(students))


students["Frank"] = [80, 90, 85]