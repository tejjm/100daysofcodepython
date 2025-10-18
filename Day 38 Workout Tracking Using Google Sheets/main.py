import requests
import os
from datetime import datetime
DATE = datetime.today().date().strftime("%Y-%m-%d")
TIME = datetime.today().time().strftime("%H:%M:%S")
API_ID = os.getenv("N_API_ID").strip() if os.getenv("N_API_ID") else None
API_KEY = os.getenv("N_API_KEY").strip() if os.getenv("N_API_KEY") else None
BEARER_AUTH = os.getenv("BEARER_AUTH")
QUERY = input("Enter your excercise details:\n")
GENDER = input("Enter your gender\n")
WEIGHT = float(input("Enter your weight in KG:\n"))
HEIGHT = float(input("Enter your height in CM:\n"))
AGE = int(input("Enter your age:\n"))
sheety_endpoint = "https://api.sheety.co/f332308f593d58afb67838a2cba10df6/workoutsTracker/workouts"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
Headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}
json_input = {
    "query":QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint,headers=Headers,json=json_input)
response.raise_for_status()
data = response.json()
sheety_header = {"Authorization": f"Bearer {BEARER_AUTH}"}
for n in range(0,len(data["exercises"])):

    json_data ={"workout": {
        "date":DATE,
        "time": TIME,
        "exercise": data["exercises"][n]["name"],
        "duration" : data["exercises"][n]["duration_min"],
        "calories" : data["exercises"][n]["nf_calories"]}
    }
    sheety_response = requests.post(url=sheety_endpoint,json=json_data,headers=sheety_header)
    print(sheety_response.status_code)
    print(sheety_response.text)
    sheety_response.raise_for_status()

