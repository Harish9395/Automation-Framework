import os


def test_mobile_chrome(mobile_driver):

    app_url = os.environ["APP_URL"]

    mobile_driver.get(app_url)

    title = mobile_driver.title

    print("Page title:", title)

    assert mobile_driver.current_url.startswith("http")
