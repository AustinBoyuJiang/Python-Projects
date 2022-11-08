import tkinter,os
from translate import Translator
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter.font import *

def tran(word):
    language = var("language")
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
        gender = var("gender")
        master = var("master")
        inp = var("inp")
        language = var("language")        
    else:
        return (varlist[spl[variable]].strip(" "))

def change1():
    win.title(tran("语音助手")+"-"+tran("软件介绍"))
    tit.set(26*" "+tran("软件介绍"))
    T.config(state="normal")
    T.delete("1.0","end")
    T.insert("end",fic1)
    T.config(state="disabled")

def change2():
    win.title(tran("语音助手")+"-"+tran("软件开发"))
    tit.set(26*" "+tran("软件开发"))
    T.config(state="normal")
    T.delete("1.0","end")
    T.insert("end",fic2)
    T.config(state="disabled")

def change3():
    win.title(tran("语音助手")+"-"+tran("注意事项"))
    tit.set(26*" "+tran("注意事项"))
    T.config(state="normal")
    T.delete("1.0","end")
    T.insert("end",fic3)
    T.config(state="disabled")

def show1():
    global win,label,lang,tit,e1,e3,e5,T,fic1,fic2,fic3
    f1 = open(os.path.abspath(os.path.dirname(__file__))+"\\数据\\软件介绍.txt","r")
    fic1 = tran(f1.read())
    f1.close()
    f2 = open(os.path.abspath(os.path.dirname(__file__))+"\\数据\\软件开发.txt","r")
    fic2 = tran(f2.read())
    f2.close()
    f3 = open(os.path.abspath(os.path.dirname(__file__))+"\\数据\\注意事项.txt","r")
    fic3 = tran(f3.read())
    f3.close()

    win = tkinter.Tk()
    x = str(int(win.winfo_screenwidth()/3.2))
    y = str(int(win.winfo_screenheight()/4))
    win.geometry("+"+ x + "+" + y)
    win.resizable(width=False, height=False)
    win.geometry("700x450")
    win.configure(bg="#43454d")
    win.title(tran("语音助手")+"-"+tran("软件介绍"))

    img = Image.open(os.path.abspath(os.path.dirname(__file__))+"\\素材\\图标\\介绍图标.png")
    photo=ImageTk.PhotoImage(img)
    img = Image.open(os.path.abspath(os.path.dirname(__file__))+"\\素材\\按钮背景2.png")
    photo2=ImageTk.PhotoImage(img)
    
    ft = Font(family="微软雅黑",size=1)
    tkinter.Label(win,bg="#43454d",fg="white",font=ft).grid(row=0)
    ft = Font(family="微软雅黑",size=20,weight=BOLD)
    tit = StringVar()
    titl=tkinter.Label(win,bg="#43454d",fg="white",font=ft,textvariable=tit)
    titl.grid(row=1,columnspan=100)
    tit.set(26*" "+tran("软件介绍"))
    
    sft = Font(family="微软雅黑",size=0)    
    tkinter.Label(win,bg="#43454d",text="    ").grid(row=3,column=1)
    tkinter.Label(win,bg="#43454d",image=photo).grid(row=3,column=2)

    sft = Font(family="微软雅黑",size=1)
    tkinter.Label(win,bg="#43454d",fg="white",font=sft,text=15*"\n").grid(row=4)
    ft = Font(family="微软雅黑",size=15)
    tkinter.Label(win,bg="#43454d",fg="white",font=ft,text="— "+tran("语音助手")+" —").grid(row=4,column=2)
    sft = Font(family="微软雅黑",size=1)
    tkinter.Label(win,bg="#43454d",fg="white",font=sft,text=5*"\n").grid(row=5)
    ft = Font(family="微软雅黑",size=10)
    button1 = tkinter.Button(win,bd=0,activebackground="#43454d",bg="#43454d",fg="black",image=photo2,font=ft,text=tran("软件介绍"),command=change1,compound="center")
    button1.grid(row=6,column=2)
    tkinter.Label(win,bg="#43454d",fg="white",font=sft).grid(row=7)
    button1 = tkinter.Button(win,bd=0,activebackground="#43454d",bg="#43454d",fg="black",image=photo2,font=ft,text=tran("软件开发"),command=change2,compound="center")
    button1.grid(row=8,column=2)
    tkinter.Label(win,bg="#43454d",fg="white",font=sft).grid(row=9)
    button1 = tkinter.Button(win,bd=0,activebackground="#43454d",bg="#43454d",fg="black",image=photo2,font=ft,text=tran("注意事项"),command=change3,compound="center")
    button1.grid(row=10,column=2)
    tkinter.Label(win,bg="#43454d",fg="white",font=sft,text=3*"\n").grid(row=11)
    
    ft = Font(family="微软雅黑",size=12)    
    tkinter.Label(win,bg="#43454d",text=10*" ").grid(row=2,column=3,rowspan=100)
    T = tkinter.Text(win,bd=0,font=ft,bg="#43454d",fg="white",height=12,width=35)
    T.grid(row=2,column=4,rowspan=100,columnspan=100)
    T.insert("end",fic1)
    T.config(state="disabled")

    win.mainloop()
    
show1()
