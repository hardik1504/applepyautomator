# applepyautomator 
applepyautomator is a simplified implementation of applescript automation for macOs in python3. With applepyautomator you can easily automate ur macOs without having to write applescript or using automator.


## Overview

applepyautomator was written with focus on simplicity. It provides applescript automation for keyboard functionality to automate workflows that use key presses and shortcuts extensively, following are the key features

 - launch and quit apps with single call functions.
 - automate typing
 - automate key presses and key combinations for shortcuts

### Getting it
To download applepyautomator, either fork this github repo or simply use Pypi via pip.
```
$pip3 install applepyautomator
```

### Using it
To start using applepyautomator First import automator from applepyautomator
```python
from applepyautomator import automator
```

#### Launching an App
To launch an app use launch_app function in automator which takes a string argument containing the app name you want to launch. The app should be located in the default Applications directory of the macOS.
```python
automator.launch_app("App Name")
```

#### Quit an App
To quit an app is similar to launching an app, use quit_app function in automator to quit an already running app.
```python
automator.quit_app("App Name")
```

#### Automate Typing
To automate typing use type_keystroke function in automator which takes a string argument containing the content which you need to type.
```python
automator.type_keystroke("type this string")
```

#### Automate Keypress
To automate keypresses applepyautomator uses applescript key codes. key codes for Commonly used keys in the keyboard and some shortcuts 
are provided in following classes.

```python
keycode.COMMON_KEYS
```
contains keycodes for common keys such as ENTER, ESC, TAB, SPACE, CONTROL, COMMAND, OPTION etc.


```python
keycode.ALPHABETS
```
contains keycodes for alphabets from a-z and A-Z.


```python
keycode.FUNCT_KEYS
```
contains keycodes for function keys F1-F12


```python
keycode.NUMBERS
```
contains keycodes for numbers 0-9


```python
keycode.SPECIAL_CHARS
```
contains keycodes for special characters


similarly key codes for common shortcuts are provided in class
```python
shortcuts.SHORTCUTS
```


In order to automate a keypress call press_key function in automator which takes keycode as an argument. A keycode can be passed in the press_key function using available keys in classes mentioned above. (complete list of available keys and shortcuts is provided in keycodes.txt file)

```python
from applepyautomator.keycode import COMMON_KEYS
from applepyautomator.shortcuts import SHORTCUTS
automator.press_key(COMMON_KEYS.ENTER)
automator.press_key(SHORTCUTS.SELECT_ALL)
```

you can also provide a key code directly to the press_key function in string format

##### Pressing Multiple Keys in Combination

multiple key presses such as COMMAND + SPACE, COMMAND + CONTROL + SPACE or other custom shortcuts can be automated using the press_combination function in automator.

press_combination function takes two arguments first is the key code for any key in the combination except COMMAND, CONTROL and SHIFT, the second argument is a list containing maximum of 3 items which are key codes for COMMAND, CONTROL and SHIFT

code examples:
COMMAND + SPACE
```python
automator.press_combination(COMMON_KEYS.SPACE, [COMMON_KEYS.COMMAND])
```

COMMAND + CONTROL + SPACE
```python
automator.press_combination(COMMON_KEYS.SPACE, [COMMON_KEYS.COMMAND, COMMON_KEYS.CONTROL])
```

### Delay Argument
Every function in applepyautomator has an optional argument delay. Value of delay is number of seconds program waits before performing the function. The default value of delay is 0.125 seconds. Each function is performed after a delay of 0.125 seconds in order to give time to UI to load. In some cases you may need to increase or decrease the delay time depending upon the use case which can easily be done using delay argument.

```python
automator.press_key(COMMON_KEYS.ENTER, delay=2)
```

in above example program will wait for 2 seconds before performing the ENTER key press.

more usage examples can be found in example.py file

#### Credits

author of https://eastmanreference.com/complete-list-of-applescript-key-codes facilitated the key codes for mapping keys to respective key codes.

The program is tested on MacBook Pro with MacOs 10.15.4 running python 3.7.4
