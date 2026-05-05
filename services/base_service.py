import os
import json
from base64 import b64encode
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class BaseClient:
    def __init__(self):
        self.base_url = "https://restful-booker.herokuapp.com"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.token = None  # 保存 auth token

    def set_token(self, token: str):
        self.token = token

    def get_headers(self):
        headers = self.headers.copy()
        if self.token:
            headers["Cookie"] = f"token={self.token}"
        return headers

    # ✅ 正确位置：在类里，和其他方法同级缩进，不在 get_headers 里面
    @property
    def headers_with_basic_auth(self):
        # restful-booker 默认 admin / password123
        username = "admin"
        password = "password123"
        token = b64encode(f"{username}:{password}".encode()).decode()
        return {**self.headers, "Authorization": f"Basic {token}"}