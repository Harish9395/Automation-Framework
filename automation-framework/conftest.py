import os
import pytest

from drivers.driver_factory import get_driver


@pytest.fixture
def driver(request):

    # Use pytest test name in Sauce Labs dashboard
    os.environ["TEST_NAME"] = request.node.name

    driver = get_driver()

    yield driver

    # Update Sauce Labs job status
    if hasattr(request.node, "rep_call"):
        if request.node.rep_call.passed:
            driver.execute_script("sauce:job-result=passed")
        else:
            driver.execute_script("sauce:job-result=failed")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.rep_call = report
