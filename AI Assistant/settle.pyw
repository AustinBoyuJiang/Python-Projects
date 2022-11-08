import tkinter,time,os,re
from translate import Translator
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.font import *
from tkinter import StringVar

def tran(word):
    translator= Translator(from_lang="chinese",to_lang=language)
    if(language!="chinese"):
        return translator.translate(word).replace("&#39;","'").replace("。",".")
    else:
        return word

def var(variable):
    global name,gender,master,inp,language
    spl = {"name":0,"gender":1,"master":2,"inp":3,"language":4}
    f = open(os.path.abspath(os.path.dirname(__file__))+"\\数据\\设置.txt","r")
    varlist = f.read().split("\n")
    if(variable == "all"):
        name = var("name")
        gender.set(var("gender"))
        master = var("master")
        inp.set(var("inp"))
        language = var("language")        
    else:
        return (varlist[spl[variable]].strip(" "))

def save():
    a = re.sub(r'[^\w\s]','',e1.get()).strip("")
    b = re.sub(r'[^\w\s]','',e3.get()).strip("")
    c = re.sub(r'[^\w\s]','',e5.get()).strip("")
    if(a=="" or b=="" or c==""):
        messagebox.showinfo(title=tran("提示"),message=tran("请输入有效信息"))
    elif(not(c in lang)):
        messagebox.showinfo(title=tran("提示"),message=tran("不存在使用语言"))
    else:
        f = open(os.path.abspath(os.path.dirname(__file__))+"\\数据\\设置.txt","w")
        f.write(a+"\n"+gender.get()+"\n"+b+"\n"+inp.get()+"\n"+c)
        f.close()
        messagebox.showinfo(title=tran("提示"),message=tran("保存设置成功\n重启程序生效"))
        exit()

def show2():
    global win,label,gender,inp,lang,e1,e3,e5
    win = tkinter.Tk()
    x = str(int(win.winfo_screenwidth()/2.5))
    y = str(int(win.winfo_screenheight()/3))
    win.geometry("+"+ x + "+" + y)
    gender = StringVar()
    inp = StringVar()
    var("all")
    win.resizable(width=False, height=False)
    win.geometry("360x240")
    win.configure(bg="#43454d")
    win.title(tran("语音助手")+"-"+tran("设置"))
    lang = ["chinese","english","french"]

    img = Image.open(os.path.abspath(os.path.dirname(__file__))+"\\素材\\按钮背景1.png")
    photo=ImageTk.PhotoImage(img)
    
    ft = Font(family="微软雅黑",size=1)
    tkinter.Label(win,bg="#43454d",fg="white",font=ft).grid(row=0)
    ft = Font(family="微软雅黑",size=12,weight=BOLD)
    tkinter.Label(win,bg="#43454d",fg="white",font=ft,text=20*" "+tran("设置")).grid(row=1, columnspan=3)
    ft = Font(family="微软雅黑",size=1)
    tkinter.Label(win,bg="#43454d",fg="white",font=ft).grid(row=2)
    ft = Font(family="微软雅黑",size=9)
    button = tkinter.Button(win,bd=0,activebackground="#43454d",bg="#43454d",image=photo,font=ft,text=tran("保存"),compound="center",command=save)

    ft = Font(family="微软雅黑",size=10)
    tkinter.Label(win,bg="#43454d",fg="white",font=ft,text="  "+tran("机器人名字")+":  ").grid(row=3,sticky="w")
    tkinter.Label(win,bg="#43454d",fg="white",font=ft,text="  "+tran("机器人性别")+":  ").grid(row=4,sticky="w")
    tkinter.Label(win,bg="#43454d",fg="white",font=ft,text="  "+tran("你的名字")+":  ").grid(row=5,sticky="w")
    tkinter.Label(win,bg="#43454d",fg="white",font=ft,text="  "+tran("输入方式")+":  ").grid(row=6,sticky="w")
    tkinter.Label(win,bg="#43454d",fg="white",font=ft,text="  "+tran("使用语言")+":  ").grid(row=7,sticky="w")

    con1 = StringVar()
    con2 = StringVar()
    con3 = StringVar()
    ft = Font(family="微软雅黑",size=9)
    e1 = tkinter.Entry(win,textvariable=con1,width="25")
    e2 = tkinter.Label(win,bg="#43454d",fg="#43454d",text="  ")
    c1 = tkinter.Radiobutton(win, activebackground="#43454d", bg="#43454d", image=photo, text = tran("男生"), compound="center", font=ft, variable = gender,value = "男")
    c2 = tkinter.Radiobutton(win, activebackground="#43454d", bg="#43454d", image=photo, text = tran("女生"), compound="center", font=ft, variable = gender,value = "女")
    e3 = tkinter.Entry(win,textvariable=con2,width="25")
    e4 = tkinter.Label(win,bg="#43454d",fg="#43454d",text="  ")
    c3 = tkinter.Radiobutton(win, activebackground="#43454d", bg="#43454d", image=photo, text = tran("语音"), compound="center", font=ft, variable = inp,value = "语音")
    c4 = tkinter.Radiobutton(win, activebackground="#43454d", bg="#43454d", image=photo, text = tran("打字"), compound="center", font=ft, variable = inp,value = "打字")
    e5 = tkinter.Entry(win,textvariable=con3,width="25")
    con1.set(name)
    con2.set(master)
    con3.set(language)

    button.grid(row=1, column=3, columnspan=3, sticky="w")
    e1.grid(row=3, column=1, columnspan=3, sticky="w")
    c1.grid(row=4, column=1, sticky="w")
    e2.grid(row=4, column=2, sticky="w")
    c2.grid(row=4, column=3, columnspan=3, sticky="w")
    e3.grid(row=5, column=1, columnspan=3, sticky="w")
    c3.grid(row=6, column=1, sticky="w")
    e4.grid(row=6, column=2, sticky="w")
    c4.grid(row=6, column=3, columnspan=3, sticky="w")
    e5.grid(row=7, column=1, columnspan=3, sticky="w")

    win.mainloop()
    
show2()
