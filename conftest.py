from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from utils import environmentUrl, userCredential


def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome", help="Enter browser")
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="class")
def test_open_browser(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(environmentUrl.uat)
        driver.implicitly_wait(1000)
        request.cls.driver = driver
    elif browser == 'firefox':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(environmentUrl.uat)
        driver.implicitly_wait(1000)
        request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
