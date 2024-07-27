#Twitter Project

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
from internet_speed_twitter_bot import InternetSpeedTwitterBot

load_dotenv()


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()

