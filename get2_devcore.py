from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html
import time

##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

#driver = webdriver.Chrome('.')  # Optional argument
driver = webdriver.Chrome()
driver.get('https://ondemandelearning.cisco.com/cisco/devcor10/videos/1')
#uname = driver.find_element_by_xpath('//*[@id="okta-signin-username"]')
#####
uname = driver.find_element_by_xpath('//*[@id="userInput"]')
#uname.click()
uname.send_keys('david.garces@akroscorp.com')
driver.find_element_by_xpath('//*[@id="login-button"]').click()
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "okta-signin-password"))
    )
except:
    driver.quit()
time.sleep(15)
pswrd = driver.find_element_by_xpath('//*[@id="okta-signin-password"]')
pswrd.click()
pswrd.send_keys('LOOKdark14monster26')
driver.find_element_by_xpath('//*[@id="okta-signin-submit"]').click()
try:
    element = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.ID, "okta-signin-password"))
    )
except:
    driver.quit()
####
time.sleep(10)

URL = 'https://ondemandelearning.cisco.com/cisco/devcor10/videos/'

for i in range (1, 5):
    URI = URL+str(i)
    driver.get(URI)
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for video in soup.find_all('video'):
        gvid = video['src']
        print(gvid)
        driver.get(gvid)
        time.sleep(10)    



