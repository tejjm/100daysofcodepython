import requests
parameters = {
    "amount" : 10,
    "type" : "boolean",
    "category" : 31,
}
end_point = "https://opentdb.com/api.php?"
response = requests.get(end_point,params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
