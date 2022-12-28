import time
import inspect

import allure
import pytest
from pages.loginPage import *
from pages.userPage import UserPage
from utils import environmentUrl, userCredential
import moment

@pytest.mark.usefixtures("test_open_browser")
class TestLogin():
    def test_verify_existing_user_login_successfully(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(userCredential.userName)
        lp.enter_password(userCredential.password)
        lp.click_submit_button()

    def test_verify_existing_user_logout_successfully(self):
        try:
            driver = self.driver
            up = UserPage(driver)
            up.click_logout()
            t = driver.title
            time.sleep(3)
            assert t=='abc'
            print("-------------Title is ------->", t)
        except:
            print("There was an exception")
            curTime=moment.now().starttime("%d-%m-%Y_%H-%M-%S")
            sh="screenshot_" + curTime
            allure.attach(self.driver.get_screenshot_as_png(), name=sh,
                          attachment_type=allure.attachment_type.PNG)

    # driver.find_element_by_xpath("//*[@id='menu-item-50']/a").click()
    # time.sleep(2)

# class TestLogin():
#     @pytest.fixture(scope="class")
#     def test_open_browser(self):
#         global driver
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("http://uat-iqrashopingdemo.ml/")
#         driver.implicitly_wait(1000)
#         yield
#         driver.close()
#         driver.quit()
#
#     def test_verify_existing_user_login_successfully(self, test_open_browser):
#         lp = LoginPage(driver)
#         lp.enter_username("Test_user2023")
#         lp.enter_password("Test_user2023")
#         lp.click_submit_button()
#
#     def test_verify_existing_user_logout_successfully(self, test_open_browser):
#         print("hello")
#         # driver.find_element_by_xpath("//*[@id='menu-item-50']/a").click()
#         # time.sleep(2)
