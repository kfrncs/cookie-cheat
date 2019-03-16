# coding: utf-8
'''conjure_calc: Checks optimal cookies saved for conjuring.
autoclick: Automatically clicks where the cookie is.
Stop the autoclick by moving the mouse to the top left.
'''
import pyautogui
import time

def num_humanize(num):
    ''' Convert big numbers to small numbers like the game does.
    '''
    
    num_dict = {
            1e6: 'm',   # million
            1e9: 'b',   # billion
            1e12: 't',  # trillion
            1e15: 'qd', # quadrillion
            1e18: 'qt', # quintillion
            1e21: 'sx', # sextillion
            1e24: 'sp', # septillion
            1e27: 'oct',# octillion
            1e30: 'non' # nonillion
            }
    
    if num > 1e30:
        num = num/1e30
        return str(num) + num_dict[1e30]
    elif num > 1e27:
        num = num/1e27
        return str(num) + num_dict[1e27]
    elif num > 1e24:
        num = num/1e24
        return str(num) + num_dict[1e24]
    elif num > 1e21:
        num = num/1e21
        return str(num) + num_dict[1e21]
    elif num > 1e18:
        num = num/1e18
        return str(num) + num_dict[1e18]
    elif num > 1e15:
        num = num/1e15
        return str(num) + num_dict[1e15]
    elif num > 1e12:
        num = num/1e12
        return str(num) + num_dict[1e12]
    elif num > 1e9:
        num = num/1e9
        return str(num) + num_dict[1e9]
    elif num > 1e6:
        num = num/1e6
        return str(num) + num_dict[1e6]
    else:
        return num

def num_biggify(human_num):
    ''' Turn a human-input string into a computer number. 
    '''
    
    if human_num.endswith('non'):
        human_num = human_num[:-3]
        human_num = float(human_num) * 1e30
        return human_num
    elif human_num.endswith('oct'):
        human_num = human_num[:-3]
        human_num = float(human_num) * 1e27
        return human_num
    elif human_num.endswith('sp'):
        human_num = human_num[:-2]
        human_num = float(human_num) * 1e24
        return human_num
    elif human_num.endswith('sx'):
        human_num = human_num[:-2]
        human_num = float(human_num) * 1e21
        return human_num
    elif human_num.endswith('qt'):
        human_num = human_num[:-2]
        human_num = float(human_num) * 1e18
        return human_num
    elif human_num.endswith('qd'):
        human_num = human_num[:-2]
        human_num = float(human_num) * 1e15
        return human_num
    elif human_num.endswith('t'):
        human_num = human_num[:-1]
        human_num = float(human_num) * 1e12
        return human_num
    elif human_num.endswith('b'):
        human_num = human_num[:-1]
        human_num = float(human_num) * 1e9
        return human_num
    elif human_num.endswith('m'):
        human_num = human_num[:-1]
        human_num = float(human_num) * 1e6
        return human_num

def conjure_calc(cps):
    ''' Checks the desired minimum number of cookies to make casting 
    the spell "Conjure Baked Goods" worth it. 
    
    Requires Grimoire (Wizard Tower lvl1 upgrade)'''
    cps = num_biggify(cps)
    cps = cps * 60 * 30 / 0.15
    return num_humanize(cps)

def autoclick():
    '''Automatically clicks where the cookie is. Doesn't switch the window or anything,
    so make sure you can see the cookie outside your terminal. Move mouse to topleft to 
    escape this horrible forever loop.'''
    while True:
        time.sleep(.01)
        pyautogui.click(x=200, y=350, clicks=500, interval=0.01) 

def pledger():
    while True:
        pyautogui.click(975, 630)
        time.sleep(.05)
        pyautogui.click(975, 630)
        time.sleep(.05)
        pyautogui.click(1035, 630)
        time.sleep(.05)

# TODO: Add converter small-numbers functionality,
#       user sets where they are (million, billion, trillion)
