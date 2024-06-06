cities = {
    "New York": 8419000,
    "Los Angeles": 3980000,
    "Chicago": 2716000,
    "Houston": 2328000,
    "Phoenix": 1690000
}

for k, v in cities.items():
    print(f"The population of {k} is {v}")

print("the city with highest population is " + max(cities, key=cities.get))
print("the city with lowest population is " + min(cities, key=cities.get))

cities["Phoenix"] = 170000
print(cities)
cities["San Francisco"] = 884000
print(cities)
