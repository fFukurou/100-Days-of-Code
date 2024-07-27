#Instagram Project
#DESCONTINUED DUE TO RISK OF GETTING INSTAGRAM ACCOUNT FLAGGED AS BOT AND BANNED

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
## MY BROWSER WAS OPENING UP IN PORTUGUESE AT THE TIME OF WRITING THIS CODE. HENCE THE PORTUGUESE WORDS.


load_dotenv()
URL = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get(URL)
        # driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.NAME,value='username').send_keys(os.environ["INSTAGRAM_EMAIL"], Keys.TAB, os.environ["INSTAGRAM_PASSWORD"], Keys.ENTER)
        sleep(3)

        self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Agora não')]").click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Agora não')]").click()


    
    def find_followers(self):
        self.driver.get(f"{URL}/{os.environ["TARGET_ACCOUNT"]}/")
        sleep(2)
        self.driver.find_element(By.XPATH,value="// button[contains(text(), 'seguindo')]").click()



    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
