#Finding the top 10 champions with the most winrate

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
from pprint import pprint
import csv

CHAMPION_AMOUNT = 10


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()




driver.get("https://www.op.gg/statistics/champions?region=br&position=jungle")
sleep(3)

driver.find_element(By.XPATH,value='//*[@id="content-container"]/div[2]/table/thead/tr/th[5]').click()
sleep(1)

champions = driver.find_elements(By.CSS_SELECTOR,value='tr td a strong')
win_rates = driver.find_elements(By.CSS_SELECTOR,value='tr td div .css-1xqka05')

champion_list = []
win_rate_list = []

for champion in champions[:CHAMPION_AMOUNT]:
    champion_list.append(champion.text)

for win_rate in win_rates[:CHAMPION_AMOUNT]:
    win_rate_list.append(win_rate.text)


win_dict = {}


for i in range(len(champion_list)):
    win_dict[champion_list[i]] = win_rate_list[i]

rows = [(key, value) for key, value in win_dict.items()]

with open("Day-53-DataEntry/data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Champion", "WinRate"])
    writer.writerows(rows)


driver.quit()