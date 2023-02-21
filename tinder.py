from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from credentials import *
from time import sleep
import random




PICKUPLINES = ['I hope you know CPR, because you just took my breath away!'
            ,'So, aside from taking my breath away, what do you do for a living?',
            'I ought to complain to Spotify for you not being named this week’s hottest single.',
            'Are you a parking ticket? ‘Cause you’ve got ‘fine’ written all over you.',
            'Your eyes are like the ocean; I could swim in them all day.',
            'When I look in your eyes, I see a very kind soul.',
            'If you were a vegetable, you’d be a ‘cute-cumber.’',
            'Do you happen to have a Band-Aid? ‘Cause I scraped my knees falling for you.',
            'I never believed in love at first sight, but that was before I saw you.',
            'I didn’t know what I wanted in a woman until I saw you.',
            'I was wondering if you could tell me: If you’re here, who’s running Heaven?',
            'No wonder the sky is gray (or dark, if at night)—all the color is in your eyes.',
            'You’ve got everything I’ve been searching for, and believe me—I’ve been looking a long time.',
            'You’re like a fine wine. The more of you I drink in, the better I feel.',
            'You’ve got a lot of beautiful curves, but your smile is absolutely my favorite.',
            'Are you as beautiful on the inside as you are on the outside?',
            'If being sexy was a crime, you’d be guilty as charged.',
            'I was wondering if you’re an artist because you were so good at drawing me in.',
            'It says in the Bible to only think about what’s pure and lovely… So I’ve been thinking about you all day long.',
            'Do you have a map? I just got lost in your eyes.'
]

URL = "https://tinder.com"
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
browser.maximize_window()
browser.get(URL)
actions = ActionChains(browser)

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
sleep(5)




body = browser.find_element(By.TAG_NAME,"body")


def press(key):
    actions.send_keys(key)
    actions.perform()

def like(times = 100,city=None):
    likes = 0
    dislikes = 0
    notinterested = True
    for i in range(times):
       
        try:
            # Open Profile
            press(Keys.ARROW_UP)
            sleep(3)
            if (city is None):
                press(Keys.ARROW_RIGHT)
                likes +=1
                sleep(3)
            else:
                try:
                    browser.find_element(By.XPATH,f"//*[text()='Lives in {city}']").is_displayed()
                    print("Found")
                    # Like profile
                    press(Keys.ARROW_RIGHT)
                    likes +=1
                    sleep(3)

                except NoSuchElementException:
                    print("Not found")
                    # Dislike profile
                    press(Keys.ARROW_LEFT)
                    dislikes +=1
                    sleep(3)
            

            # This popup happens only once that's why we will stop this test after it's displayed
            if (notinterested):
                try:
                    browser.find_element(By.XPATH,"//div[text()='Not interested']").is_displayed()
                    press(Keys.ESCAPE)
                    print("Not interested is displayed")
                    notinterested = False
                    sleep(2)
                except NoSuchElementException:
                    print("Not interested isn't displayed")

            # This pop that let's you know that you're out of likes -> we will break when that's happen
            try:
                browser.find_element(By.XPATH,"//*[text()='No Thanks']").is_displayed()
                press(Keys.ESCAPE)
                print("Out of Likes")
                break
            except NoSuchElementException:
                print("Still likes")
                sleep(5)

        except:

            print("Exception raised in like function")
            
          
    # print out the number of likes and dislikes    
    print(f"You have liked : {likes} and disliked : {dislikes}")

def dislike(times = 100):

    notinterested = True
    for i in range(times):

        try:            

            # This popup happens only once that's why we will stop this test after it's displayed
            if (notinterested):
                try:
                    browser.find_element(By.XPATH,"//div[text()='Not interested']").is_displayed()
                    press(Keys.ESCAPE)
                    print("Not interested is displayed")
                    notinterested = False
                    sleep(2)
                except NoSuchElementException:
                    print("Not interested isn't displayed")

            # This pop that let's you know that you're out of likes -> we will break when that's happen
            try:
                browser.find_element(By.XPATH,"//*[text()='No Thanks']").is_displayed()
                press(Keys.ESCAPE)
                print("Out of Likes")
                break
            except NoSuchElementException:
                print("Still likes")
                sleep(5)
            
            # dislike
            press(Keys.ARROW_LEFT)
            sleep(2)
        except:

            print("Exception raised in like function")

def message():
    try:
        
        matches_panel = browser.find_element(By.XPATH,"//button[text()='Matches']")
        matches_panel.click()
        matches = browser.find_elements(By.CLASS_NAME,"matchListItem")
        
        for match in matches:
            matches_panel.click()
            if("Likes" not in match.accessible_name):
                match.click()
                sleep(4)
                name = browser.find_element(By.TAG_NAME,"h1").accessible_name
                pickupline = random.choice(PICKUPLINES)
                msg = f"Hi {name} {pickupline}"
                press(msg)
                send = browser.find_element(By.XPATH,"//*[@id='c-1351236777']/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button[2]")
                send.click()

                sleep(3)
        print("Messages were sent successfully  ")
    except:
        print("Exception raised in message function")




like(10,"Lappeenranta")

message()


browser.quit()



