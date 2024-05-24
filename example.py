from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.google.com/' )
assert 'Google' in browser.title

