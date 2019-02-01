# coding: utf-8
'''ConjureCalc: Checks optimal cookies saved for conjuring.

Example:

1. import conjureCalc in Python REPL (I use IPython)
    [you could also run ipython -i conjureCalc.py]

2. conjureCalc(x) will return the number of cookies that you should
    keep for optimal "Conjure Baked Goods" use.
    x is your current Cookies Per Second (CPS).
    (Note that if you have Shorten Numbers on, use the "Shortened 
    Number" and this will return a "Shortened Number" too.)

3. Spend cookies but keep above the optimal level.

'''

def conjureCalc(ownedCookies):
    ''' Checks the desired minimum number of cookies to make casting 
    the spell "Conjure Baked Goods" worth it. 
    
    Requires Grimoire (Wizard Tower lvl1 upgrade)'''
    return(ownedCookies * 60 * 30 / 0.15)


# TODO: Make operable directly via command line.

