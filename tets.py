import requests

base_url = "http://127.0.0.1:5000/users/"

# POST - Create User
response = requests.post(base_url + "1", json={"user_name": "Gilad"})
try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("Non-JSON response:", response.text)
