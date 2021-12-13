import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class AddPage():
    def __init__(self, driver, username):
        self._employee_name_field_locator = "systemUser_employeeName_empName"
        self._username_field_locator = "systemUser_userName"
        self._password_field_locator = "systemUser_password"
        self._confirm_password_field_locator = "systemUser_confirmPassword"
        self._save_button_locator = "btnSave"

        self._driver = driver

        self._employee_name = "John Smith"
        self._username = username
        self._password = "asdxn43k32jejbhn4lkhen"
        self._password_confirmation = self._password



    def set_employee_name(self):
        self._driver.find_element(By.ID, self._employee_name_field_locator).click()
        self._driver.find_element(By.ID, self._employee_name_field_locator).send_keys(self._employee_name)

    def set_username(self):
        self._driver.find_element(By.ID, self._username_field_locator).click()
        self._driver.find_element(By.ID, self._username_field_locator).send_keys(self._username)

    def set_password(self):
        self._driver.find_element(By.ID, self._password_field_locator).click()
        self._driver.find_element(By.ID, self._password_field_locator).send_keys(self._password)

    def set_password_confirmation(self):
        self._driver.find_element(By.ID, self._confirm_password_field_locator).click()
        self._driver.find_element(By.ID, self._confirm_password_field_locator).send_keys(self._password_confirmation)
        return self

    def set_information(self):
        self.set_employee_name()
        self.set_username()
        self.set_password()
        self.set_password_confirmation()
        return self

    def confirm_additon(self):
        self._driver.find_element(By.ID, self._save_button_locator).click()
        return self

    def add_user(self):
        self.set_information()
        time.sleep(0.5)
        self._driver.find_element(By.ID, self._save_button_locator).click()
        time.sleep(0.5)

