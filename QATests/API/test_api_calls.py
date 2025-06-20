import os
import json
import requests
import pytest
from QATests.tests.base_test import BaseTest
import time

class TestAPIGetCall:

    @pytest.mark.functional
    def test_get_api_call(self):
        """
        This function tests the GET API call to retrieve an activity by ID.
        It checks if the status code is 200 and prints the response.
        """
        # Define the headers for the request
        head = {
            'Accept':'text/plain'
        }

        response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/1",headers=head)
        print(response.status_code)
        print(response.json())

        assert response.status_code == 200, "Status code is not 200"

    def test_post_api_call(self):
        head = {
            'Content-Type':'application/json',
            'Authorization':'Bearer 12143133a105c96f203540fa1b2f5c61a1e15f09cfde2c34d449a9c96dbe8c32'
        }
        # Each time I run this I have to update/change the email address to avoid duplicates
        body = {
            "name": "Shawn 120",
            "email": "asitest122@gmail.com",
            "gender": "male",
            "status": "active"
        }
        url = "https://gorest.co.in/public/v2/users"
        # Make the POST request with headers and body
        response = requests.post(url, headers=head, json=body)
        print(response.status_code)
        print(response.json())
        assert response.status_code == 201, "Status code is not 201"

        getResponse = requests.get(url+"/"+str(response.json()['id']), headers=head)
        print(getResponse.json())

    def test_parameterized_api_call(self):
        url='https://gorest.co.in/public/v2/users'
        para = {
            'page': 1,
            'per_page': 3
        }
        response = requests.get(url,params=para)
        print(response.status_code)
        print(response.json())

        assert response.status_code == 200, "Status code is not 200"

    def test_post_demo(self):
        base_url = 'https://reqres.in/'
        headers_test = {
            'Content-Type':'application/json'
        }

        json_file = os.path.join(os.path.dirname(__file__), "../data/users.json")
        with open(json_file, "r", encoding="utf-8") as file:
            json_payload = json.load(file)
        # Use json=payload when passing json data
        response = requests.post(url=base_url+'api/users', headers=headers_test, json=json_payload)
        # Some people use data instead of json if they are passing csv
        # response = requests.post(url=base_url+'api/users', headers=headers_test, data=json.dumps(json_payload))
        print(response.status_code)
        print(response.text)
        # print(response.json())

        assert response.status_code == 201, "Status code is not 201"

    def test_get_reqres_demo_(self):
        header = {
            'Content-Type':'application/json'
        }
        base_url = 'https://reqres.in/'
        response = requests.get(url=str(base_url+'api/users/2'), headers=header)
        print(response.status_code)
        print(response.text)
        assert response.status_code == 200, "Status code is not 200"
