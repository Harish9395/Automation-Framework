from driver import get_mobile_driver
import time


def test_home_page():

    driver = get_mobile_driver()

    try:

        driver.get(
            "https://your-react-app-url.com"
        )

        time.sleep(5)

        title = driver.title

        print(
            "Page title:",
            title
        )

        assert driver.current_url.startswith(
            "https://"
        )

    finally:
        driver.quit()
