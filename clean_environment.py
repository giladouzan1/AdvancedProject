import requests

try:
    response = requests.get('http://127.0.0.1:5000/stop_server')
    response.raise_for_status()  # Raise an exception for non-200 status codes
except requests.exceptions.RequestException as e:
    print(f"Error stopping server at 127.0.0.1:5000: {e}")

try:
    response = requests.get('http://127.0.0.1:5001/stop_server')
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error stopping server at 127.0.0.1:5001: {e}")