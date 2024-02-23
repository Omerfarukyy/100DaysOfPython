#  this project normally for job applications, but I don't want to apply, so I  just save them instead.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/")

email = "pythontestomer@gmail.com"
password = "omerfaruk"

email_input = driver.find_element(By.XPATH, value='//*[@id="session_key"]')
email_input.send_keys(f"{email}", Keys.ENTER)

password_input = driver.find_element(By.XPATH, value='//*[@id="session_password"]')
password_input.send_keys(f"{password}", Keys.ENTER)

sleep(2)
search_bar = driver.find_element(By.XPATH, value='//*[@id="global-nav-typeahead"]/input')
search_bar.send_keys("Python Developer", Keys.ENTER)

sleep(3)
jobs = driver.find_element(By.XPATH, value='//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
jobs.click()

sleep(3)
easy_apply_buttons_div = driver.find_element(By.XPATH, value='//*[@id="search-reusables__filters-bar"]/ul/li[7]/div')
easy_apply_buttons_div = easy_apply_buttons_div.find_element(By.TAG_NAME, value="button")
easy_apply_buttons_div.click()

sleep(3)
all_jobs = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")
for job in all_jobs:
    print("in the loop")
    sleep(3)
    job.click()
    sleep(3)
    save_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-save-button')
    save_button.click()
