import os

from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_mobile_driver():
    username = os.environ["SAUCE_USERNAME"]
    access_key = os.environ["SAUCE_ACCESS_KEY"]

    options = UiAutomator2Options()

    # W3C capabilities
    options.set_capability("platformName", "Android")
    options.set_capability("browserName", "Chrome")

    # Appium capabilities
    options.set_capability("appium:automationName", "UiAutomator2")
    options.set_capability(
        "appium:deviceName",
        os.getenv("DEVICE_NAME", "Samsung Galaxy S23")
    )

    # Optional, but recommended
    platform_version = os.getenv("PLATFORM_VERSION")
    if platform_version:
        options.set_capability(
            "appium:platformVersion",
            platform_version
        )

    # Sauce Labs capabilities
    options.set_capability(
        "sauce:options",
        {
            "username": username,
            "accessKey": access_key,
            "name": os.getenv("TEST_NAME", "ECS Mobile Smoke Test"),
            "build": os.getenv("BUILD_NAME", "ECS-Mobile"),
            "recordVideo": True,
            "capturePerformance": True,
            "tags": [
                "mobile",
                "web",
                os.getenv("TEST_TYPE", "Smoke"),
            ],
        },
    )

    return webdriver.Remote(
        command_executor="https://ondemand.eu-central-1.saucelabs.com/wd/hub",
        options=options,
    )
