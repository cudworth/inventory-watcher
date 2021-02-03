#!/usr/bin/python3
import json, time
from twilio.rest import Client
from selenium import webdriver

def sendTextNotification(message):
    myClient = Client(data['twilioAccountSID'], data['twilioAuthToken'])
    message = myClient.messages.create(body=message, from_=data['twilioPhone'], to=data['myPhone'])

def addToCart(driver, iter, elementID, notifierMessage):
    time.sleep(3)
    try:
        elem = driver.find_element_by_id(elementID)
        if elem and 'out-of-stock' not in elem.get_attribute("class"):
            elem.click()
            sendTextNotification(notifierMessage)
            print('add to cart btn clicked')
            iter = False
    except Exception as err:
        print('Error occured: ', err)
    return iter

def costcoLogin(driver):
    driver.find_element_by_id('logonId').send_keys(data['costcoEmail'])
    driver.find_element_by_id('logonPassword').send_keys(data['costcoPassword'])
    driver.find_element_by_id('option1').send_keys(' ')
    driver.find_element_by_id('LogonForm').submit()
    time.sleep(20)


fo = open('credentials.json', 'r')
data = json.load(fo)
fo.close()

loginPage = "https://www.costco.com/LogonForm"
productPage = "https://www.costco.com/xbox-series-x-1tb-console-with-additional-controller.product.100691493.html"

myDriver = webdriver.Firefox()

myDriver.get(loginPage)

costcoLogin(myDriver)

myDriver.get(productPage)

iter = True
while iter:
    time.sleep(25);
    myDriver.refresh()
    iter = addToCart(myDriver, iter, "add-to-cart-btn", "Inventory @ Costco")
