#导入库
import win32api,keyboard,threading,tkinter,aiml,time,sys,os,re
from translate import Translator
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter.font import *
from operation import *
from ctypes import *
from audio import *

#翻译
def tran(word):
    global language
    translator= Translator(from_lang="chinese",to_lang=language)
    if(language!="chinese"):
        return translator.translate(word).replace("&#39;","'").replace("。",".")
    else:
        return word

#获取变量
def var(variable):
    global name,gender,master,inp,language
    spl = {"name":0,"gender":1,"master":2,"inp":3,"language":4}
    f = open(os.path.abspath(os.path.dirname(__file__))+"\\数据\\设置.txt","r")
    varlist = f.read().split("\n")
    f.close()
    if(variable == "all"):
        name = var("name")
        gender = var("gender")
        master = var("master")
        inp = var("inp")
        language = var("language")        
    else:
        return (varlist[spl[variable]].strip(" "))

#按钮执行
def  go():
    global winwait,content
    winwait = 1

#修改窗口内容
def change(word):
    if(end == "结束"):
        exit()
    label.config(text="\n "+str(word)+" \n")

#打开窗口
def show():
    global label,enter,win,content,end
    end = 0
    win = tkinter.Tk()
    x = str(int(win.winfo_screenwidth()/2.35))
    y = str(int(win.winfo_screenheight()/2.8))
    win.geometry("+"+ x + "+" + y)
    win.configure(bg="#43454d")
    win.configure()
    win.resizable(width=False, height=False)
    win.title(tran("语音助手"))
    ft = Font(family="微软雅黑",size=10,weight=BOLD)
    label = tkinter.Label(win,bg="#43454d",fg="white",font=ft,text="\n"+tran("正在加载")+"...\n")
    label.pack()
    content = StringVar()
    ft = Font(family="微软雅黑",size=10)
    enter=tkinter.Entry(win,font=ft,bg="white",textvariable=content)
    content.set(tran(" 输入内容"))
    enter.pack()
    space = tkinter.Label(win,bg="#43454d").pack()
    ft = Font(family="微软雅黑",size=10)
    img = Image.open(os.path.abspath(os.path.dirname(__file__))+"\\素材\\按钮背景1.png")
    photo=ImageTk.PhotoImage(img)
    button=tkinter.Button(win,bd=0,activebackground="#43454d",bg="#43454d",image=photo,font=ft,text=tran("发送"),compound="center",padx=8,pady=-5,command=go)
    button.pack()
    label1 = tkinter.Label(win,bg="#43454d",text=70*" ").pack()
    win.mainloop()
    end = "结束"
    return 0

#加载
def get_module_dir(name):
    print("module", sys.modules[name])
    path = getattr(sys.modules[name], '__file__', None)
    print(path)
    if not path:
        raise AttributeError('module %s has not attribute __file__' % name)
    return os.path.dirname(os.path.abspath(path))

#初始化
def initialize():
    global name,gender,master,inp,rou,language,alice,n
    var("all")
    thread = threading.Thread(target=show, args=())
    thread.daemon = True
    thread.start()
    print(tran("正在加载..."))
    alice_path = get_module_dir('aiml') + '\\botdata\\alice'
    os.chdir(alice_path)
    alice = aiml.Kernel()
    alice.learn("startup.xml") 
    alice.respond('LOAD ALICE')
    print(tran("加载完毕"))
    print(tran("正在启动人工智能")+"\n")
    time.sleep(0.5)
    n = 0
    print(tran("你好")+","+tran("我是"+name))
    change(tran("你好")+","+tran("我是"+name))
    try:
        speak("start",tran("你好，我是"+name),gender)
    except Exception as e:
        print(tran("出了点小问题"))
        change("出了点小问题")
        print(tran("错误类型")+": "+str(e))
        time.sleep(2)
        exit()

#聊天
def chat():
    global name,gender,master,inp,language,rou,alice,n,winwait,end
    print("")
    n=n+1
    if(inp=="语音"):
        aw = rouse(name)
        print(tran(aw)+"\n")
        speak("Audio"+str(n),tran(aw),gender)
        n=n+1
    else:
        winwait = 0
        while(winwait == 0 or end == "结束"):
            pass
        if(end == "结束"):
            exit()
        message = re.sub(r'[^\w\s]','',enter.get())
        content.set(tran(" 输入内容"))
        enter.icursor (5)
        change("正在处理...")
        print(tran("文字输入")+">> "+message)
    try:
        choise = operation(message.strip("嘿").strip("HI").strip("Hi").strip("hi").strip(name),name,gender,master,language,n)
        if(choise == None):
            translator= Translator(from_lang=language,to_lang="english")
            message = translator.translate(message)
            response = alice.respond(message)
            response = str(response)
            translator= Translator(to_lang="chinese")
            response = translator.translate(response)
            print(tran(response.replace("无名",name)))
            change(tran(response.replace("无名",name)))
            speak("Audio"+str(n),tran(response.replace("无名",name)),gender)
        elif(choise!=0):
            choise = str(choise)
            if("翻译结果为" in choise):
                print(tran("翻译结果为")+" \""+choise.strip("翻译结果为")+"\"")
                change(tran("翻译结果为")+" \""+choise.strip("翻译结果为")+"\"")
                speak("Audio"+str(n),tran("翻译结果为")+choise.strip("翻译结果为"),gender)
            else:
                if(tran("天气情况") in choise):
                    change(tran("正在为你播报天气"))
                    speak("Audio"+str(n),tran(choise),gender)
                    change(tran("已为你播报天气"))
                else:
                    print(tran(choise))
                    change(tran(choise))
                    speak("Audio"+str(n),tran(choise.replace("、",",").replace("\n",",")),gender)
    except Exception as e:
        n=n+1
        print(tran("出了点小问题"))
        print(tran("错误类型")+": "+str(e))
        change(tran("出了点小问题"))
        speak("Audio"+str(n),tran("出了点小问题"),gender)

#主函数
def main():
    if(var("master").strip("") == ""):
        import word
        word.display("你好，我是你的语音助手")
        word.display("初次见面，先看看一些我的介绍吧")
        win32api.ShellExecute(0, "open",os.path.abspath(os.path.dirname(__file__))+"\\introduce.pyw","","", 1)
        time.sleep(5)
        word.display("你还需要告诉我你的名字")
        win32api.ShellExecute(0, "open",os.path.abspath(os.path.dirname(__file__))+"\\settle.pyw","","", 1)
        time.sleep(3)
        word.display("再次点开我就可以聊天啦")
        exit()
    else:
        initialize()
        while(1):
            if(end == "结束"):
                exit()
            chat()

main()
