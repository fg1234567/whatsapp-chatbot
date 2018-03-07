#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')


#name = input('Enter the name of user or group : ')
#msg = input('Enter the message : ')
#count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')
#user = driver.find_element_by_xpath('//div[@class = "_2wP_Y"]')

search = driver.find_element_by_xpath('//*[@id="input-chatlist-search"]')
search.send_keys("Halkman")

time.sleep(5)

user = driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[2]')

user.click()

time.sleep(5)

text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

msg_S = "This message has been sent by a simple bot! :)"
text_box.send_keys(msg_S)

button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/button')

time.sleep(5)

button.click()
print "Done!"

'''
msg2 = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/div[3]/div[16]/div/div/div/div[1]/div/span')

text = msg2.text

print "Last message you recieved is " + text
'''


'''
msg_box = driver.find_element_by_class_name('input-container')

for i in range(count):
    msg_box.send_keys(msg)
    #driver.find_element_by_class_name('compose-btn-send').click()
'''
