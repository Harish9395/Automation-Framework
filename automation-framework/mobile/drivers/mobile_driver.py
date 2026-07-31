import os

from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_mobile_driver():
    username = os.environ["SAUCE_USERNAME"]
    access_key = os.environ["SAUCE_ACCESS_KEY"]

    options = UiAutomator2Options()

    # W3C Capabilities
    options.set_capability("platformName", "Android")
    options.set_capability("browserName", "Chrome")

    # Appium Capabilities
    options.set_capability("appium:automationName", "UiAutomator2")
    options.set_capability(
        "appium:deviceName",
        os.getenv("DEVICE_NAME", "Samsung Galaxy S23 FE")
    )
    options.set_capability(
        "appium:platformVersion",
        os.getenv("PLATFORM_VERSION", "14")
    )

    # Sauce Labs Capabilities
    options.set_capability(
        "sauce:options",
        {
            "username": username,
            "accessKey": access_key,
            "name": os.getenv("TEST_NAME", "ECS Mobile Smoke Test"),
            "build": os.getenv("BUILD_NAME", "ECS-Mobile"),
            "buildId": os.getenv("BUILD_ID", ""),
            "recordVideo": True,
            "capturePerformance": True,
            "tags": [
                "mobile",
                "web",
                os.getenv("TEST_TYPE", "Smoke"),
            ],
        },
    )

    driver = webdriver.Remote(
        command_executor="https://ondemand.eu-central-1.saucelabs.com/wd/hub",
        options=options,
    )

    return driver
