from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")

name = 'Szymon'
last_name = 'Rogala'
email = 'Test123@gmail.com'

fname_input = driver.find_element(By.NAME, "fName")
lname_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")
submit_btn = driver.find_element(By.CSS_SELECTOR, "form.form-signin button")

fname_input.send_keys(name)
lname_input.send_keys(last_name)
email_input.send_keys(email)
submit_btn.click()




