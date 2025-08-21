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

    def test_get_user_by_id_success(self, assert_helper):
        expected_response_time=2
        expected_response_code=200
        userId=2
        response = self.reqres_service.get_user(user_id=userId)
        elapsed_time = response.elapsed
        response_time_seconds = elapsed_time.total_seconds()
        self.assert_api_execution_time(response_time_seconds,expected_response_time,f"Executing the GET on 'get a specific user {userId}'. The execution time was {response_time_seconds}. Expected the execution time to be less than: {expected_response_time}", assert_helper)
        self.assert_api_status_code(response.status_code,expected_response_code,f"Executing the GET on 'get a specific user {userId}'. The status code was {response.status_code}. Expected: {expected_response_code}", assert_helper)
        print(f"Response time: {response_time_seconds:.4f} seconds.")
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

    def test_get_users_list_success(self, assert_helper):
        expected_response_time=2
        expected_response_code=200
        response = self.reqres_service.get_user_list(page=1,per_page=5)
        elapsed_time = response.elapsed
        response_time_seconds = elapsed_time.total_seconds()
        self.assert_api_execution_time(response_time_seconds,expected_response_time,f"Executing the GET on 'get all users'. The execution time was {response_time_seconds}. Expected the execution time to be less than: {expected_response_time}", assert_helper)
        self.assert_api_status_code(response.status_code,expected_response_code,f"Executing the GET on 'get all users'. The status code was {response.status_code}. Expected: {expected_response_code}", assert_helper)
        print(f"Response time: {response_time_seconds:.4f} seconds.")
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

    def test_post_create_user(self, assert_helper):
        expected_response_time=2
        expected_response_code=201
        response = self.reqres_service.post_create_user(name="Shawn",job="SDET")
        elapsed_time = response.elapsed
        response_time_seconds = elapsed_time.total_seconds()
        self.assert_api_execution_time(response_time_seconds,expected_response_time,f"Executing the POST on 'creating a user'. The execution time was {response_time_seconds}. Expected the execution time to be less than: {expected_response_time}", assert_helper)
        self.assert_api_status_code(response.status_code,expected_response_code,f"Executing the POST on 'creating a user'. The status code was {response.status_code}. Expected: {expected_response_code}", assert_helper)
        print(f"Response time: {response_time_seconds:.4f} seconds.")
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

    def test_put_update_user(self, assert_helper):
        expected_response_time=1
        expected_response_code=200
        response = self.reqres_service.put_update_user(id=2,name="Joe",job="Tester")
        elapsed_time = response.elapsed
        response_time_seconds = elapsed_time.total_seconds()
        self.assert_api_execution_time(response_time_seconds,expected_response_time,f"Executing the PUT on 'updating a user'. The execution time was {response_time_seconds}. Expected the execution time to be less than: {expected_response_time}", assert_helper)
        self.assert_api_status_code(response.status_code,expected_response_code,f"Executing the PUT on 'updating a user'. The status code was {response.status_code}. Expected: {expected_response_code}", assert_helper)
        print(f"Response time: {response_time_seconds:.4f} seconds.")
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

    def test_delete_user(self, assert_helper):
        expected_response_time=1
        expected_response_code=204
        response = self.reqres_service.delete_user(id=2)
        elapsed_time = response.elapsed
        response_time_seconds = elapsed_time.total_seconds()
        self.assert_api_execution_time(response_time_seconds,expected_response_time,f"Executing the DELETE on a 'user'. The execution time was {response_time_seconds}. Expected the execution time to be less than: {expected_response_time}", assert_helper)
        self.assert_api_status_code(response.status_code,expected_response_code,f"Executing the PUT on 'create user'. The status code was {response.status_code}. Expected: {expected_response_code}", assert_helper)
        print(f"Response time: {response_time_seconds:.4f} seconds.")
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

    def assert_api_status_code(self, actual_status_code, expected_status_code, message, assert_helper):
        assert_helper.equal(
            actual=actual_status_code,
            expected=expected_status_code,
            requirement_id="REQ-101.1",
            description=message
        )

    def assert_api_execution_time(self, actual_execution_time, expected_execution_time, message, assert_helper):
        assert_helper.lessThanOrEqual(
            actual=actual_execution_time,
            expected=expected_execution_time,
            requirement_id="REQ-101.1",
            description=message
        )