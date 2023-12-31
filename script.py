# a simple python script for adding data

import json

date = input("date: ")
minn = input("min: ")
maxx = input("max: ")
humidity = input("humidity: ")
rainfall = input("rainfall: ")

with open("data.json", "r") as data:
    data = json.load(data)

data["2024"][date] = {
    "min":minn,
    "max":maxx,
    "humidity":humidity,
    "rainfall":rainfall
}

with open("data.json", "w") as file:
    json.dump(data,file,indent=4)
