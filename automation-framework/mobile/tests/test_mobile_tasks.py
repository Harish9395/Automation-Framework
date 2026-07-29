import pytest


@pytest.mark.mobile
def test_open_mobile_app(
    mobile_driver
):

    title = mobile_driver.find_element(
        "accessibility id",
        "appTitle"
    )


    assert title.is_displayed()
