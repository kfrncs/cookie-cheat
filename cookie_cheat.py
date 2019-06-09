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
        shimmer = browser.find_element_by_id('shimmer')
        tprint('shimmer found')
        shimmer.click()
        tprint('shimmer clicked')
        del shimmer
        break
    except:
        tprint('shimmer not found')
