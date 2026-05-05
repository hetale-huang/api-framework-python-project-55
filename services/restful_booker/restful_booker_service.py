import json

from services.base_service import BaseClient
from config import BASE_URI
from utils.request import APIRequest


class RestfulBookerClient(BaseClient):
    def __init__(self):
        super().__init__()#BaseClient.__init__(self)相当于这一句
        #子类一旦自己写了init就不会执行父类的init，所以要加上super，带上父类的初始化
        self.base_url = BASE_URI
        self.request = APIRequest()

    def create_booking(self, payload):
        return self.request.post_request(
            self.base_url, json.dumps(payload), self.headers
        )

    def get_booking(self, booking_id):
        url = f"{BASE_URI}/{booking_id}"
        return self.request.get_request(url, self.headers)

    def update_booking(self, booking_id, payload):
        url = f"{BASE_URI}/{booking_id}"
        return self.request.put_request(
            url, json.dumps(payload), self.headers_with_basic_auth
        )

    def delete_booking(self, booking_id):
        url = f"{BASE_URI}/{booking_id}"
        return self.request.delete_request(url, self.headers_with_basic_auth)
