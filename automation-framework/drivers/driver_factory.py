import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def get_driver():
    username = os.getenv("SAUCE_USERNAME")
    access_key = os.getenv("SAUCE_ACCESS_KEY")

    if not username:
        raise Exception("SAUCE_USERNAME is missing")

    if not access_key:
        raise Exception("SAUCE_ACCESS_KEY is missing")

    browser = os.getenv("BROWSER", "chrome").lower()

    sauce_url = "https://ondemand.eu-central-1.saucelabs.com/wd/hub"

    if browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()
    else:
        options = Options()

    options.set_capability("browserName", browser)
    options.set_capability("browserVersion", "latest")
    options.set_capability("platformName", "Windows 11")

    sauce_options = {
        "username": username,
        "accessKey": access_key,
        "name": os.getenv("TEST_NAME", "ECS Automation"),
        "build": os.getenv("BUILD_NAME", "GitHub Actions"),
        "buildId": os.getenv("BUILD_ID", ""),
        "tags": [
            os.getenv("GIT_BRANCH", ""),
            "GitHub Actions"
        ]
    }

    options.set_capability("sauce:options", sauce_options)

    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=options
    )

    driver.maximize_window()

    return driver
