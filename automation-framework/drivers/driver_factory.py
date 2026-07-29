import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def get_driver():

    browser = os.environ.get(
        "BROWSER",
        "chrome"
    )


    username = os.environ["SAUCE_USERNAME"]

    access_key = os.environ["SAUCE_ACCESS_KEY"]


    sauce_url = (
        f"https://{username}:{access_key}"
        "@ondemand.us-west-1.saucelabs.com:443/wd/hub"
    )


    if browser == "chrome":

        options = Options()


    elif browser == "firefox":

        options = FirefoxOptions()


    elif browser == "edge":

        options = EdgeOptions()


    else:

        raise Exception(
            f"Unsupported browser: {browser}"
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
            "build": "Flask-ECS-Build",
            "name": f"{browser} smoke test"
        }
    )


    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=options
    )


    driver.maximize_window()


    return driver
