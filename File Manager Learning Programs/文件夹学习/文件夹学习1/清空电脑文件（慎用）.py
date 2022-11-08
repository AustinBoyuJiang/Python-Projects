import os,shutil,sys,time,tkinter
from tkinter import messagebox

jur=1
n=0
path=os.getcwd()
self=os.path.basename(sys.argv[0])
oldsite=path+"\\"+self
desktop="C:\\Users\\Administrator\\Desktop"
c="C:"
d="D:"
e="E:"
f="F:"

while(1):
        print("当前目录：",path)
        newsite=input("请输入清除地址(C盘、D盘、E盘、F盘、桌面、当前目录、自定义)：")
        print("")
        if(newsite=="C盘"):
            if(jur==0):
                newsite=c
                break
            else:
                print("你没有权限\n")
        elif(newsite=="D盘"):
            if(jur==0):
                newsite=d
                break
            else:
                print("你没有权限\n")
        elif(newsite=="E盘"):
            if(jur==0):
                newsite=e
                break
            else:
                    print("你没有权限\n")
        elif(newsite=="F盘"):
            if(jur==0):
                newsite=f
                break
            else:
                    print("你没有权限\n")
        elif(newsite=="桌面"):
            if(jur==0):
                newsite=desktop
                break
            else:
                print("你没有权限\n")
        elif(newsite=="自定义"):
            if(jur==0):
                newsite=input("请输入自定义地址：")
                break
            else:
                print("你没有权限\n")
        elif(newsite=="当前目录"):
            if(jur==0):
                break
            else:
                print("你没有权限\n")
        else:
            print("请输入正确的回复")

y=input(('请确认指令删除 '+newsite+' 所有文件(是/否)：'))
if(y=="是"):
    try:
        if(newsite!="当前目录"):
            path=newsite
            shutil.move(oldsite,newsite)
            print("\n移动成功")
            os.chdir(newsite)
    except BaseException:
        print("不存在该目录")
        
    file_name=os.listdir(path)
    for i in range (len(file_name)):
        file=file_name[n]
            
        if (file != self):
            if os.path.isdir(file):
                print("\n删除文件夹成功")
                print("文件夹名：",file)
                print("文件夹地址：",path)
                shutil.rmtree(file)
            else:
                f=open(file,"w")
                f.write("")
                f.close()
                print("删除文件成功")
                print("文件名：",file)
                print("文件地址：",path,"\n")
                os.remove(file)
        else:
            print("已自动跳过程序本身")
            print("文件名：",file)
            print("文件地址：",path,"\n")
                
        n=n+1
    
if(n==1):
    print("未发现其他文件\n")
    tkinter.messagebox.showwarning(title='提示', message="未发现其他文件")
else:
    print("所有文件删除成功")
    tkinter.messagebox.showwarning(title='提示', message="文件删除成功")

t=5
for i in range(t):
        print(t,"秒后程序自动关闭")
        time.sleep(1)
        t=t-1
