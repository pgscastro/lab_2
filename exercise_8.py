cart = [
    {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
    {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
    {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
    {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]

for items in cart:
    print(items)

total = 0

for i in range(len(cart)):
    total += int(cart[i]["quantity"]) * float(cart[i]["price_per_unit"])
print(total)

cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})
cart[1]["quantity"] = 10
cart.pop(3)
print(cart)
