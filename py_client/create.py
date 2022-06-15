import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'Homepage',
    'price': 45.89
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
