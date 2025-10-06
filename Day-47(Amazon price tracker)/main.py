from  bs4 import BeautifulSoup
import requests
import os
import dotenv
import smtplib
from email.message import EmailMessage

dotenv.load_dotenv()

MIN_PRICE = 90

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pl,en-US;q=0.9,en;q=0.8,uk;q=0.7",
    "Host": "httpbin.org",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Opera GX\";v=\"122\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 OPR/122.0.0.0",
    "X-Amzn-Trace-Id": "Root=1-68e272a6-55ee5c92417f10f42d9ef2d5"
  }


amazon_product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(amazon_product_url, headers=headers)
response.raise_for_status()

content = response.text

soup = BeautifulSoup(content, "html.parser")
whole_price_tag = soup.find(name="span",class_="a-price-whole")
fraction_price_tag = soup.find(name="span",class_="a-price-fraction")

full_price = float(whole_price_tag.text) + float(fraction_price_tag.text)/100
print(full_price)

def send_email():
    global full_price
    global amazon_product_url

    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    username = os.getenv("GMAIL_USERNAME")
    password = os.getenv("GMAIL_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = "Product Price Alert!"
    msg["From"] = "rogalaszymon78@gmail.com"
    msg["To"] = "rogalaszymon78@gmail.com"
    msg.set_content(f""
                    f"Low price alert!Your items is only {full_price}$ now!"
                    f"See it here: {amazon_product_url}")

    with smtplib.SMTP(smtp_host, smtp_port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username, password)
        smtp.send_message(msg)
    print("Email has been sent!")

if full_price < MIN_PRICE:
    send_email()

