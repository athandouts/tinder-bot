from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from credentials import *
import time

URL = "https://tinder.com"

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
browser.maximize_window()
browser.get(URL)

def sleep(t):
    time.sleep(t)

sleep(2)
cookies = browser.find_element(By.XPATH,"//*[text()='I decline']")
cookies.click()
sleep(2)
login = browser.find_element(By.XPATH,"//*[text()='Log in']")
login.click()
sleep(2)
facebook = browser.find_element(By.XPATH,"//*[text()='Login with Facebook']")
facebook.click()
sleep(2)
browser.switch_to.window(browser.window_handles[1])
sleep(2)
facebookCookies = browser.find_element(By.XPATH,"//*[@data-cookiebanner='accept_only_essential_button']")
facebookCookies.click()
sleep(2)
email = browser.find_element(By.XPATH,"//*[@id='email']")
email.send_keys(EMAIL)
password = browser.find_element(By.XPATH,"//*[@id='pass']")
password.send_keys(PASSWORD+Keys.ENTER)
sleep(10)
browser.switch_to.window(browser.window_handles[0])
location = browser.find_element(By.XPATH,"//*[text()='Allow']")
location.click()
sleep(2)
notifications = browser.find_element(By.XPATH,"//*[text()='Not interested']")
notifications.click()
sleep(3)
darkmode = browser.find_element(By.XPATH,"//*[@id='q1613718255']/main/div/div[2]/button")
darkmode.click()
sleep(3)
like = browser.find_element(By.XPATH,"//*[@id='q1392377819']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")

for i in range(100):
    try:
        like.click()
    except:
        browser.find_element(By.XPATH,"//*[@id='q848845626']/main/div/div[1]/div/div[4]/button").click()

    sleep(6)

browser.quit()



