import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import requests
import pytest
from QATests.tests.base_test import BaseTest

class TestAPIGetCall(BaseTest):

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

