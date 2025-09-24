import requests

question_data = []

def fetch_questions():
    global question_data
    params = {
        "amount": 10,
        "type": "boolean",
    }
    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    data = response.json()["results"]
    question_data = data
    print(question_data)

fetch_questions()
