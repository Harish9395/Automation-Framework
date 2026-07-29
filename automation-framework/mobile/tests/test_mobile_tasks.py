import os

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.mobile
@pytest.mark.smoke
def test_mobile_app_launch(mobile_driver):

    app_url = os.getenv("APP_URL")

    if not app_url:
        raise Exception("APP_URL environment variable is missing")

    mobile_driver.get(
        f"{app_url.rstrip('/')}/mobile"
    )

    assert "ECS Task Mobile App" in mobile_driver.page_source


@pytest.mark.mobile
@pytest.mark.smoke
def test_mobile_load_tasks(mobile_driver):

    app_url = os.getenv("APP_URL")

    if not app_url:
        raise Exception("APP_URL environment variable is missing")

    mobile_driver.get(
        f"{app_url.rstrip('/')}/mobile"
    )

    load_button = WebDriverWait(
        mobile_driver,
        10
    ).until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "loadTasks"
            )
        )
    )

    load_button.click()

    WebDriverWait(
        mobile_driver,
        10
    ).until(
        EC.presence_of_element_located(
            (
                By.CLASS_NAME,
                "task"
            )
        )
    )

    page = mobile_driver.page_source

    assert "task1" in page
    assert "task2" in page
    assert "task3" in page
