import win32api, win32con, win32gui
import os

#设置壁纸
def setWallPaper(imagepath='/pic/background.png'):
  keyex = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
  win32api.RegSetValueEx(keyex, "WallpaperStyle", 0, win32con.REG_SZ, "0")
  win32api.RegSetValueEx(keyex, "TileWallpaper", 0, win32con.REG_SZ, "0")
  win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, os.path.abspath('.') + imagepath, win32con.SPIF_SENDWININICHANGE)

setWallPaper()
