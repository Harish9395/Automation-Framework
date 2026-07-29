import pytest


@pytest.mark.regression
def test_login(driver):

    driver.get("application-url")

    username = driver.find_element(
        "id",
        "username"
    )

    username.send_keys("testuser")


    password = driver.find_element(
        "id",
        "password"
    )

    password.send_keys("password")


    driver.find_element(
        "id",
        "login"
    ).click()


    assert "Dashboard" in driver.page_source
