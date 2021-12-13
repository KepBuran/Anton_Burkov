import pytest
import time
# import json
from selenium import webdriver
from behave import *
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import time

from pages.LoginPage import LoginPage
from pages.StartPage import StartPage
from pages.UsersPage import UsersPage
from pages.AddPage import AddPage

def generate_username():
  return str(hash(random.random()))

class TestFirst():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()


    def teardown_method(self):
        self.driver.quit()

    def launch_browser(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1166, 748)

    def login(self):
        return LoginPage(self.driver).login_as("Admin", "admin123")

    def go_to_users(self):
        return StartPage(self.driver).go_to_users()

    def add_user(self, username):
        UsersPage(self.driver, username).add_user()
        AddPage(self.driver, username).add_user()

    def find_user(self, username):
        return UsersPage(self.driver, username).find_user()

    def delete_user(self, username):
        return UsersPage(self.driver, username).delete_user()

    def check_deletion(self, username):
        return UsersPage(self.driver, username).check_deletion()

    def test(self, setup):
        self.launch_browser()
        self.login()
        time.sleep(0.5)
        self.go_to_users()

        username = generate_username()
        self.add_user(username)
        self.find_user(username)
        self.delete_user(username)
        assert self.check_deletion(username) == 1
