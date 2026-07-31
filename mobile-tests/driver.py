import os

from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_mobile_driver():

    options = UiAutomator2Options()

    # W3C capabilities
    options.set_capability(
        "platformName",
        "Android"
    )

    options.set_capability(
        "browserName",
        "Chrome"
    )

    # Appium
    options.set_capability(
        "appium:automationName",
        "UiAutomator2"
    )

    options.set_capability(
        "appium:deviceName",
        "Samsung Galaxy S23 FE"
    )

    options.set_capability(
        "appium:platformVersion",
        "14"
    )

    options.set_capability(
        "appium:newCommandTimeout",
        300
    )


    # Sauce Labs
    options.set_capability(
        "sauce:options",
        {
            "username": os.environ["SAUCE_USERNAME"],
            "accessKey": os.environ["SAUCE_ACCESS_KEY"],
            "name": "React Mobile Chrome Smoke Test",
            "build": "React-Web-Mobile",
            "tags": [
                "mobile",
                "chrome",
                "smoke"
            ]
        }
    )


    driver = webdriver.Remote(
        command_executor=
        "https://ondemand.eu-central-1.saucelabs.com/wd/hub",
        options=options
    )


    return driver
