from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_number.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search_icon = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
search_icon.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

