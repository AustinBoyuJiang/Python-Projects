from ctypes import *
while True:

        user32 = windll.LoadLibrary('user32.dll')

        user32.LockWorkStation()
