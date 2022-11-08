from tkinter import *
import tkinter.filedialog,os
from MyQR import myqr

print("generate QRcode\n")

name=input("What's the QRcode name: ")

content=input("What's the QRcode content: ")

color=input("Whether there is color(true or false): ")
if(str.lower(color)=="true"):
    color=1
else:
    color=0
    
print("Select background image: ",end="")
filename=filename=tkinter.filedialog.askopenfilename()
filename=filename.replace('/','\\')
if(filename==""):
    print("No background picture")
else:
    print(filename)

save=os.getcwd()
print(save)

myqr.run(
    words=content,
    picture=filename,
    colorized=bool(color),
    save_name=save+"\\"+name+".png"
)

print("\nQRcode generate success")
