import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DemowebshopTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    def test_1_register_positive(self):
        browser = self.browser
        browser.get('https://demowebshop.tricentis.com/register')
        
        browser.find_element(By.ID, 'gender-female').click()
        browser.find_element(By.ID, 'FirstName').send_keys('Mutia')
        browser.find_element(By.ID, 'LastName').send_keys('Anggraini')
        browser.find_element(By.ID, 'Email').send_keys('mutia@mail.com')
        browser.find_element(By.ID, 'Password').send_keys('password123')
        browser.find_element(By.ID, 'ConfirmPassword').send_keys('password123')
        browser.find_element(By.ID, 'register-button').click()
        
        success_message = browser.find_element(By.CLASS_NAME, 'result').text
        self.assertIn('Your registration completed', success_message)

    def test_2_register_negative_duplicate_email(self):
        browser = self.browser
        browser.get('https://demowebshop.tricentis.com/register')
        
        browser.find_element(By.ID, 'gender-female').click()
        browser.find_element(By.ID, 'FirstName').send_keys('Mutia')
        browser.find_element(By.ID, 'LastName').send_keys('Anggraini')
        browser.find_element(By.ID, 'Email').send_keys('mutia@mail.com')
        browser.find_element(By.ID, 'Password').send_keys('password123')
        browser.find_element(By.ID, 'ConfirmPassword').send_keys('password123')
        browser.find_element(By.ID, 'register-button').click()
        
        error_message = browser.find_element(By.CLASS_NAME, 'message-error').text
        self.assertIn('The specified email already exists', error_message)

    def test_3_login_positive(self):
        browser = self.browser
        browser.get('https://demowebshop.tricentis.com/login')
        
        browser.find_element(By.ID, 'Email').send_keys('mutia@mail.com')
        browser.find_element(By.ID, 'Password').send_keys('password123')
        browser.find_element(By.CSS_SELECTOR, 'input.button-1.login-button').click()
        
        account_header = browser.find_element(By.CLASS_NAME, 'account').text
        self.assertIn('mutia@mail.com', account_header)

    def test_4_login_negative(self):
        browser = self.browser
        browser.get('https://demowebshop.tricentis.com/login')
        
        browser.find_element(By.ID, 'Email').send_keys('mutia@mail.com')
        browser.find_element(By.ID, 'Password').send_keys('wrongpassword')
        browser.find_element(By.CSS_SELECTOR, 'input.button-1.login-button').click()
        
        error_message = browser.find_element(By.CLASS_NAME, 'message-error').text
        self.assertIn('Login was unsuccessful', error_message)

    def test_5_add_to_cart_and_checkout_positive(self):
        browser = self.browser
        browser.get('https://demowebshop.tricentis.com/login')

        browser.find_element(By.ID, 'Email').send_keys('mutia@mail.com')
        browser.find_element(By.ID, 'Password').send_keys('password123')
        browser.find_element(By.CSS_SELECTOR, 'input.button-1.login-button').click()
        
        account_header = browser.find_element(By.CLASS_NAME, 'account').text
        self.assertIn('mutia@mail.com', account_header)
        browser.find_element(By.CSS_SELECTOR, 'input.button-2.product-box-add-to-cart-button').click()

        browser.find_element(By.ID, 'giftcard_2_RecipientName').send_keys("Mutia")
        browser.find_element(By.ID, 'giftcard_2_RecipientEmail').send_keys("mutia@mail.com")
        browser.find_element(By.ID, 'giftcard_2_SenderName').send_keys("Anggraini")
        browser.find_element(By.ID, 'giftcard_2_SenderEmail').send_keys("anggraini@mail.com")
        browser.find_element(By.ID, 'giftcard_2_Message').send_keys("Happy Birthday!")
        browser.find_element(By.ID, 'add-to-cart-button-2').click()

        browser.find_element(By.ID, 'topcartlink').click()
        browser.find_element(By.ID, 'termsofservice').click()
        


    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
