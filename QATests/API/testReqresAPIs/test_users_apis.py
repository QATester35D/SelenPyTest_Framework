import os
import json
import requests
import pytest
from QATests.test_api_services.reqres_service import ReqresService

# This is testing the the users functionality of the training site: https://reqres.in
# The structured testing approach will test each "functionality" (major resource) like the users functionality
#   found in the swagger doc: https://reqres.in/api-docs/

# @pytest.mark.functional
class TestReqresUsersAPI:
    def setup_method(self, method):
        self.reqres_service = ReqresService()

    def test_get_user_by_id_success(self):
        response = self.reqres_service.get_user(user_id=2)
        elapsed_time = response.elapsed
        response_time_seconds = elapsed_time.total_seconds()
        assert response_time_seconds < 2, f"The API call took more than 1 second to execute; it took {response_time_seconds}"
        assert response.status_code == 200, "Status code is not 200"
        print(f"Response time: {response_time_seconds:.4f} seconds.")
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

    def test_get_users_list_success(self):
        response = self.reqres_service.get_user_list(page=1,per_page=5)
        elapsed_time = response.elapsed
        response_time_seconds = elapsed_time.total_seconds()
        assert response_time_seconds < 2, f"The API call took more than 1 second to execute; it took {response_time_seconds}"
        assert response.status_code == 200, "Status code is not 200"
        print(f"Response time: {response_time_seconds:.4f} seconds.")
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

    def test_post_create_user(self):
        response = self.reqres_service.post_create_user(name="Shawn",job="SDET")
        elapsed_time = response.elapsed
        response_time_seconds = elapsed_time.total_seconds()
        assert response_time_seconds < 2, f"The API call took more than 1 second to execute; it took {response_time_seconds}"
        assert response.status_code == 201, "Status code is not 200"
        print(f"Response time: {response_time_seconds:.4f} seconds.")
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

    def test_put(self):
        base_url = 'https://reqres.in/'
        headers_test = {
            'Content-Type':'application/json',
            'x-api-key':'reqres-free-v1'
        }

        json_file = os.path.join(os.path.dirname(__file__), "../data/users.json")
        with open(json_file, "r", encoding="utf-8") as file:
            json_payload = json.load(file)
        # Use json=payload when passing json data
        # response = requests.post(url=base_url+'api/users', headers=headers_test, json=json_payload)
        # Some people use data instead of json if they are passing csv
        response = requests.post(url=base_url+'api/users', headers=headers_test, data=json.dumps(json_payload))
        elapsed_time=response.elapsed
        response_time_seconds = elapsed_time.total_seconds()
        assert response_time_seconds < 1, f"The API call took more than 1 second to execute; it took {response_time_seconds}"
        print(f"Response time: {response_time_seconds:.4f} seconds.")
        print(response.status_code)
        print(response.text)
        # print(response.json())
        assert response.status_code == 201, "Status code is not 201"

##### Helpers
    def increment_get_address_name_counter():
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "addressNameCounter.txt"))
        file = open(filename, 'r+')
        ctr = file.read().strip()
        new_ctr = int(ctr) + 1
        file.seek(0)
        file.write(str(new_ctr))
        file.close()
        return ctr
    
    def create_email_with_counter(nameCounter):
        #asitest124@gmail.com
        email='asitest'+nameCounter+'@gmail.com'
        return email