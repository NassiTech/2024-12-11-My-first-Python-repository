import requests

user_input = input("Enter your city? ")
response = requests.get("http://wttr.in/" + user_input + "?format=j1")
data = response.json()
print(data)

temperature = data["current_condition"][0]["temp_C"]
feelslike_temperature = data["current_condition"][0]["FeelsLikeC"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
location = data["nearest_area"][0]["areaName"][0]["value"]
# [0] means we only want to get the first object of the list
# print(weather)

print(
    f"the weather in {location} is {weather} with {temperature} in °C and feels like {feelslike_temperature} in °C"
)
