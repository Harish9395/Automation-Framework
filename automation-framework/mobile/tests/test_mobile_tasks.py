import pytest
import time


@pytest.mark.mobile
@pytest.mark.smoke
def test_mobile_app_launch(mobile_driver):

    assert mobile_driver.session_id is not None

    print(
        "Mobile application launched successfully"
    )


@pytest.mark.mobile
@pytest.mark.regression
def test_load_tasks(mobile_driver):

    # Click Load Tasks button
    load_button = mobile_driver.find_element(
        "accessibility id",
        "loadTasksButton"
    )

    load_button.click()


    time.sleep(3)


    # Verify task is displayed
    task = mobile_driver.find_element(
        "accessibility id",
        "taskName"
    )


    assert task.is_displayed()


    print(
        "Tasks loaded successfully"
    )
