import requests


# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={'title': "Manchester United", "content": "Glory Glory", "price": 200})
print(get_response.text)

print(get_response.json())