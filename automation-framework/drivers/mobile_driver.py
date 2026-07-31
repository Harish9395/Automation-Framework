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


    # Dynamic configuration from GitHub Actions
    browser = os.getenv(
        "BROWSER",
        "chrome"
    ).lower()

    browser_version = os.getenv(
        "BROWSER_VERSION",
        "latest"
    )

    platform = os.getenv(
        "PLATFORM",
        "Windows 11"
    )


    sauce_url = (
        "https://ondemand.eu-central-1.saucelabs.com/wd/hub"
    )


    # Browser options
    if browser == "firefox":

        options = FirefoxOptions()

    elif browser == "edge":

        options = EdgeOptions()

        # Sauce Labs expects MicrosoftEdge
        browser = "MicrosoftEdge"

    else:

        options = Options()
        browser = "chrome"



    # Common Sauce capabilities

    options.set_capability(
        "browserName",
        browser
    )

    options.set_capability(
        "browserVersion",
        browser_version
    )

    options.set_capability(
        "platformName",
        platform
    )


    sauce_options = {

        "username": username,

        "accessKey": access_key,


        # Test information
        "name": os.getenv(
            "TEST_NAME",
            "ECS Automation Test"
        ),

        "build": os.getenv(
            "BUILD_NAME",
            "GitHub Actions"
        ),

        "buildId": os.getenv(
            "BUILD_ID",
            ""
        ),


        # Sauce debugging
        "recordVideo": True,

        "capturePerformance": True,

        "extendedDebugging": True,


        # Tags visible in Sauce Dashboard
        "tags": [
            os.getenv(
                "TEST_TYPE",
                "automation"
            ),

            browser,

            os.getenv(
                "GIT_BRANCH",
                ""
            ),

            "GitHub Actions"
        ]
    }


    options.set_capability(
        "sauce:options",
        sauce_options
    )


    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=options
    )


    driver.maximize_window()


    return driver
