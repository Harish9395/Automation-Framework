from utilities.config import load_environment
from pages.home_page import HomePage

def test_home_page(driver):
    url = load_environment()
    print("Application URL:", url)
    home = HomePage(driver)
    home.open(url)
