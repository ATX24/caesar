import selenium
from selenium import webdriver
import pandas as pd
import time



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path='/Applications/panther5/chromedriver')
browser = webdriver.Chrome(service=service, options=chrome_options)


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
testname = ''
testpass = ''

browser.get('https://laketravis.schoology.com/login/ldap?&school=17707999')
browser.implicitly_wait(15)

#Log into Website
browser.find_element("name", "mail").send_keys(testname)
browser.find_element("name", "pass").send_keys(testpass)
browser.implicitly_wait(15)
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
browser.find_element('xpath', '/html/body/div[1]/div[2]/ul[3]/li[4]/div/ul/li[2]/a').click()
time.sleep(3)

#Get items (Noun and Adjective)
item1 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[1]/h3').text
item2 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[2]/h3').text
item3 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[3]/h3').text
item4 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[4]/h3').text
item5 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[5]/h3').text
item6 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[6]/h3').text
item7 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[7]/h3').text
item8 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[8]/h3').text
item9 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[9]/h3').text
item10 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[10]/h3').text
itemList = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10]
#Get answers
time.sleep(3)
yes1 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[1]/div/div/div[1]/label')
yes2 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[2]/div/div/div[1]/label')
yes3 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[3]/div/div/div[1]/label')
yes4 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[4]/div/div/div[1]/label')
yes5 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[5]/div/div/div[1]/label')
yes6 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[6]/div/div/div[1]/label')
yes7 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[7]/div/div/div[1]/label')
yes8 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[8]/div/div/div[1]/label')
yes9 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[9]/div/div/div[1]/label')
yes10 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[10]/div/div/div[1]/label')

no1 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[1]/div/div/div[2]/label')
no2 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[2]/div/div/div[2]/label')
no3 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[3]/div/div/div[2]/label')
no4 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[4]/div/div/div[2]/label')
no5 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[5]/div/div/div[2]/label')
no6 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[6]/div/div/div[2]/label')
no7 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[7]/div/div/div[2]/label')
no8 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[8]/div/div/div[2]/label')
no9 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[9]/div/div/div[2]/label')
no10 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[10]/div/div/div[2]/label')

#answer test
# yes1.click()
# no2.click()
# yes3.click()
# no4.click()
# yes5.click()
# browser.execute_script("window.scrollBy(0,500)","")
# no6.click()
# yes7.click()
# no8.click()
# yes9.click()
# browser.execute_script("window.scrollBy(0,500)","")
# no10.click()

yesList = [yes1, yes2, yes3, yes4, yes4, yes6, yes7, yes8, yes9, yes10]
noList  = [no1, no2, no3, no4, no5, no6, no7, no8, no9, no10]
#Spit items into nouns and adj
nouns = []
adjs = []

for item in itemList:
    doublething = item.split()
    nouns.append(doublething[0])
    adjs.append(doublething[1])

base11 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[1]/p[1]/em').text
base12 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[2]/p[1]/em').text
base13 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[3]/p[1]/em').text
base14 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[4]/p[1]/em').text
base15 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[5]/p[1]/em').text
base16 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[6]/p[1]/em').text
base17 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[7]/p[1]/em').text
base18 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[8]/p[1]/em').text
base19 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[9]/p[1]/em').text
base20 = browser.find_element('xpath', '/html/body/div[6]/div[2]/form/ol/li[10]/p[1]/em').text

baseListNoun = [base11, base12, base13, base14, base15, base16, base17, base18, base19, base20]

#Get base words to get declensions (2nd genitive)
base1 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[1]/p[2]/em').text
base2 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[2]/p[2]/em').text
base3 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[3]/p[2]/em').text
base4 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[4]/p[2]/em').text
base5 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[5]/p[2]/em').text
base6 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[6]/p[2]/em').text
base7 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[7]/p[2]/em').text
base8 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[8]/p[2]/em').text
base9 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[9]/p[2]/em').text
base10 = browser.find_element('xpath', '//*[@id="pairs_list"]/li[10]/p[2]/em').text

baseListAdj = [base1, base2, base3, base4, base5, base6, base7, base8, base9, base10]



#Get the declensions of each word using a delcension library 
declensionbrary =  {
    "ae": "1st",
    "ī":  "2nd", 
    "is": "3rd", 
    "ūs": "4th", 
    "eī": "5th"
}

declensionsNoun = []
from unidecode import unidecode

for i, base in enumerate(baseListNoun): 
    ahh = base.split(",")
    base = ahh[0]
    check = False
    for key, value in declensionbrary.items(): 
        if unidecode(base).endswith(unidecode(key)):
            declensionsNoun.append(str(value))
            check = True
    if (check == False):
        declensionsNoun.append("1st") #This is basically if it doesn't match any in the dictionary - auto goes to first

declensionsAdj = []

from unidecode import unidecode

for i, base in enumerate(baseListAdj): 
    ahh = base.split(",")
    base = ahh[0]
    check = False
    for key, value in declensionbrary.items(): 
        if unidecode(base).endswith(unidecode(key)):
            declensionsAdj.append(str(value))
            check = True
    if (check == False):
        declensionsAdj.append("1st") #This is basically if it doesn't match any in the dictionary - auto goes to first
    
print("NOUNS")
print(nouns)
print("ADJS")
print(adjs)
print("________________")
print("EXTRA INFORMATION")
print(baseListNoun)
print(baseListAdj)
print("____________")
print("DECLENSIONS")
print(declensionsNoun)
print(declensionsAdj)


from nounsadjs import dictionary
    
for i, declension in enumerate(nouns):
    nouns = nouns[i]
    adj = adjs[i]
    declensionNoun = declensionsNoun[i]
    declensionAdj = declensionsAdj[i]
    for key, item in dictionary.items:
        print(key)
        print(item)

   
