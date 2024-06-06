members = [
    {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
    {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
    {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
    {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
]

for i in range(len(members)):
    print("Member:", members[i]["name"], members[i]["age"], "years old")

for i in range(len(members)):
    if members[i]["name"] == "Charlie":
        print("The book borrowed by charlie is:", members[i]["books_borrowed"])
members.append({"name": "Eve", "age": 28, "books_borrowed": "Pride and Prejudice"})

for i in range(len(members)):
    if members[i]["name"] == "Bob":
        members[i]["age"] = 31

for i in range(len(members)):
    if members[i]["name"] == "David":
        members.pop(i)
        break

print(members)
