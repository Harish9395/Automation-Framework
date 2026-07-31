import os
from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_mobile_driver():

    options = UiAutomator2Options()

    # W3C capabilities
    options.platform_name = "Android"
    options.browser_name = "Chrome"

    # Appium 2 capabilities
    options.set_capability(
        "appium:automationName",
        "UiAutomator2"
    )

    options.set_capability(
        "appium:autoGrantPermissions",
        True
    )

    options.set_capability(
        "sauce:options",
        {
            "username": os.environ["SAUCE_USERNAME"],
            "accessKey": os.environ["SAUCE_ACCESS_KEY"],
            "name": "React Chrome Mobile Test",
            "build": "GitHub Actions"
        }
    )

    driver = webdriver.Remote(
        command_executor="https://ondemand.eu-central-1.saucelabs.com/wd/hub",
        options=options
    )

    return driver
