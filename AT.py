import os
import pyautogui
import win32gui
import win32con
import keyboard
import random
# ^^^ requirements

count = 0 # for looping 


#                        vvv  Read this vvv
 # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv #
 # Check the entire code and you can clear the comments if you want.     #
 # Also you should read the README.md file.                              #
 # Feel free to modify the code, but please don't claim it as your own.  #
 # You should check the all the lines on from 55 to 96.                  #
 # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #



randomTexts = [
    "veri good text 123",
    "Why u select this?? u nob idiot :((",
    "Hello, i like men.",
    "This text is really random, btw.",
    "I like snakes.",
    "Python > all."
]


hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,500,200,0)




def Typer(text):
    try:
        print('\n[\u001b[31m!\u001b[37m] Typing')
        pyautogui.write(text, interval=0.0)
    except Exception:
        print('\n[\u001b[31m!\u001b[37m] Stopped')
        os.system('pause >NUL')
    except pyautogui.FailSafeException:
       print('\n[\u001b[31m!\u001b[37m] Safety Feature, Your Cursor Was At The Corner Of The Screen')
       os.system('pause >NUL') 
    

if __name__ == "__main__":
    os.system('cls & title [Automatic Typer] made in Python')
    print(
        '[\u001b[31m1\u001b[37m] Random',
        '\n[\u001b[31m2\u001b[37m] Manual Text',
        '\n[\u001b[31m3\u001b[37m] Manual Looped'  
    )

    # Typing modes: 1 = "random" text, 2 = Manual text, but only one time and 3 = Manual text, but looped
    # Mode 1
    choice = input('\n\u001b[31m>\u001b[37m ')
    if "1" in choice:
            keyboard.wait('f3')
            print(random.choice(randomText))
            print("This one has a bit of issues. They will be fixed at somepoint.")

    # Mode 2
    if "2" in choice:
        text = input('\n\u001b[31m>\u001b[37m Text\u001b[31m:\u001b[37m ')
        keyboard.wait('f3')
        Typer(text)
        exit()

    # Mode 3    
    if "3" in choice:
        text = input('\n\u001b[31m>\u001b[37m Text\u001b[31m:\u001b[37m ')
        keyboard.wait("f3")
         # "while True:" repeats itself endlessly and "while count > <value>:" repeats itself <value> times. 
         # Example: while count > 10: repeats itself 10 times.
        while True:
        #while count > 10: This one has issues, don't use it.
            Typer(text)
            count = count + 1 

            # Checks if F2 or ESC is pressed. (actually functions correctly, i'm surprised, like no fucking way, 
            # you have no idea how much time i spent on this.)
            if keyboard.is_pressed('f2'):
               print('You pressed F2.\n')
               print('Exiting.')
               exit()
            if keyboard.is_pressed('esc'):
               print('You pressed ESC.\n')
               print('Exiting.')
               exit() 
           
    # Prints this if you can't type numbers, lmao.
    else:
        print('[\u001b[31m!\u001b[37m] Invalid Option.')
        exit()
