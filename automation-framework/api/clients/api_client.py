import os
import requests


class APIClient:

    def __init__(self):

        self.base_url = os.getenv("APP_URL")

        if not self.base_url:
            raise Exception("APP_URL environment variable is missing")

        self.session = requests.Session()

        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        )


    def get(self, endpoint, params=None):

        url = self.base_url + endpoint

        response = self.session.get(
            url,
            params=params,
            timeout=10
        )

        return response


    def post(self, endpoint, payload=None):

        url = self.base_url + endpoint

        response = self.session.post(
            url,
            json=payload,
            timeout=10
        )

        return response


    def put(self, endpoint, payload=None):

        url = self.base_url + endpoint

        response = self.session.put(
            url,
            json=payload,
            timeout=10
        )

        return response


    def patch(self, endpoint, payload=None):

        url = self.base_url + endpoint

        response = self.session.patch(
            url,
            json=payload,
            timeout=10
        )

        return response


    def delete(self, endpoint):

        url = self.base_url + endpoint

        response = self.session.delete(
            url,
            timeout=10
        )

        return response


    def close(self):

        self.session.close()
