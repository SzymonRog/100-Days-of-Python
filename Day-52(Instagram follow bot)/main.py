from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import dotenv
import time

dotenv.load_dotenv()

username = os.getenv("INSTAGRAM_EMAIL")
password = os.getenv("INSTAGRAM_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://www.instagram.com/")
wait = WebDriverWait(driver, 180)

# -------------------Discard cookies if present-------------------
try:
    discard_cookie_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'))
    )
    discard_cookie_button.click()
except:
    pass  # jeśli prompt cookies nie pojawi się

# -------------------Login-------------------
username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')))

username_input.clear()
username_input.send_keys(username)
password_input.clear()
password_input.send_keys(password)
login_button.click()

# -------------Czekamy aż użytkownik wpisze kod SMS / 2FA-------------
choose = input("Wpisz kod SMS w przeglądarce i naciśnij y tutaj w terminalu, aby kontynuować...")


# -------------------Follow all followers of a person-----------------------
def follow_followers():
    followed_accounts = 0

    # Klikamy profil
    profile_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Profile']"))
    )
    profile_button.click()

    # Klikamy followers
    followers_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/followers/')]"))
    )
    followers_button.click()

    time.sleep(2)  # krótka pauza na załadowanie listy

    # Klikamy wszystkie "Obserwuj"
    last_height = driver.execute_script("return document.querySelector('div[role=dialog] ul').scrollHeight")

    while True:
        buttons = driver.find_elements(By.XPATH, "//div[text()='Obserwuj']")
        for b in buttons:
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", b)
                b.click()
                followed_accounts += 1
                print(f"Followed {followed_accounts}")
                time.sleep(2.5)  # bezpieczne tempo
            except:
                continue

        # przewijamy listę followers
        driver.execute_script("document.querySelector('div[role=dialog] ul').scrollTop += 500")
        time.sleep(2)

        new_height = driver.execute_script("return document.querySelector('div[role=dialog] ul').scrollHeight")
        if new_height == last_height:
            break  # koniec listy
        last_height = new_height


if choose == "y":
    follow_followers()
else:
    print("Nie wybrano opcji followers.")
