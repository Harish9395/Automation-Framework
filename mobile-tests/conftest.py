import pytest

from drivers.mobile_driver import get_mobile_driver


@pytest.fixture(scope="function")
def mobile_driver():

    driver = get_mobile_driver()

    yield driver

    driver.quit()
