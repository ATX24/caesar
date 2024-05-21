#Timed morphology dataminer

import selenium
from selenium import webdriver
import pandas as pd
import time
import keyboard
from pynput.keyboard import Key, Controller
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path='/Applications/panther4/chromedriver')
browser = webdriver.Chrome(service=service, options=chrome_options)
actions = ActionChains(browser)


#helper functions 
def movemouse(path):
    action = webdriver.ActionChains(browser)
    element = browser.find_element('xpath', path) # or your another selector here
    action.move_to_element(element)
    action.perform()


def feedsleep():
    #Get feedback
    time.sleep(3.0)
    browser.find_element('xpath', '/html/body/div[6]/div[1]/a').click()

def submitvalue(path, p):
    browser.find_element('xpath', path).send_keys(p)
    print(p)




#Make sure latin app is up and running
testname =
testpass = 

browser.get('https://laketravis.schoology.com/login/ldap?&school=17707999')
time.sleep(3)
# #Log into Website
browser.find_element("name", "mail").send_keys(testname)
browser.find_element("name", "pass").send_keys(testpass)
browser.find_element('name','op').click()

#Click on Latin 4 Class
browser.find_element("xpath", "/html/body/div[3]/div[3]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/ul/li[2]/section/div[2]").click()
#Press the Latin App Bookmark
browser.find_element("xpath", "//*[@id='app-run-364888653']/a").click()
time.sleep(5)

browser.get('https://lthslatin.org/')


#Click on challenge folder
browser.find_element('xpath', '/html/body/div[1]/div[2]/ul[3]/li[4]/h6/a').click()

#Click on challenge
browser.execute_script("window.scrollBy(0,500)","")
browser.find_element('name', 'timed_morphology').click()
time.sleep(3)

browser.find_element('xpath', '//*[@id="whatreading"]/option[2]').click()


selectionList = []
print('Beginning Test :)')
pyautogui.press('left')
pyautogui.press('right')




for i in range(30000): 
    df = pd.read_csv('datasets/wordstuff3.csv')
    words = list(df['words'])
    descs = list(df['descriptions'])

    dfno = pd.read_csv('datasets/notstuff.csv')
    wordsn = list(dfno['words'])
    notList = list(dfno['nots'])

    word1 = browser.find_element('xpath', '//*[@id="timedMorph_form"]').text
    dec1 = browser.find_element('xpath', '//*[@id="timedMorph_stimulus"]').text
    print(word1)
    print(dec1)
    

    autobar = False
    match = False
    for i, word in enumerate(words):
        if (word1 == word and descs[i] == dec1):
            print('match found in database - clicking true')
            # actions.send_keys(Keys.ARROW_LEFT).perform()
            # pyautogui.press('left')
            keyboard.press_and_release('left')

            time.sleep(0.75)
            match = True

            

    if(autobar == False and match == False):
            print("Don't know this one, time to learn! (By clicking false)")
            # actions.send_keys(Keys.ARROW_RIGHT).perform()
            # pyautogui.press('right')
            keyboard.press_and_release('right')


            time.sleep(0.5)
            #Get current streak to see if clicking false randomly worked
            yay = browser.find_element('xpath', '/html/body/div[6]/div[6]/h3').text
            print(yay)
            if ('streak' in yay):
                print(f'I learned that {word1} is not {dec1}')
                wordsn.append(word1)
                notList.append(dec1)
            else: 
                if ('is' in yay):
                    print(f'I learned that {word1} is {dec1}')
                    words.append(word1)
                    descs.append(dec1)

            df2 = pd.DataFrame({'words':words, 'descriptions':descs})
            df3 = pd.DataFrame({'words':wordsn, 'nots':notList})

            import os
            os.system('rm datasets/wordstuff3.csv')
            df2.to_csv('datasets/wordstuff3.csv')

            os.system('rm datasets/notstuff.csv')
            df3.to_csv('datasets/notstuff.csv')
    time.sleep(0.75) #Gives the new question time to load








        



