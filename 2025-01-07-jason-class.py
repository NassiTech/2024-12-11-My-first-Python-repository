import requests
user_input = input("Enter your city" )
response = requests.get("http://wttr.in/berlin?format = j1")
data = response.json()
temperature = data["current_conditions"][0]["temp_C"]
feelslike_temoerature = data["current_conditions"][0]["feelslike_temp_C"]
weather = data["current_conditions"][0]["weatherDesc"][0]["value"]
location = data["nearest_area"][0]["area_name"][0]["value"]
print(weather)
print(f"the weather in berlin is {weather} witrn {temperature} in °C" feels like {feels_like_temp_C} in °C )
