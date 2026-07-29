import os
import requests


def test_application_health():

    app_url = os.getenv("APP_URL")

    response = requests.get(
        app_url,
        timeout=10
    )

    assert response.status_code == 200
