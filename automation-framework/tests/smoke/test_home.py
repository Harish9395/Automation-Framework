from config.config import load_environment
from pages.home_page import HomePage

def test_home_page(driver):

    home = HomePage(driver)

    home.open(load_environment())

    assert "App Works" in home.get_page_source()
