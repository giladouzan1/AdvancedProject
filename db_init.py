import requests

url = 'http://127.0.0.1:3000/users/2'
# data = {"user_name": "Gilad"}

try:
    response = requests.delete(url)
    response.raise_for_status()  # Check for HTTP errors

    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    # Print additional information if needed, such as the server's status and logs