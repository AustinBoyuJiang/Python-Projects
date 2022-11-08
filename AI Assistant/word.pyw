#导入库
from tkinter.font import *
import tkinter as tk
import _thread
import time
import audio

def init():
    global n
    n = 1
    _thread.start_new_thread(window,())
    time.sleep(0.5)

def window():
    global label,win1,x,y
    win1 = tk.Tk()
    win1.wm_attributes("-topmost", True)
    win1.overrideredirect(True)
    win1.attributes("-transparentcolor","#10ccff")
    ft = Font(family="微软雅黑", size= 30, weight=BOLD)
    label = tk.Label(win1, bg="#10ccff", font=ft, fg = "#00ccff")
    label.pack()
    screen_width = win1.winfo_screenwidth()
    screen_height = win1.winfo_screenheight()
    x = str(int(screen_width/2))
    y = str(int(screen_height/2.2))
    win1.geometry("+"+ x + "+" + y)
    win1.mainloop()

def display(word):
    global n
    label.config(text=word)
    win1.geometry("+"+ str(int(x)-len(word)*25) + "+" + y)
    audio.speak("introduce"+str(n),word,"女")
    n = n+1

def close():
    win1.destroy()

init()
