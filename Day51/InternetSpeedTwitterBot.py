from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver.get("https://www.google.com")
speedtest = "https://www.speedtest.net/"
x = "https://twitter.com/"


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
        sleep(45)
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
        self.driver.get(x)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                                '1]/div/div/div[3]/div[5]/a')
        login_button.click()
        sleep(3)
        email_thing = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div'
                                                               '[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/'
                                                               'div[2]/div/input')
        email_thing.send_keys("pythontestomer@gmail.com", Keys.ENTER)
        sleep(2)
        username_thing = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                                  'div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label'
                                                                  '/div/div[2]/div/input')
        username_thing.send_keys("PythonComplaint", Keys.ENTER)
        sleep(2)
        password_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                                  'div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/d'
                                                                  'iv/label/div/div[2]/div[1]/input')
        password_input.send_keys("omerfaruk", Keys.ENTER)
        sleep(3)
        tweet_input = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/d'
                                                               'iv/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                               '1]/div/div/div/div/div/div/div/div/div/div/label/div[1]'
                                                               '/div/div/div/div/div/div[2]/div/div/div/div')
        if float(self.down) < 150 or float(self.up) < 15:
            tweet_input.send_keys(f"Hey internet provider, why my internet speed {self.down}down/{self.up}up when i pay"
                                  f" for 150down/15up")
        sleep(2)
        tweet_post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/di'
                                                              'v[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div'
                                                              '[2]/div[2]/div/div/div/div[3]')
        tweet_post.click()
