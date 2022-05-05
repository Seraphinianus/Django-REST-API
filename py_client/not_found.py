import requests

endpoint = "http://localhost:8000/api/products/198132919184/"

get_response = requests.get(endpoint)

print(get_response.json())