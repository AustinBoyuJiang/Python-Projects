import os,tkinter
from tkinter import messagebox
content="空文件"
name="系统文件"
serial=0
suffix ="txt"
n=100
for i in range(n):
    file=name+str(serial+1)+"."+suffix
    try:
        f=open(file,"x")
        f=open(file,"w") 
        f.write(content)
        f=open(file,"r")
        print("生成文件成功")
        print("文件名："+file)
        print("文件内容：")
        print(f.read()+"\n")
        f.close()
    except BaseException:
        print("已存在该文件名\n错误文件："+file+"\n")
    serial=serial+1
    
tkinter.messagebox.showinfo(title='系统提示', message='恢复系统文件完成')
