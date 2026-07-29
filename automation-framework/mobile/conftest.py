import pytest

from mobile.drivers.mobile_driver import get_mobile_driver


@pytest.fixture
def mobile_driver():

    driver = get_mobile_driver()


    yield driver


    driver.quit()
