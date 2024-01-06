#importing the required libraries
import tkinter as tk
from tkinter import *
import recorder as rec

#initialising running as None
running = None

#writing the start and stop functions
def start():
    global running
    if running is not None:
        print("Already Running")
    else:
        running=rec.open('untitled.flac','wb')
        running.start_recording()

    Label(window,text='Recording has started').pack()

def stop():
    global running

    if running is not None:
        running.stop_recording()
        running.close()
        running=None
        Label(window,text='Recording has stopped').pack()
    else:
        print("It is not running")
#creating the required GUI Window
window=Tk()
window.geometry('900x900')
window.title('Voice Recorder')
Label(window,text="Click on START to start recording",font=('bold',25)).pack()

#creating required buttons
Button(window,text='START',bg='green',command=start,font=('bold',25)).pack()
Button(window,text='STOP',bg='red',command=stop,font=('bold',25)).pack()
window.mainloop()


        
