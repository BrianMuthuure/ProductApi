import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    'title': "Hello folk",
    'price': 140
}
get_response = requests.put(endpoint, json=data)

print(get_response.json())