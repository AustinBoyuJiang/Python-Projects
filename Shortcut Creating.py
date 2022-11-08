from os import path  
import winshell  
 
def create_shortcut_to_desktop(target):
    s = path.basename(target)  
    fname = path.splitext(s)[0]  
    winshell.CreateShortcut(  
    Path = path.join(winshell.desktop(), fname + '.lnk'),  
    Target = target,  
    Icon=(target, 0))

create_shortcut_to_desktop(__file__)
