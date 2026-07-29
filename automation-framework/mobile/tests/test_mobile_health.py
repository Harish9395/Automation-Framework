import os

import pytest


@pytest.mark.mobile
@pytest.mark.smoke
def test_mobile_application_launch(mobile_driver):

    app_url = os.getenv("APP_URL")

    if not app_url:
        raise Exception("APP_URL environment variable is missing")

    mobile_driver.get(
        f"{app_url.rstrip('/')}/mobile"
    )

    assert mobile_driver.session_id is not None

    assert "ECS Task Mobile App" in mobile_driver.page_source
