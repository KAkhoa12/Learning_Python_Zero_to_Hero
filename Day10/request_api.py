import requests

path = "https://jsonplaceholder.typicode.com/todos/1"

def request_api(path):
    response = requests.get(path)
    return response.json()

data = request_api(path)

print(data)  # In ra "{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}"
