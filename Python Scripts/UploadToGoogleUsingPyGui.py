# import libraries
import pyautogui as gui
import webbrowser
import time
import pyperclip
import pw

#The pixels on a full screen chrome window for my laptop, values may change for other laptops.
new=77,277
new_file=157,337

#open the correct chrome profile
#adjust the timing depending on how fast your computer loads the pages.
webbrowser.open(pw.gurl)
time.sleep(3)
gui.click(new)
time.sleep(3)
gui.click(new_file)
time.sleep(2)
gui.typewrite(pyperclip.paste())
time.sleep(1)
gui.press('enter')