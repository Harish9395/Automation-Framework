import pytest
from utilities.config import load_environment
from pages.home_page import HomePage

@pytest.mark.smoke
def test_home_page(driver):

    url = load_environment()
    home = HomePage(driver)
    home.open(url)
    assert "App Works" in driver.page_source
