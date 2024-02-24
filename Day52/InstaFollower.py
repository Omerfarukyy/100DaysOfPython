from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver.get("https://www.google.com")
instagram = "https://www.instagram.com/"
target_account = "chefsteps"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.email = "pythontestomer@gmail.com"
        self.password = "omerfaruk"

    def login(self):
        sleep(8)
        self.driver.get(instagram)
        email_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')

        email_input.send_keys(self.email, Keys.TAB)
        sleep(1)
        password_input.send_keys(self.password, Keys.ENTER)

    def find_followers(self):
        sleep(4)
        self.driver.get(f"{instagram}{target_account}/followers")
        scr1 = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/di'
                                                 'v[3]/div[1]/div')
        sleep(4)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

    def follow(self):
        pass
