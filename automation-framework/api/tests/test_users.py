import pytest


@pytest.mark.api
@pytest.mark.regression
def test_users_endpoint(api_client):

    response = api_client.get(
        "/users"
    )

    assert response.status_code == 200
    data = response.json()
    assert isinstance(
        data,
        list
    )
