import pytest

from utilities.config import load_environment


@pytest.mark.regression
def test_login(driver):

    url = load_environment()

    driver.get(url)

    assert "App Works" in driver.page_source
