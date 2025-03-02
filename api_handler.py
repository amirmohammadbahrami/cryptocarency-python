import requests
from constants import CRYPTO_API


class APIRequest:
    def __init__(self, api: str):
        self.api = api
        self.status_code = None
        self.content = None

    def get_req(self):
        response = requests.get(self.api)
        self.status_code = response.status_code
        self.content = response.json()

cryptocurrency_api = APIRequest(CRYPTO_API)

