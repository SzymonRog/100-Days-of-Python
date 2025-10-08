import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import os
import dotenv

dotenv.load_dotenv()

class SpeedTestBot:
    def __init__(self):
        self.ping = 0
        self.download_speed = 0
        self.upload_speed = 0

        self.x_login_url = "https://x.com/i/flow/login"
        self.speed_test_url = "https://www.speedtest.pl/"

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)



        self.x_password = os.getenv("X_PASSWORD")
        self.x_email = os.getenv("X_EMAIL")

        self.driver = webdriver.Chrome(options=self.chrome_options)

        self.wait = WebDriverWait(self.driver, 10)

    def login(self,message):
        try:
            self.driver.get(self.x_login_url)

            email_input = self.wait.until(EC.element_to_be_clickable((By.NAME, 'text')))
            email_input.click()
            email_input.send_keys(self.x_email)

            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Dalej"]/ancestor::button')))
            next_button.click()

            password_input = self.wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
            password_input.click()
            password_input.send_keys(self.x_password)

            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Zaloguj"]/ancestor::button')))
            login_button.click()

            self.post_message(message)
        except Exception as e:
            print(f"Could not login because X block bots: {e}")

    def post_message(self, message):
        tweet_msg_box = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        tweet_msg_box.click()
        tweet_msg_box.send_keys(message)

        time.sleep(0.5)

        tweet_button = self.wait.until(
            lambda d: d.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]') if d.find_element(
                By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]').get_attribute(
                "aria-disabled") == "false" else False
        )

        tweet_button.click()

        print("Message posted!")

    def check_speed(self):
        self.driver.get(self.speed_test_url)

        cookie_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button[1]')))
        cookie_button.click()

        start_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.big-button.start')))
        time.sleep(2)
        start_button.click()

        ms_tag = WebDriverWait(self.driver,90).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[1]/div[4]')))
        download_tag = WebDriverWait(self.driver,90).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div/span')))
        upload_tag = WebDriverWait(self.driver,90).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[3]/div[4]/div/span')))

        self.ping = float(ms_tag.text)
        self.download_speed = float(download_tag.text)
        self.upload_speed = float(upload_tag.text)

        message = (f"Download Speed: {download_tag.text}\n"
              f"Upload Speed: {upload_tag.text}\n"
              f"Ping: {ms_tag.text}"
        )
        print(message)
        return message
