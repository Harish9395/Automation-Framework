import requests
import os


class APIClient:

    def __init__(self):

        self.base_url = os.getenv(
            "APP_URL"
        )


    def get(self, endpoint):

        response = requests.get(
            self.base_url + endpoint,
            timeout=10
        )

        return response


    def post(self, endpoint, payload):

        response = requests.post(
            self.base_url + endpoint,
            json=payload,
            timeout=10
        )

        return response
