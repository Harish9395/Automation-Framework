import os

from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_mobile_driver():

    username = os.getenv("SAUCE_USERNAME")
    access_key = os.getenv("SAUCE_ACCESS_KEY")
    app = os.getenv("SAUCE_APP")

    if not username:
        raise Exception("SAUCE_USERNAME is missing")

    if not access_key:
        raise Exception("SAUCE_ACCESS_KEY is missing")

    if not app:
        raise Exception("SAUCE_APP is missing")


    options = UiAutomator2Options()


    options.set_capability(
        "platformName",
        "Android"
    )

    options.set_capability(
        "appium:automationName",
        "UiAutomator2"
    )

    options.set_capability(
        "appium:deviceName",
        "Samsung Galaxy S23"
    )

    options.set_capability(
        "appium:app",
        app
    )


    options.set_capability(
        "sauce:options",
        {
            "username": username,
            "accessKey": access_key,

            "name": os.getenv(
                "TEST_NAME",
                "ECS Mobile Test"
            ),

            "build": os.getenv(
                "BUILD_NAME",
                "ECS Mobile Build"
            ),

            "buildId": os.getenv(
                "BUILD_ID",
                ""
            ),

            "recordVideo": True,

            "capturePerformance": True,

            "tags": [
                "mobile",
                os.getenv(
                    "TEST_TYPE",
                    "Smoke"
                )
            ]
        }
    )


    driver = webdriver.Remote(

        command_executor=
        "https://ondemand.eu-central-1.saucelabs.com/wd/hub",

        options=options
    )


    return driver
