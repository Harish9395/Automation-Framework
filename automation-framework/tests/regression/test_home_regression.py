import pytest

from utilities.config import load_environment
from pages.home_page import HomePage


@pytest.mark.regression
def test_application_load(driver):

    url = load_environment()

    home = HomePage(driver)

    home.open(url)


    assert driver.title is not None


@pytest.mark.regression
def test_application_response(driver):

    url = load_environment()

    driver.get(url)

    assert "App Works" in driver.page_source
