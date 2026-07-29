import os

from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_mobile_driver():

    username = os.getenv(
        "SAUCE_USERNAME"
    )

    access_key = os.getenv(
        "SAUCE_ACCESS_KEY"
    )


    if not username:
        raise Exception(
            "SAUCE_USERNAME missing"
        )


    if not access_key:
        raise Exception(
            "SAUCE_ACCESS_KEY missing"
        )


    options = UiAutomator2Options()


    options.platform_name = "Android"

    options.device_name = "Samsung Galaxy S23"

    options.automation_name = "UiAutomator2"


    # Sauce Labs application
    options.app = os.getenv(
        "SAUCE_APP"
    )


    options.set_capability(
        "sauce:options",
        {
            "username": username,
            "accessKey": access_key,
            "name": "ECS Mobile Test",
            "build": os.getenv(
                "BUILD_NAME",
                "ECS-Mobile"
            ),
            "recordVideo": True,
            "capturePerformance": True
        }
    )


    driver = webdriver.Remote(

        "https://ondemand.eu-central-1.saucelabs.com/wd/hub",

        options=options
    )


    return driver
