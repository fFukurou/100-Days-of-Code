#LinkedIn Project

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

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3979300879&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

sleep(1)
try:
    sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
    sign_in_button.click()
except:
    sign_in_button = driver.find_element(By.XPATH, value="/html/body/nav/div/a[2]")
    sign_in_button.click()

sleep(1)
username_form = driver.find_element(By.ID,value="username")
username_form.send_keys(os.environ["LINKEDIN_EMAIL"], Keys.TAB)
sleep(1)
passowrd_form = driver.find_element(By.ID,value="password")
passowrd_form.send_keys(os.environ["LINKEDIN_PASSWORD"])
sleep(1)
submit_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
submit_button.click()
sleep(1)
save_button = driver.find_element(By.XPATH,value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[6]/div/button')

sleep(10)
# jobs = driver.find_elements(By.CSS_SELECTOR, value = ".scaffold-layout__list-container li")
jobs = driver.find_elements(By.CSS_SELECTOR, value = ".job-card-container--clickable")

for job in jobs:
    job.click()
    save_button = driver.find_element(By.CLASS_NAME,value='jobs-save-button')
    save_button.click()
    sleep(1)