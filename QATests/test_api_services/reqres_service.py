import requests
from QATests.utilities.reqresApiConfig import BASE_URL, HEADERS

class ReqresService:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = HEADERS

    def get_user(self, user_id):
        endpoint = f'/api/users/{user_id}'
        url = self.base_url + endpoint
        return requests.get(url=url, headers=self.headers)

    def get_user_list(self, page, per_page):
        endpoint = f'/api/users?{page},{per_page}'
        url = self.base_url + endpoint
        return requests.get(url=url, headers=self.headers)
    
    def post_create_user(self,name,job):
        endpoint = f'/api/users?{name},{job}'
        url = self.base_url + endpoint
        return requests.post(url=url, headers=self.headers)
    
    def put_update_user(self,id,name,job):
        endpoint = f'/api/users/{id}?{name},{job}'
        url = self.base_url + endpoint
        return requests.put(url=url, headers=self.headers)
    
    def delete_user(self,id):
        endpoint = f'/api/users/{id}'
        url = self.base_url + endpoint
        return requests.delete(url=url, headers=self.headers)