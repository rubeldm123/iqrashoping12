class UserPage():
    def __init__(self, driver):
        self.driver = driver
        self.logout_btn = "//*[@id='menu-item-50']/a"

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_btn).click()
