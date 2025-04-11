import requests

header = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

request_payload = {
        "id": 122,
        "title": "Shawn test2",
        "dueDate": "2025-04-10T19:34:08.635Z",
        "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=header, json=request_payload)
print(response.status_code)
print(response.json())
data = response.json()
print(data['id'])
assert response.status_code == 200, "Status code is not 200"
assert data['id'] == 122, "ID is not 122"