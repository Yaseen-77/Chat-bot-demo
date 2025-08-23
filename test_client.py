import requests

url = "http://127.0.0.1:5000/ask"
payload = {"query": "How long does it take to get my Aadhaar letter after enrollment?"}


response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
