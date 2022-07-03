print("""\n
https://github.com/TsuomiLOL/autoclick\n
! ! ! WARNING ! ! !\n
If it's wrong on Linux, download python3-tkinter\n
Arch Linux: sudo pacman -S tk\n
Debian: sudo apt install python3-tk python3-dev\n\n\n
""")

import pyautogui
import threading
import time

print("Ctrl + C to close\nWait . . .")

time.sleep(4)

while True:
    pyautogui.click()

