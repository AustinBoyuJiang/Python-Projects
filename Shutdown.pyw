import win32api,win32con

def put(x1,y1):
    x = int(x1)
    y = int(y1)
    for i in range(100000):
        win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    for i in range(100000):
        win32api.SetCursorPos((x, y))

length = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

put(length*0.015,height*0.98)
put(length*0.015,height*0.935)
put(length*0.015,height*0.85)
