import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():

    username = os.environ["SAUCE_USERNAME"]
    access_key = os.environ["SAUCE_ACCESS_KEY"]


    sauce_url = (
        f"https://{username}:{access_key}"
        "@ondemand.us-west-1.saucelabs.com:443/wd/hub"
    )


    options = Options()

    options.set_capability(
        "browserName",
        "chrome"
    )

    options.set_capability(
        "browserVersion",
        "latest"
    )

    options.set_capability(
        "platformName",
        "Windows 11"
    )


    options.set_capability(
        "sauce:options",
        {
            "name": "Flask ECS Test",
            "build": "GitHub Actions"
        }
    )


    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=options
    )

    return driver
