#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

#Scan the code before proceeding further
input('Enter anything after scanning QR code')


#newConversation finds and clicks on the new conversation link on the main page
newConversation = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div')
newConversation.click()
time.sleep(5)

#searchPerson types the key into the search person space
searchPerson = driver.find_element_by_xpath('//*[@id="input-chatlist-search"]')
searchPerson.send_keys("Furkan")
time.sleep(5)

#selectPerson clicks on the first person on the list. Note: in this case there were only one person on the list.
#It may cause problems if there were multiple
#
selectPerson = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div[2]/div/div/div/div/div')
selectPerson.click()
time.sleep(5)

#types the key into the message space inn the conversation page
text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

msg_S = "."
text_box.send_keys(msg_S)
time.sleep(5)

sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/button')
sendButton.click()
time.sleep(5)

#button.click()
print "Done!"
