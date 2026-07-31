import os
from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_mobile_driver():

    options = UiAutomator2Options()

    options.set_capability("platformName", "Android")
    options.set_capability("browserName", "Chrome")

    options.set_capability(
        "appium:automationName",
        "UiAutomator2"
    )

    options.set_capability(
        "sauce:options",
        {
            "username": os.environ["SAUCE_USERNAME"],
            "accessKey": os.environ["SAUCE_ACCESS_KEY"],
            "name": "React Mobile Chrome Test",
            "build": "GitHub Actions"
        }
    )

    return webdriver.Remote(
        command_executor="https://ondemand.eu-central-1.saucelabs.com/wd/hub",
        options=options
    )
