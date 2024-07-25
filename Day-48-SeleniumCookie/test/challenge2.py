from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page/")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
# article_count.click()


#LINK TEXT !!!
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

try:
    search_button = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
    search_button.click()

finally:
    sleep(0.5)

    search = driver.find_element(By.NAME, value="search")
    search.send_keys("Python", Keys.ENTER)

# driver.quit()