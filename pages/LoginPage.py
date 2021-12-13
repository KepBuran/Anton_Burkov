from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self._username_locator = "txtUsername"
        self._password_locator = "txtPassword"
        self._login_button_locator = "btnLogin"
        self._driver = driver

    def type_username(self, username):
        self._driver.find_element(By.ID, self._username_locator).send_keys(username)
        return self

    def type_password(self, password):
        self._driver.find_element(By.ID, self._password_locator).send_keys(password)
        return self

    def submit_login(self):
        self._driver.find_element(By.ID, self._login_button_locator).click()
        return self

    def login_as(self, username, password):
        self.type_username(username)
        self.type_password(password)
        return self.submit_login()




   