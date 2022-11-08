from tkinter import *
import tkinter.filedialog,os
from MyQR import myqr

print("二维码生成")
text=input()



filename=0
print("选择图片: ",end="")
while(filename==0):
    filename=tkinter.filedialog.askopenfilename()
    
myqr.run(
    words='https://www.baidu.com',
    picture=filename,
    colorized=True,
    save_name='animated.gif'
)
