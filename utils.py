from selenium import webdriver
import os
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import time
#
# PATH="chromedriver_linux64 (1)/chromedriver"
#
# options = Options()
# options.add_argument("headless")
# driver=webdriver.Chrome(PATH,options=options)

op=webdriver.ChromeOptions()
op.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)




ecomerce_webs=["https://www.amazon.com/","https://www.aliexpress.com/"]

# for website in ecomerce_webs:
#     driver.get(website)

def amazon():
    driver.get(ecomerce_webs[0])
    return driver.title

