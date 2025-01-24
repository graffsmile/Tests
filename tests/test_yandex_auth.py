import os
import time
import unittest
import webbrowser
from os import error
import requests
from dotenv import load_dotenv
from selenium import webdriver
import selenium
import webdriver_manager
from requests import options
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


chrome_path = ChromeDriverManager().install()
service = Service(executable_path=chrome_path)

dotenv_path = 'config_example.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
LOGIN = os.getenv('YA_LOGIN')
PASSWORD = os.getenv('YA_PASSWORD')

class YaAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=service)

    def test_login_pass(self):
        self.driver.get('https://passport.yandex.ru/auth')
        self.assertIn('Авторизация', self.driver.title)
        element = self.driver.find_element(By.NAME, 'login')
        time.sleep(1)
        element.send_keys(LOGIN)
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        try:
            button = self.driver.find_element(By.XPATH, '//button[@data-t="button:pseudo"]')
            button.click()
            time.sleep(5)
            self.assertTrue(False, 'button is Find')
        except Exception as e:
            self.assertTrue(True, 'button is None')
        self.driver.find_element(By.NAME, 'passwd').send_keys(PASSWORD)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[@data-t="button:action:passp:sign-in"]').click()
        time.sleep(3)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()