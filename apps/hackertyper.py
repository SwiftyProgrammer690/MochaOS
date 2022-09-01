"""
Importing time
Importing Sys
Importing os
"""
import time
import sys
import os

# Clears screen + disclaimer
os.system('clear')

# Pretty typing animation
def printf(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

# The "fake" hacking code
code = [
    "#include <iostream>\n",
    "#include <cmath>\n",
    "\n",
    "int main() {\n",
    "   std::cout << 'Hacking mainframe...';\n",
    "   float hackMainframe();\n"
    "   return 0;\n"
    "}\n",
    "\n",
    "class hackMainframe {\n",
    "   float bits[] = 63.9;\n",
    "   public:\n",
    "       hackMainframe() {\n",
    "           float bits[]++ on run; \n",
    "       };\n",
    "};\n"
]

def fake_hack():
    for arr in range(14):
        printf(code[arr])
        arr += 1

# printf(code[0] + code[1] + code[2] + code[3] + code[4] + code[5])
inputHack = input(" ")
if inputHack == "h":
    os.system('clear')
    print(fake_hack())
else:
    quit()
