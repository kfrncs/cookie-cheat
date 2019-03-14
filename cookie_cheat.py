# coding: utf-8
'''conjure_calc: Checks optimal cookies saved for conjuring.
autoclick: Automatically clicks where the cookie is.
Stop the autoclick by moving the mouse to the top left.
'''
import pyautogui

def conjure_calc(cps):
    ''' Checks the desired minimum number of cookies to make casting 
    the spell "Conjure Baked Goods" worth it. 
    
    Requires Grimoire (Wizard Tower lvl1 upgrade)'''
    return(cps * 60 * 30 / 0.15)

def autoclick():
    '''Automatically clicks where the cookie is. Doesn't switch the window or anything,
    so make sure you can see the cookie outside your terminal. Move mouse to topleft to 
    escape this horrible forever loop.'''
    while True: 
        pyautogui.click(x=200, y=350, clicks=100000, interval=0.0001) 

# TODO: Add converter small-numbers functionality,
#       user sets where they are (million, billion, trillion)
