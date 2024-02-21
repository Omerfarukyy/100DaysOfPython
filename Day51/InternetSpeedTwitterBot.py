from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver.get("https://www.google.com")
speedtest = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = int
        self.up = int

    def get_internet_speed(self):
        self.driver.get(speedtest)
        button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/di'
                                                          'v[1]/a')
        button.click()
        sleep(30)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                             '/div[3]/div/''div[3]/div/div/div[2]/div[1]/div[1]/div/div'
                                                             '[2]/span')
        self.down = self.down.text
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/d'
                                                           'iv[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/sp'
                                                           'an')
        self.up = self.up.text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        pass
