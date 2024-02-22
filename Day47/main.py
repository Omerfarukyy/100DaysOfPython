import requests
from bs4 import BeautifulSoup
import smtplib

email_name = "pythontestomer@gmail.com"
password = "pkwtlgnzuycesufa"
wanted_price = 100
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {"User-Agent": "Defined",
           "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4",
           }
# Brute forcing for bypassing reCaptcha
for i in range(10):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("span", class_="a-price-whole")
    title = soup.find("span", id="productTitle")
    try:
        print(price)
        print(price.getText())
        price = float(price.getText())
        title = title.getText()
        if price < float(wanted_price):
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=email_name, password=password)
                connection.sendmail(from_addr=email_name,
                                    to_addrs="omerfarukyy@hotmail.com",
                                    # because title contains non ASCII characters and ord() func doesnt work also
                                    # I didn't use title in the message
                                    msg=f"Subject:Amazon Price Alert!\n\n Your wanted product is now {price}! \n {url}")
        break
    except AttributeError:
        print("damn")
