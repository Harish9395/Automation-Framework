import os
import pytest

from drivers.driver_factory import get_driver
from api.clients.api_client import APIClient


# ==================================================
# Selenium UI Test Fixture (Sauce Labs)
# ==================================================

@pytest.fixture
def driver(request):

    # Sauce Labs test name will show actual pytest test name
    os.environ["TEST_NAME"] = request.node.name

    driver = get_driver()

    yield driver

    # Update Sauce Labs job result
    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            screenshot_path = (
                f"reports/{request.node.name}.png"
            )

            driver.save_screenshot(
                screenshot_path
            )

            driver.execute_script(
                "sauce:job-result=failed"
            )

        else:

            driver.execute_script(
                "sauce:job-result=passed"
            )

    driver.quit()


# ==================================================
# API Test Fixture
# ==================================================

@pytest.fixture
def api_client():

    client = APIClient()

    yield client

    client.close()


# ==================================================
# Pytest Hook
# Capture Test Result For Sauce Status
# ==================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call":

        item.rep_call = report
