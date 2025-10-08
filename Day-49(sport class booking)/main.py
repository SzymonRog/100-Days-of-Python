from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)


driver.get("https://appbrewery.github.io/gym")

email = 'student@test.com'
password = 'password123'


def login():
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email-input"]')))
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password-input"]')))
    submit_btn = wait.until(EC.presence_of_element_located((By.ID, "submit-button")))

    email_input.send_keys(email)
    password_input.send_keys(password)
    submit_btn.click()

classes_booked = 0
waitlists_joined = 0
already_booked_waitlisted = 0
total_classes = 0

def click_btns(buttons):
    for btn in buttons:
        btn.click()

try:
    login()
    wait = WebDriverWait(driver, 5)
    BookClassBtns = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '.ClassCard_cardActions__tVZBm button')
    ))


    all_classes = []
    classes_to_book = []
    for btn in BookClassBtns:
        btn_id = btn.get_attribute('id')
        date = btn_id.split('-')[-4:-1]
        date = '-'.join(date)
        date_obj = datetime.strptime(date, '%Y-%m-%d')

        if date_obj.weekday() == 1 or date_obj.weekday() == 3:
            if  btn.is_enabled():

                if btn.text == 'Book Class':
                    classes_booked += 1
                elif btn.text == 'Join Waitlist':
                    waitlists_joined += 1

                classes_to_book.append(btn)
            else:
                already_booked_waitlisted += 1
            total_classes += 1





    click_btns(classes_to_book)
except Exception as e:
    print(e)
print(f"Classes booked: {classes_booked}")
print(f"Waitlists joined: {waitlists_joined}")
print(f"Already booked waitlisted: {already_booked_waitlisted}")
print(f"Total classes: {total_classes}")












