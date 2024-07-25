from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

form = driver.find_element(By.NAME, value="fName")
form.send_keys("Fukurou", Keys.TAB, "Kurosu", Keys.TAB, "dummyemail@gmail.com", Keys.ENTER)

