from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class StartPage:
    def __init__(self, driver):
        self._admin_menu_locator = "#menu_admin_viewAdminModule > b"
        self._user_management_menu_locator = "menu_admin_UserManagement"
        self._viewSystemUsers_locator = "menu_admin_viewSystemUsers"
        self._driver = driver

    def go_to_users(self):
        self._driver.find_element(By.CSS_SELECTOR, self._admin_menu_locator).click()
        self._driver.find_element(By.ID, self._user_management_menu_locator).click()
        element = self._driver.find_element(By.ID, self._user_management_menu_locator)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()
        self._driver.find_element(By.ID, self._viewSystemUsers_locator).click()
        return self

