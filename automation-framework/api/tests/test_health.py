import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_application_health(api_client):

    response = api_client.get(
        "/health"
    )

    assert response.status_code == 200
