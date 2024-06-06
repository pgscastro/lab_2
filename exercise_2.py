inventory = {
    "apple": (50, 0.5),
    "banana": (100, 0.2),
    "orange": (75, 0.3),
    "pear": (20, 0.4)
}
inventory_value = 0
for k, v in inventory.items():
    inventory_value += v[1]*v[0]
print(inventory_value)

inventory["mango"] = (30, 0.6)
inventory["banana"] = (120, 0.6)
del inventory["pear"]

print(inventory)