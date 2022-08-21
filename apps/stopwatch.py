# Imports
import time
import os

# Clears system
os.system('clear')

"""
Converts the timelapse(sec) for end result
"""
def convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = Hours:{0}, Minutes:{1}, Seconds:{2}".format(int(hours),int(mins),int(sec)))

# Main Code
input("To Start, [ENTER] -> ")
start_time = time.time()

input("To Stop, [ENTER] -> ")
end_time = time.time()

time_lapsed = end_time - start_time
convert(time_lapsed)
quit()