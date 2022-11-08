from PIL import ImageGrab
import win32api,win32con,winreg,sys,os

def get_desktop():
    DeskTop = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'
    return DeskTop

def get_name():
    n = 1
    while(os.path.exists(get_desktop()+"截图"+str(n)+".png")):
        n = n+1
    return get_desktop()+"截图"+str(n)+".png"

def screenshots():
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    bbox = (0, 0, x, y)
    im = ImageGrab.grab(bbox)
    name = get_name()
    im.save(name)
    win32api.ShellExecute(0, "open",name,"","", 1)
