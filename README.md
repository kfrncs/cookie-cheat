# Cookie Cheat

A set of tools for optimizing your play of "Cookie Cutter"
from Orteil. Requires pyautogui

### NOTE: when you're locked in, move the mouse to the top-left corner to get out of the loops. Save unsaved work before doing this. 
### conjure_calc: 
Checks optimal cookies saved for conjuring.
### autoclick: 
clicks like crazy til you move your mouse to the top left corner of the screen.
### pledger:
Automates the process of pledging to the grandmas.


### Example:

1: ```conjure_calc(x)``` will return the number of cookies that you should keep for optimal "Conjure Baked Goods" use (requires Wizard Tower). ```x``` is your current Cookies Per Second (CPS), input *as a 'string'* ending in:

```
m: million
b: billion
t: trillion
qd: quadrillion
qt: quintillion
sx: sextillion
sp: septillion
oct: octillion
non: nonillion
```
2: Cast the Conjure Cookies spell when you're above the optimal cookie level. Use ```autoclick()``` when you're not. You may need to adjust the x, y values passed into this function if your screen is a different size than mine. Use ```pyautogui.displayMousePosition()``` to figure out what the x and y values need to be. Move mouse to top-left corner to exit.

3:  Use ```pledger()``` to automate the process of Elder Pledge/Elder Covenant. See Step 2 for info on ```x,y```. Move mouse to top-left corner to exit.