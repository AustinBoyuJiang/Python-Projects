from tkinter import *
import tkinter.filedialog,os
from PIL import Image
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/len(ascii_char)
    return ascii_char[int(gray/unit)]
if __name__ == "__main__":
    filename=0
    print("选择图片: ",end="")
    while(filename==0):
        filename=tkinter.filedialog.askopenfilename()
    width = 80
    height = 40
    im = Image.open(filename)
    im = im.resize((width,height))
    txt = ''
    for i in range(height):
        for j in range(width):
            content = im.getpixel((j,i))
            txt += get_char(*content)
        txt = txt + '\n'
    f=open(os.getcwd()+"\\"+os.path.splitext(os.path.basename(filename))[0]+".txt","w")
    f.write(txt)
    f.close()
    print("已生成文件: ",os.path.splitext(os.path.basename(filename))[0]+".txt")
while(1):
    print("",end="")
