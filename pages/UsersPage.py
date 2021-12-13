from selenium import webdriver
from selenium.webdriver.common.by import By

class UsersPage():
    def __init__(self, driver, username):
        self._search_field_locator = "searchSystemUser_userName"
        self._search_button_locator = "searchBtn"
        self._add_button_locator = "btnAdd"
        self._reset_button_locator = "resetBtn"
        self._delete_button_locator = "btnDelete"
        self._delete_dialog_button_locator = "dialogDeleteBtn"
        self._driver = driver
        self._username = username

    def add_user(self):
        self._driver.find_element(By.ID, self._add_button_locator).click()

    def search_user(self):
        self._driver.find_element(By.ID, self._search_field_locator).send_keys(self._username)
        self._driver.find_element(By.ID, self._search_field_locator).click()
        self._driver.find_element(By.ID, self._search_button_locator).click()

    def reset(self):
        self._driver.find_element(By.ID, self._reset_button_locator).click()

    def find_user(self):
        self._driver.find_element(By.ID, self._search_field_locator).send_keys(self._username)
        self._driver.find_element(By.ID, self._search_field_locator).click()
        self._driver.find_element(By.ID, self._search_button_locator).click()
        self.reset()

    def delete_user(self):
        self._driver.find_element(By.XPATH, "//tr[td[a[contains(text(),\'" + self._username + "\')]]]//input").click()
        self._driver.find_element(By.ID, "btnDelete").click()
        self._driver.find_element(By.ID, "dialogDeleteBtn").click()

    def check_deletion(self):
        try:
            self._driver.find_element(By.XPATH, "//tr[td[a[contains(text(),\'" + self._username + "\')]]]//input").click()
            return 0
        except Exception:
            return 1







