countries = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

for k, v in countries.items():
    print("The capital of", k, "is", v)
print(countries["Germany"])
countries["Australia"] = "Canberra"
print(countries)
countries["USA"] = "New Washington"
print(countries)
del countries["France"]
print(countries)