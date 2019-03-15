# Cookie Cheat

A set of tools for optimizing your play of "Cookie Cutter"
from Orteil. Requires pyautogui

### conjure_calc: Checks optimal cookies saved for conjuring.
### autoclick: clicks like crazy til you move your mouse to the top left corner of the screen.

### Example:

1. Use conjure_calc(x) will return the number of cookies that you should
keep for optimal "Conjure Baked Goods" use.
x is your current Cookies Per Second (CPS), input *as a string* ending in:

'm', million                                                                                                           
'b', billion                                                                                                           
't', trillion                                                                                                          
'qd', quadrillion                                                                                                       
'qt', quintillion                                                                                                       
'sx', sextillion                                                                                                        
'sp', septillion                                                                                                        
'oct', octillion                                                                                                         
'non', nonillion  

2. Cast the Conjure Cookies spell when you're above the optimal cookie level. Use autoclick()
when you're not. You may need to adjust the x, y values passed into this function if your screen is a different size than mine.
