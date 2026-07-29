import pytest


@pytest.mark.mobile
@pytest.mark.smoke
def test_mobile_application_launch(
    mobile_driver
):

    assert mobile_driver.session_id is not None
