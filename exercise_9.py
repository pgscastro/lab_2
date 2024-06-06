weather = {
    "Monday": {"temperature": 20, "humidity": 60},
    "Tuesday": {"temperature": 22, "humidity": 55},
    "Wednesday": {"temperature": 19, "humidity": 65},
    "Thursday": {"temperature": 23, "humidity": 50},
    "Friday": {"temperature": 21, "humidity": 70}
}
for k, v in weather.items():
    print(k, "will have the temperature of:", v["temperature"], "and the humidity of:", v["humidity"])

max_temp = max(int(temp["temperature"]) for temp in weather.values())
max_temp_day = [k for k, v in weather.items() if v["temperature"] == max_temp]
print("The day with the maximum temperature is:", max_temp_day[0])

min_humidity = min(int(hum["humidity"]) for hum in weather.values())
min_humidity_day = [k for k, v in weather.items() if v["humidity"] == min_humidity]
print("The day with the minimum humidity is:", min_humidity_day[0])

weather["Wednesday"]["temperature"] = 25
weather["Saturday"]= {"temperature": 23, "humidity": 60}

print(weather)