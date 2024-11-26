import requests

url = "https://worrying-nonie-teja-9052d7b4.koyeb.app/bot_chat"
payload = {"message": "hi"}

try:
    response = requests.post(url, json=payload, timeout=50)
    response.raise_for_status()
    print("Response JSON:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
