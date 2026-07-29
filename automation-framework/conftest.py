import os
import pytest

from drivers.driver_factory import get_driver


@pytest.fixture
def driver(request):

    os.environ["TEST_NAME"] = request.node.name

    driver = get_driver()

    yield driver

    if hasattr(request.node, "rep_call"):
        if request.node.rep_call.failed:
            driver.save_screenshot(
                f"reports/{request.node.name}.png"
            )
            driver.execute_script(
                "sauce:job-result=failed"
            )
        else:
            driver.execute_script(
                "sauce:job-result=passed"
            )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.rep_call = report
