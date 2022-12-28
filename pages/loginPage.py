class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_editbox = "//*[@id='username-9']"
        self.password_editbox = "//*[@id='user_password-9']"
        self.submit_btn = "//*[@id='um-submit-btn']"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_editbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_editbox).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element_by_xpath(self.submit_btn).click()
