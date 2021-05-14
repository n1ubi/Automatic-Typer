import os
import pyautogui
import time
import win32gui
import win32con
import keyboard
import random


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
    # Press F3 to make it type.
    choice = input('\n\u001b[31m>\u001b[37m ')
    if "1" in choice:
            keyboard.wait('f3')
            print(random.choice(randomText))
            print("This one has a bit of issues. They will be fixed at somepoint.")

    if "2" in choice:
        text = input('\n\u001b[31m>\u001b[37m Text\u001b[31m:\u001b[37m ')
        keyboard.wait('f3')
        Typer(text)
        exit()
        
    if "3" in choice:
        text = input('\n\u001b[31m>\u001b[37m Text\u001b[31m:\u001b[37m ')
        keyboard.wait("f3")
        while True:
            Typer(text)
        # Failsafe feature, press F2 or ESC to make it stop.
        if keyboard.is_pressed('f2'):
            print('You pressed F2.\n')
            print('Exiting.')
            exit()
        if keyboard.is_pressed('esc'):
            exit()

    else:
        print('[\u001b[31m!\u001b[37m] Invalid Option.')
        exit()

