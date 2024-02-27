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
        sleep(17)
        self.driver.get(instagram)
        email_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')

        email_input.send_keys(self.email, Keys.TAB)
        sleep(1)
        password_input.send_keys(self.password, Keys.ENTER)

    def find_followers(self):
        sleep(8)
        self.driver.get(f"{instagram}{target_account}")

        for _ in range(10):
            self.driver.find_element('/html/body/div[5]/div/div/div[2]//a').send_keys(Keys.END)
            sleep(2)  # Allow the list to update

    def follow(self):
        sleep(10)
        list_buttons = self.driver.find_elements(By.XPATH, value='/html/body/div[5]/div/div/div[2]/ul//button')
        for button in list_buttons:
            if button.text == "Follow":
                button.click()
                sleep(2)
