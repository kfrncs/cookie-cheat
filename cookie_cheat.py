from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Firefox()
url = 'http://orteil.dashnet.org/cookieclicker/'
from time import sleep
from datetime import datetime

browser.get(url)
sleep(2)
# big cookie button to click
big_cookie = browser.find_element_by_id('bigCookie')
# fetch number of cookies owned & cookies per second
cookies = browser.find_element_by_id('cookies')

def tprint(string):
    return print(f'{datetime.now()}: {string}')


while True:

    # why does this click slowly?
    big_cookie.click()

    # if a golden cookie is found, click it,
    # then clear the variable
    try:
        shimmers = browser.find_element_by_id('shimmers')
        shimmers.click()
        tprint('shimmers clicked')
        del shimmers
        break
    except:
        tprint('shimmers not found')

    for i in range(0,10):
        try:
            product = browser.find_element_by_id(f'product{i}')
            product.click()
            tprint(f'product{i} clicked')
            big_cookie.click()

        except:
            tprint(f'product{i} not found')
            big_cookie.click()
            break
    
    for i in range(0,10):
        try:
            upgrade = browser.find_element_by_id(f'upgrade{i}')
            upgrade.click()
            tprint(f'upgrade{i} clicked')
            big_cookie.click()

        except:
            tprint(f'upgrade{i} not found')
            big_cookie.click()
            break
