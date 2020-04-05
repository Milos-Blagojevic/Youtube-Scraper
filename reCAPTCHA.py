import time
import re
import urllib
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
import requests
import timeit
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from datetime import datetime
import pickle

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--user-data-dir=chrome-data")

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--user-data-dir=chrome-data")
browser = webdriver.Chrome("C:/Users/milos/Downloads/chromedriver.exe",options=chrome_options)
# browser.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
# time.sleep(3)
# browser.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
# browser.find_element_by_xpath('//input[@type="email"]').send_keys('username')
# browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
# time.sleep(3)
# browser.find_element_by_xpath('//input[@type="password"]').send_keys('password')
# browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
# time.sleep(3)

chrome_options.add_argument("user-data-dir=chrome-data") 
# browser.get('https://www.somedomainthatrequireslogin.com')
# time.sleep(30)  # Time to enter credentials
# browser.quit()


browser.get('https://www.youtube.com/channel/UCJCSL8IJfD4d5nunRrmrT1Q/about')
pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in pickle.load(open("cookies.pkl", "rb")):
    if 'expiry' in cookie:
        del cookie['expiry']
    browser.add_cookie(cookie)
time.sleep(2)
go_to_email = browser.find_element_by_xpath('//*[@id="details-container"]/table/tbody/tr[1]/td[3]/ytd-button-renderer')
go_to_email.click()
time.sleep(2)
# browser.find_element_by_xpath('//*[@id="email-container"]/a').text
WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[starts-with(@name,'a-')]")))
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#recaptcha-anchor > div.recaptcha-checkbox-border"))).click()

# //*[@id="captcha-container"]/form/div/div/div/iframe
# browser.find_element_by_xpath('span//*[@id="recaptcha-anchor"]').click()
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="captcha-container"]/form/button/span').click()
