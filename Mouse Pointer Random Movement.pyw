import win32api,win32con,random,time
length = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

for i in range(1000):
    time.sleep(0.01)
    x = random.randint(0,length)
    y = random.randint(0,height)
    win32api.SetCursorPos((x, y))
