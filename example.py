from applepyautomator import automator
from applepyautomator.keycode import COMMON_KEYS
from applepyautomator.keycode import FUNCT_KEYS
from applepyautomator.shortcuts import SHORTCUTS


email = "email@example.com"
password = "password"

# example twitter login
# Launch Google Chrome
automator.launch_app("Google Chrome")   
# Type twitter URL
automator.type_keystroke("https://twitter.com/login")   
# Press ENTER
automator.press_key(COMMON_KEYS.ENTER)   
# Wait for 2 seconds and then type email
automator.type_keystroke(email, delay=2)    
# Press TAB
automator.press_key(COMMON_KEYS.TAB)
# Type Password
automator.type_keystroke(password)   
# Press ENTER
automator.press_key(COMMON_KEYS.ENTER)    

# open inspect element in google chrome and copy html code
# Press F12 to open developer options
automator.press_key(FUNCT_KEYS.F12)  
# Press F2
automator.press_key(FUNCT_KEYS.F2)
# Select all
automator.press_key(SHORTCUTS.SELECT_ALL)
# copy
automator.press_key(SHORTCUTS.COPY)

# quit Google Chrome
automator.quit_app("Google Chrome", delay=2)
