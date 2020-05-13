from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime

#search box
search_Box="//div[@class='_2S1VP copyable-text selectable-text']"


#user name input
user=input("\nEnter The Name Of Target User\n")


#text file creation
f=(open(user+".txt","w"))
f.write("DATA OF "+user+"\n")
f.write("--------------------------------------------------\n")
f.close

#online label detect
Status_online="//span[@class='O90ur _3FXB1' and @title='online']"


#open browser
browser=webdriver.Chrome()
browser.get("https://web.whatsapp.com/")
wait=WebDriverWait(browser,600)
input_box=wait.until(EC.presence_of_element_located((By.XPATH,search_Box)))
input_box.send_keys(user)
input_box.send_keys(Keys.ENTER)

time.sleep(15)
i=1
present_state=0
present_time=0
past_state=0
past_time=0
while(i>0):
    f=(open(user+".txt","a+"))
   
    try:
        browser.find_element_by_xpath(Status_online)
        #print(user +" is online")
        present_state=True
        if(i==1):
            past_state=True
            past_time=datetime.now().strftime("%H:%M:%S")
    except:
        #print(user+" is offline")
        present_state=False
        if(i==1):
            past_state=False
            past_time=datetime.now().strftime("%H:%M:%S")
    if(present_state!=past_state):
       
        if(present_state==True):
            present_time=datetime.now().strftime("%H:%M:%S")
            f.write(user +" was offline from "+past_time+" to "+present_time+"\n")
            past_state=present_state
            past_time=present_time 
        else:
            present_time=datetime.now().strftime("%H:%M:%S")
            f.write(user +" was online from "+past_time+" to "+present_time+"\n")
            past_state=present_state
            past_time=present_time     
    i=2
    f.close  


