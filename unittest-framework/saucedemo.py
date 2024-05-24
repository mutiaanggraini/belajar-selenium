import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 

class SaucedemoTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_login_success(self):
        browser = self.browser
        browser.get('http://www.saucedemo.com')
        browser.find_element(By.NAME, 'user-name').send_keys('standard_user')
        browser.find_element(By.NAME, 'password').send_keys('secret_sauce')
        browser.find_element(By.NAME, 'login-button').click()  

    def test_login_failed(self):
        browser = self.browser
        browser.get('http://www.saucedemo.com')
        browser.find_element(By.NAME, 'user-name').send_keys('bruhh')
        browser.find_element(By.NAME, 'password').send_keys('secret_sauce')
        browser.find_element(By.NAME, 'login-button').click() 

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()