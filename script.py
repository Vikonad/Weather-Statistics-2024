# a simple python script for adding new data

import json

date = input("date: ")
minn = input("min: ")
maxx = input("max: ")
sunrise = input("sunrise: ")
sunset = input("sunset: ")
moonrise = input("moonrise: ")
moonset = input("moonset: ")

with open("data.json", "r") as data:
    data = json.load(data)

data["2024"][date] = {
    "min":minn,
    "max":maxx,
    "sunrise":sunrise,
    "sunset":sunset,
    "moonrise":moonrise,
    "moonset":moonset
}

with open("data.json", "w") as file:
    json.dump(data,file,indent=4)
