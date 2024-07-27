from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import speedtest

load_dotenv()

PROMISED_DOWN = 500
PROMISED_UP = 120

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.down = 0
        self.up = 0
        self.st = speedtest.Speedtest()

    def get_internet_speed(self):
        print("Fetching speeds...")
        dwnld = round(self.st.download() / 1000000, 2)
        upld = round(self.st.upload() / 1000000, 2)
        print(dwnld, upld)
        self.down = dwnld
        self.up = upld


    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver = webdriver.Chrome(options=self.chrome_options)
            message = f'''Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?'''


            self.driver.get("https://twitter.com/i/flow/signup")

            self.driver.maximize_window()

            sleep(1)
            login_button = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/button/span/span')
            login_button.click()

            sleep(3)

            form = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'\
            '')
            form.send_keys(os.environ["TWITTER_EMAIL"], Keys.ENTER)

            sleep(2)

            self.driver.find_element(By.NAME,value='text').send_keys(os.environ["TWITTER_USERNAME"], Keys.ENTER)
            sleep(2)

            self.driver.find_element(By.NAME,value='password').send_keys(os.environ["TWITTER_PASSWORD"], Keys.ENTER)

            sleep(5)

            tweet_compose = self.driver.find_element(By.CSS_SELECTOR, value='.notranslate')
            tweet_compose.send_keys(message)
            sleep(1)

            self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()

        else:
            self.driver.quit()

    