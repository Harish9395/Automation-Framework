from selenium import webdriver

def get_driver():

    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    return driver
