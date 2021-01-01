#!/usr/bin/python3
import os, json, webbrowser, requests, time, random
from twilio.rest import Client
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

url = "https://www.costco.com/xbox-series-x-1tb-console-with-additional-controller.product.100691493.html"

driver = webdriver.Firefox()
driver.get(url)

#wait = WebDriverWait(driver, 10);

login = input('Press return when user is logged in to the desired webpage\n');

def pause(low, high):
    interval = low + (high - low) * random.random()
    time.sleep(interval)

def sendTextNotification():
    with open('twilioKeys.json', 'r') as jsonFile:
        data = json.load(jsonFile)
        myClient = Client(data['accountSID'], data['authToken'])
        message = myClient.messages.create(body='SUCCESS', from_=data['twilioPhone'], to=data['myPhone'])


iterate = True  
while iterate == True:

    driver.refresh()
    pause(20, 40)

    #wait.until(presence_of_element_located((By.LINK, "random")))

    try:
        #links = driver.find_elements_by_tag_name("a") #Reddit

        elem = driver.find_element_by_id("add-to-cart-btn") #Costco
        if elem:
            elem.click()
            sendTextNotification()
            iterate = False

        '''
        for link in links:
            if link.get_attribute('href') == target:
                link.click()
                iterate = False
                break
        '''

    except Exception as err:
        print('Error occured: ', err)
