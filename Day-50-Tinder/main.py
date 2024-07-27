#Tinder Project

#!!!! Every way to login on tinder requires further verifications, rendering this project not really feasible.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

sleep(1)
sign_in_button = driver.find_element(By.XPATH,value='//*[@id="c-1330188189"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
sign_in_button.click()

sleep(1.5)
# google_sign_in = driver.find_element(By.CSS_SELECTOR,value='#c-248354030 iframe')
# google_sign_in.click()
facebook_sign_in = driver.find_element(By.XPATH,value='//*[@id="c1236398031"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_sign_in.click()

sleep(2)
window_handles = driver.window_handles  

driver.switch_to.window(window_handles[-1])
# email_field = driver.find_element(By.XPATH,value='//*[@id="identifierId"]')
email_field = driver.find_element(By.ID,value='email')
email_field.send_keys(os.environ["EMAIL"], Keys.TAB, os.environ["PASSWORD"], Keys.ENTER)




