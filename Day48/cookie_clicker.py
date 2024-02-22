from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

five_sec = time.time() + 5
five_min = time.time() + 60*5

cookie = driver.find_element(by=By.ID, value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()

    if time.time() > five_sec:

        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        can_buy = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                can_buy[cost] = id

        can_buy_highest = max(can_buy)
        to_purchase_id = can_buy[can_buy_highest]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        five_sec = time.time() + 5

    if time.time() > five_min:
        cps = driver.find_element(by=By.ID, value="cps").text
        print(cps)
        break
