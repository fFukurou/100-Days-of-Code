from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://store.steampowered.com/app/367520/Hollow_Knight/")

price = driver.find_element(By.CLASS_NAME, value="game_purchase_price")
# print(price.text)

search_bar = driver.find_element(By.NAME, value='term')
# print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, "store_search_link")
# print(button.size)

link = driver.find_element(By.CSS_SELECTOR, value=".dev_row a")
# print(link.text)

#XPATH
more_reviews = driver.find_element(By.XPATH, value='//*[@id="genresAndManufacturer"]/span/a[3]')
# print(more_reviews.text)



#Close will close a single tab
# driver.close()
#Quit will quit the entire progrogram 
driver.quit()