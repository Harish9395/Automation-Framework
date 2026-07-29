import os
import time
import pytest


@pytest.mark.performance
def test_home_page_performance(driver):

    app_url = os.getenv("APP_URL")

    if not app_url:
        raise Exception("APP_URL secret is missing")

    start_time = time.time()

    driver.get(app_url)

    end_time = time.time()

    load_time = end_time - start_time

    print(
        f"Page load time: {load_time:.2f} seconds"
    )

    # Send performance data to Sauce Labs job
    driver.execute_script(
        "sauce:context=Page load time: %.2f seconds" % load_time
    )

    assert load_time < 5
