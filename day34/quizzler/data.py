import requests


parameters = {
    "amount": 10,
    "category": 20,
    "type": "boolean"
}

URL = "https://opentdb.com/api.php"

response = requests.get(URL, parameters)
response.raise_for_status()
question_data = response.json()["results"]

print(question_data)