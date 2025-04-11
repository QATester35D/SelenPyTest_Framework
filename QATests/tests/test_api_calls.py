import requests
import pytest
from QATests.tests.base_test import BaseTest

class APIGetCall(BaseTest):

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




# This works:
# head = {
#     'Accept':'text/plain'
# }

# response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/30",headers=head)
# print(response.status_code)
# print(response.json())

# assert response.status_code == 200, "Status code is not 200"

head = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

putPayLoad = {
  "id": 30,
  "title": "shawn test123_v2",
  "dueDate": "2025-04-10T21:24:19.546Z",
  "completed": True
}

response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/30", headers=head, json=putPayLoad)
print(response.status_code)
print(response.json())