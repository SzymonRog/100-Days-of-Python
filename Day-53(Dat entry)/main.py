import time

from  datascraper import DataScraper
from selenium import webdriver


data_scraper = DataScraper()
offers = data_scraper.get_offers()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSceuTBWPMOGNO2hNcjhsZZ26OefTXN_m4iA9A3BA3Nl6NI5Og/viewform?usp=dialog")

for i in range(0,len(offers)):
    time.sleep(1)

    address_input = driver.find_element(by="xpath",value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(by="xpath",value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(by="xpath",value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_input.send_keys(offers[i]["address"])
    price_input.send_keys(offers[i]["price"])
    link_input.send_keys(offers[i]["link"])

    submit_button.click()

    next_answer = driver.find_element(by="xpath", value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_answer.click()







