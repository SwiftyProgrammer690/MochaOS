import time
import os

logo = '''
 __    __     ______     ______     __  __     __     ______    
/\ "-./  \   /\  __ \   /\  __ \   /\ \/\ \   /\ \   /\___  \   
\ \ \-./\ \  \ \ \/\ \  \ \ \/\_\  \ \ \_\ \  \ \ \  \/_/  /__  
 \ \_\ \ \_\  \ \_____\  \ \___\_\  \ \_____\  \ \_\   /\_____\ 
  \/_/  \/_/   \/_____/   \/___/_/   \/_____/   \/_/   \/_____/ 
'''

print("Welcome to...\n")
print(logo + "\n")
print("Get ready for a series of challenges that will test your mind!")
print("Sponsored by Yo Mom!")
print("\n")

# Main code
choice1 = input("What inspired the creation of MochaOS?")
if choice1 == "LeafOS":
    choice2 = input("What year did the Berlin Wall fall?")
    if choice2 == "1989":
        choice3 = input("If Urainium is in something, what does it make it?")
        if choice3 ==  "Radioactive":
            print("That's all...")
            quit()
        else:
            print("Wrong")
            time.sleep(2)
            quit()
    else:
        print("Wrong!")
        time.sleep(2)
        quit()
else:
    print("Wrong!")
    time.sleep(2)
    quit()