import json
import requests

SECRET_KEY = "sk_test_326a93d9c800ce11b7b164f8947bf59e98d1b3cf"

def paystack(email, amount):
    url = "https://api.paystack.co/transaction/initialize"
    data = {
        "email": email,
        "amount": int(amount * 10),
    }
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SECRET_KEY}"}
    
    response = requests.post(url, json=data, headers=header)
    data = response.json()

    auth_url = data["data"]["authorization_url"]
    reference_id = data["data"]["reference"]

    return {"authorization_url": auth_url, "reference_id": reference_id}