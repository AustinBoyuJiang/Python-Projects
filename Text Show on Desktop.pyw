#导入库
from tkinter.font import *
import tkinter as tk
import _thread
import time

def backgroundColor(co):
    color=str.lower(co)
    colorValue=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    if(colorValue.index(color[6])==15):
        a=14
    else:
        a=colorValue.index(color[6])+1
    return "#"+color[1]+color[2]+color[3]+color[4]+color[5]+colorValue[a]

def init(message):
    global n
    n = 1
    _thread.start_new_thread(window,(message,))
    time.sleep(0.5)

def window(message):
    global label,win1,x,y,ab
    ab=message
    color=message["color"]
    win1 = tk.Tk()
    win1.wm_attributes("-topmost", True)
    win1.overrideredirect(True)
    win1.attributes("-transparentcolor",color)
    ft = Font(family="微软雅黑", size= message["size"], weight=BOLD)
    label = tk.Label(win1, bg=color, font=ft, fg = backgroundColor(color))
    label.pack()
    screen_width = win1.winfo_screenwidth()
    screen_height = win1.winfo_screenheight()
    x = str(int(screen_width/2))
    y = str(int(screen_height/2.2))
    win1.geometry("+"+ x + "+" + y)
    win1.mainloop()

def display(word):
    global n,ab
    label.config(text=word)
    win1.geometry("+"+ str(int(x)-len(word)*int(ab["size"]/2)) + "+" + str(int(y)-ab["size"]))
    n=n+1

def close():
    win1.destroy()

init({"color":"#00aaff" , "size":30})
display("你好")
time.sleep(2)
display("我是你爸爸")
time.sleep(2)
close()
exit()
