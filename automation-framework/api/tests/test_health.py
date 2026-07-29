import os
import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_application_health(api_client):

    app_url = os.getenv("APP_URL")

    response = api_client.get(
        f"{app_url}api/health"
    )

    assert response.status_code == 200
