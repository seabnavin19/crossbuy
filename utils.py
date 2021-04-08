from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

PATH="chromedriver_linux64 (1)/chromedriver"

options = Options()
options.add_argument("headless")
driver=webdriver.Chrome(PATH,options=options)



ecomerce_webs=["https://www.amazon.com/","https://www.aliexpress.com/"]

for website in ecomerce_webs:
    driver.get(website)
    print(driver.title)

def amazon():
    driver.get(ecomerce_webs[0])
    return driver.title

