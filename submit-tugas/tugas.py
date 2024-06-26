import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

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
        browser.find_element(By.ID, 'Email').send_keys('mutiaa@mail.com')
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
        
        account_header = browser.find_element(By.CLASS_NAME,'account').text
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

        browser.find_element(By.ID, 'giftcard_2_RecipientName').send_keys("Baby")
        browser.find_element(By.ID, 'giftcard_2_RecipientEmail').send_keys("baby@mail.com")
        browser.find_element(By.ID, 'giftcard_2_Message').send_keys("Happy Birthday!")

        browser.find_element(By.ID, 'add-to-cart-button-2').click()
        browser.find_element(By.ID, 'topcartlink').click()
        time.sleep(2)

        browser.find_element(By.ID, 'termsofservice').click()
        browser.find_element(By.ID, 'checkout').click()


        browser.find_element(By.CSS_SELECTOR, 'input.button-1.new-address-next-step-button').click()
        browser.find_element(By.CSS_SELECTOR, 'input.button-1.payment-method-next-step-button').click()
        browser.find_element(By.CSS_SELECTOR, 'input.button-1.payment-info-next-step-button').click()
        browser.find_element(By.CSS_SELECTOR, 'input.button-1.confirm-order-next-step-button').click()
        
        browser.get('https://demowebshop.tricentis.com/checkout/completed/')
        confirmation_message = browser.find_element(By.CLASS_NAME, 'title').text
        self.assertIn('Your order has been successfully processed!', confirmation_message)

    def test_6_add_to_cart_and_checkout_negative(self):
        browser = self.browser
        browser.get('https://demowebshop.tricentis.com/login')

        browser.find_element(By.ID, 'Email').send_keys('mutia@mail.com')
        browser.find_element(By.ID, 'Password').send_keys('password123')
        browser.find_element(By.CSS_SELECTOR, 'input.button-1.login-button').click()
        
        account_header = browser.find_element(By.CLASS_NAME, 'account').text
        self.assertIn('mutia@mail.com', account_header)

        browser.find_element(By.CSS_SELECTOR, 'input.button-2.product-box-add-to-cart-button').click()

        browser.find_element(By.ID, 'giftcard_2_RecipientName').send_keys("Baby")
        browser.find_element(By.ID, 'giftcard_2_RecipientEmail').send_keys("baby@mail.com")
        browser.find_element(By.ID, 'giftcard_2_Message').send_keys("Happy Birthday!")
        browser.find_element(By.ID, 'addtocart_2_EnteredQuantity').send_keys("25")
        time.sleep(10)

        browser.find_element(By.ID, 'add-to-cart-button-2').click()

        error_message = browser.find_element(By.CLASS_NAME, 'content').text
        self.assertIn('The maximum quantity allowed for purchase is 5.', error_message)

if __name__ == "__main__":
    unittest.main()
