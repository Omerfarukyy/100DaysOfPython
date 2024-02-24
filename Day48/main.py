from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

#              Amazon site things
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_dollar.text}.{price_cents.text}")

#              Python site things
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
#
# asd = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(asd.text)

table = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
times = table.find_elements(By.TAG_NAME, value="time")
time_list = []

for time in times:
    time_list.append(time.get_attribute("datetime")[:10])
events = table.text.splitlines()[1::2]

main_dict = {}
for event in range(len(events)):
    dicts = {"name": f"{events[event]}",
             "date": f"{time_list[event]}"}
    main_dict.update({f"{event}": f"{dicts}"})

# driver.close()
print(main_dict)
driver.quit()
