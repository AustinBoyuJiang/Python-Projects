import os,time
import win32gui
import win32con
import win32clipboard as w

def send(name,msg):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
    handle = win32gui.FindWindow(None, name)
    win32gui.SendMessage(handle, 770, 0, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.1)

name=input('轰炸对象: ')
message=input('轰炸内容: ')
n=int(input('轰炸次数: '))
for i in range(n):
    send(name,message+str(i+1))
    print("第"+str(i+1)+"遍已发送")
input(str(n)+"遍轰炸结束")
os.sys("cls")
