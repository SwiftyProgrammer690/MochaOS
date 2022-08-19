# Made by Swarit Choudhari

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
print("Sponsored by absolutely no one! :(")
print("\n")

# Main code
choice1 = input("What inspired the creation of MochaOS? ")
if choice1 == "LeafOS":
    choice2 = input("What year did the Berlin Wall fall? ")
    if choice2 == "1989":
        choice3 = input("If Urainium is in something, what does it make it? ")
        if choice3 ==  "Radioactive":
            choice4 = input("How many holes are there in a game of golf? ")
            if choice4 != "18":
                print("Wrong")
                time.sleep(2)
                quit()
            else:
                choice5 = input("What is the name of the Jungle Book bear? ")
                if choice5 != "Baloo":
                    print("Wrong!")
                    time.sleep(2)
                    quit()
                else:
                    choice6 = input("Who made replit? ")
                    if choice6 != "Amjad Masad":
                        print("Wrong!")
                        time.sleep(2)
                        quit()
                    else:
                        choice7 = input("Who won the first super bowl? ")
                        if choice7 != "Green Bay Packers":
                            print("Wrong!")
                            time.sleep(2)
                            quit()
                        else:
                            choice8 = input("Who is the best chess player? ")
                            if choice8 != "Magnus Carlsen":
                                print("Wrong!")
                                time.sleep(2)
                                quit()
                            else:
                                choice9 = input("How to save mother earth in 3 WORDS? ")
                                if choice9 != "Reduce, Reuse, Recycle":
                                    print("Imagine getting it wrong on the last question...")
                                    time.sleep(2)
                                    quit()
                                else:
                                    print("Wow! You are actually smart! Great job!")
                                    print("Since you won! I made something for you!")
                                    print("https://bit.ly/3T5eaj2")
                                    time.sleep(10)
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
