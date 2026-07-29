import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():

    username = os.environ.get("SAUCE_USERNAME")
    access_key = os.environ.get("SAUCE_ACCESS_KEY")


    if not username or not access_key:
        raise Exception(
            "Sauce Labs credentials are missing"
        )


    sauce_url = (
        "https://"
        + username
        + ":"
        + access_key
        + "@ondemand.us-west-1.saucelabs.com:443/wd/hub"
    )


    options = Options()


    options.set_capability(
        "browserName",
        "chrome"
    )

    options.set_capability(
        "platformName",
        "Windows 11"
    )

    options.set_capability(
        "browserVersion",
        "latest"
    )


    options.set_capability(
        "sauce:options",
        {
            "name": "Flask ECS Smoke Test",
            "build": "GitHub Actions Build"
        }
    )


    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=options
    )


    return driver
