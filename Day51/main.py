from selenium import webdriver
from InternetSpeedTwitterBot import InternetSpeedTwitterBot
twitter_email = "pythontestomer@gmail.com"
twitter_password = "omerfaruk"

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

bot.tweet_at_provider()
