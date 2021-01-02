#!/usr/bin/python3
import json, time, random
from twilio.rest import Client
from selenium import webdriver

costcoURL = "https://www.costco.com/xbox-series-x-1tb-console-with-additional-controller.product.100691493.html"
amazonURL = "https://www.amazon.com/dp/B08H75RTZ8/?coliid=I3T2N56UL91B2I&colid=6ONAQH8MLC04&psc=0&ref_=lv_ov_lig_dp_it"

dr1 = webdriver.Firefox()
dr2 = webdriver.Firefox()

dr1.get(costcoURL)
dr2.get(amazonURL)

def pause(low, high):
    interval = low + (high - low) * random.random()
    time.sleep(interval)

def sendTextNotification(message):
    with open('twilioKeys.json', 'r') as jsonFile:
        data = json.load(jsonFile)
        myClient = Client(data['accountSID'], data['authToken'])
        message = myClient.messages.create(body=message, from_=data['twilioPhone'], to=data['myPhone'])

def refresh(driver, iter):
    if iter:
        driver.refresh()

def addToCart(driver, iter, elementID, notifierMessage):
    if iter:
        try:
            elem = None
            elem = driver.find_element_by_id(elementID)
            if elem:
                elem.click()
                sendTextNotification(notifierMessage)
                iter = False
        except Exception as err:
            print('Error occured: ', err)
    return iter


iter1 = True
iter2 = True

login = input('Press return when user is logged in to the desired webpage\n');

while True:
    refresh(dr1, iter1)
    refresh(dr2, iter2)

    pause(40, 60)

    iter1 = addToCart(dr1, iter1, "add-to-cart-btn", "Inventory @ Costco")
    iter2 = addToCart(dr2, iter2, "add-to-cart-button", "Inventory @ Amazon")
