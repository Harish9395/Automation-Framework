import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():

    username = os.getenv("SAUCE_USERNAME")
    access_key = os.getenv("SAUCE_ACCESS_KEY")

    if not username:
        raise Exception("SAUCE_USERNAME is missing")

    if not access_key:
        raise Exception("SAUCE_ACCESS_KEY is missing")


    sauce_url = "https://ondemand.us-west-1.saucelabs.com/wd/hub"


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
            "username": username,
            "accessKey": access_key,
            "name": "Flask ECS Smoke Test",
            "build": "GitHub Actions"
        }
    )


    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=options
    )

    return driver
