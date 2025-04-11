import requests

head = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

putPayLoad = {
  "id": 121,
  "title": "shawn test123_v2",
  "dueDate": "2025-04-10T21:24:19.546Z",
  "completed": True
}

response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/121", headers=head, json=putPayLoad)
print(response.status_code)
print(response.json())
