from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

google_form_link = ("https://docs.google.com/forms/d/e/1FAIpQLSdZ1vos1meN7lVKt86AOs32Qk7EET_9cB3pES6H5Z9aEVbaMA/viewform?usp=sf_link")
URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
res = response.text

soup = BeautifulSoup(res, "html.parser")

links = [link["href"] for link in soup.find_all("a", class_="property-card-link")]
addresses = [address.text.strip() for address in soup.find_all("address")]
prices = [price.text[:6:] for price in soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")]
prices[14] = '$1,914'

for house in range(len(links)):
    driver.get(google_form_link)
    sleep(3)
    inputs = driver.find_elements(By.CSS_SELECTOR, value='.whsOnd')
    inputs[0].send_keys(addresses[house], Keys.TAB)
    inputs[1].send_keys(prices[house], Keys.TAB)
    inputs[2].send_keys(links[house], Keys.TAB, Keys.ENTER)

driver.close()
