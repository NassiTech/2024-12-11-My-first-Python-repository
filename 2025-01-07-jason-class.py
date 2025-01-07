import requests

user_input = input("Enter your city? ")
response = requests.get("http://wttr.in/" + user_input + "?format=j1")
data = response.json()


temperature = data["current_condition"][0]["temp_C"]
feelslike_temperature = data["current_condition"][0]["FeelsLikeC"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
location = data["nearest_area"][0]["areaName"][0]["value"]

# print(weather)

print(
    f"the weather in {location} is {weather} with {temperature} in °C and feels like {feelslike_temperature} in °C"
)
