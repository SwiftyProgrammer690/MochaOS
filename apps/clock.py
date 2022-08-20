# Import stuff
"""
Import os for clearing system
Import datetime for time and month and day
Import time for sleeping
"""
import datetime
import time
import os

# Clear system
os.system('clear')

# ASCII Art
logo = '''
       .-.-.
  ((  (__I__)  ))
    .'_....._'.
   / / .12 . \ \\
  | | '  |  ' | |
  | | 9  /  3 | |
   \ \ '.6.' / /
    '.`-...-'.'
jgs  /'-- --'\\
    `"""""""""`
'''

# Print out time, date
currentDT = datetime.datetime.now()
print(logo)
print("The time is:")
print(currentDT, sep=" <- Year, Time -> ")

# Give time for user to read output
time.sleep(10)
