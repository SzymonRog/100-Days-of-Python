import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)




driver.get("https://ozh.github.io/cookieclicker")



WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
).click()

cookie_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)



with open("cookie_save.txt", "r") as f:
    save = f.read()

driver.execute_script("localStorage.setItem('CookieClickerGame', arguments[0]);", save)



def check_products():
    try:
        products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        if products:
            products[-1].click()  # kup najdroższy dostępny
    except:
        pass

def check_upgrades():
    try:
        upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
        if upgrades:
            upgrades[-1].click()
    except:
        pass



i = 0

while True:
    try:
        cookie_button.click()
        i += 1

        if i % 50 == 0:

            check_upgrades()
            check_products()

        if i % 200 == 0:
            i = 0
            save = driver.execute_script("return localStorage.getItem('CookieClickerGame');")
            with open("cookie_save.txt", "w") as f:
                f.write(save)


    except:
        cookie_button = driver.find_element(By.ID, "bigCookie")

save = driver.execute_script("return localStorage.getItem('CookieClickerGame');")

