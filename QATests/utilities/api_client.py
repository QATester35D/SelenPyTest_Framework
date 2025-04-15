import requests

class APIClient:
    # BASE_URL="https://reqres.in/api/"
    BASE_URL="https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get(self, endpoint, params=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        return response

    def post(self, endpoint, data=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def put(self, endpoint, data=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, headers=self.headers, json=data)
        return response

    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, headers=self.headers)
        return response 