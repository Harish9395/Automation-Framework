import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_application_health(api_client):

    response = api_client.get(
        "/api/health"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "App Works"
