from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup Chrome with Selenium WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get('http://127.0.0.1:81')

title = driver.title

#driver.implicitly_wait(0.5)

print(title)

# Example of logging in
username = driver.find_element(by=By.NAME, value="username")
password = driver.find_element(by=By.NAME,  value="password")
login_button = driver.find_element('xpath', '//input[@type="submit"]')

username.send_keys('')
password.send_keys('')
login_button.click()

cookies = driver.get_cookies()
print(cookies)

driver.quit()
