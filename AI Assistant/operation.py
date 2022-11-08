import datetime,win32api,weather,search,note,time,os
from screenshots import screenshots
from translate import Translator
from translat import translat
from ctypes import *
from audio import *

def timeNow():
    week = {"Mon":"星期一","Tues":"星期二","Wed":"星期三","Thu":"星期四","Fri":"星期五","Sat":"星期六","Sun":"星期日"}
    return (time.strftime("%Y")+"年"+time.strftime("%m")+"月"+time.strftime("%d")+"日 "+week[time.strftime("%a")]+time.strftime(" %H")+":"+time.strftime("%M")+":"+time.strftime("%S"))

def tran(word):
    global lan
    translator= Translator(from_lang="chinese",to_lang=lan)
    translation = translator.translate(word)
    return translation
    
def operation(mes,name,gender,master,language,n):
    global lan
    lan = language
    translator= Translator(from_lang=lan,to_lang="chinese")
    message = translator.translate(mes)
    if(message=="" or message==tran(" 输入内容")):
        return "我没有听清楚"
    elif("翻译" in message):
        message = message.strip("翻译")
        if(message == ""):
            return "翻译什么"
        else:
            return "翻译结果为"+translat(message.strip(translat("language","chinese")),lan)
    elif("搜" in  message or "查" in  message):
        return (search.search(message.strip("搜索").strip("查找").strip("查询").strip("搜").strip("查")))
    elif("天气" in message or "气象" in message or "温度" in message or "气温" in message):
        message=message.strip(name).strip("天气").strip("今天").strip("最近").strip("的").strip("现在").strip("情况").strip("信息").strip("查看").strip("获得").strip("气象").strip("是").strip("怎么样").strip("温度").strip("气温").strip("什么").strip("？").strip("?").strip(",").strip("，").strip("。").strip(".").strip("(").strip(")").strip("（").strip("）")
        if(message!=""):
            wea=weather.weather(message,language)
            if(wea!=None):
                print(tran("今天"+message+"天气:"))
                return weather.output(wea)
            else:
                return "没有收录该地区"
        else:
            return "我不知道你指哪里的天气"
    elif("设置" in message):
        win32api.ShellExecute(0, "open",os.path.abspath(os.path.dirname(__file__))+"\\settle.pyw","","", 1)
        return "已为你打开设置"
    elif("介绍" in message or "开发" in message or "注意" in message):
        win32api.ShellExecute(0, "open",os.path.abspath(os.path.dirname(__file__))+"\\introduce.pyw","","", 1)
        return "已为你打开介绍"
    elif("计算" in message or "算数" in message):
        os.system("calc")
        return "已为你打开计算器"
    elif("记事本" in message):
        note.openNote()
        return "已为你打开记事本"
    elif("截屏" in message or "截图" in message):
        screenshots()
        return "已为你截屏"
    elif("时间" in message or "几点了" in message or "日期" in message or "星期" in message):
        return "现在时间是 "+timeNow()
    elif("电影" in message or "电视" in message or "视频" in message or "连续剧" in message or "剧集" in message or "追剧" in message or "综艺" in message or "动画" in message or "动漫" in message):
        win32api.ShellExecute(0, "open","https://www.youtube.com","","", 1)
        return "已为你打开YouTube"
    elif("资讯" in message or "新闻" in message):
        win32api.ShellExecute(0, "open","https://news.google.com/","","", 1)
        return "已为你打开Google新闻"
    elif(message=="关机" or message=="电脑关机"):
        print(tran("正在关机"))
        speak("Audio"+str(n),tran("正在关机"),gender)
        os.system("shutdown -s -t 00")
        return 0
    elif(message=="重启" or message=="电脑重启" or message=="重启电脑"):
        print(tran("正在重启"))
        speak("Audio"+str(n),tran("正在重启"),gender)
        os.system("shutdown -r -t 00")
        return 0
    elif(message=="锁屏" or message=="电脑锁屏"):
        print(tran("正在锁屏"))
        speak("Audio"+str(n),"正在锁屏",gender)
        user32 = windll.LoadLibrary('user32.dll')
        user32.LockWorkStation()
        return 0
    elif(message=="退出程序" or message=="程序退出" or message=="关闭程序" or message=="程序关闭" or message=="退出" or message=="关闭"):
        print(tran("正在退出"))
        speak("Audio"+str(n),tran("正在退出"),gender)
        exit()
    elif(("用处" in message or "功能" in message or "干什么" in message or "干嘛" in message or "做什么" in message) and "你" in message):
        return "我可以聊天,翻译\n搜索,看天气等"
    elif(name in message):
        return "你是在找我吗"
    elif(master in message and ("我" in message or "名字" in message or "姓名" in message)):
        return ("巧了，我的主人也叫"+master)
    elif(master in message):
        return (master+"是我的主人")
    elif("主人" in message):
        return ("我的主人是"+master+"呀")
    elif("创造" in message or "制造" in message or "创造人" in message or "制作人" in message or "作者" in message):
        return "我是蒋博羽创造的"
    elif(("年龄" in message or "岁" in message or "出生" in message or "诞生" in message)and(not("我" in message) or "你" in message)):
        return ("我"+str(datetime.datetime.now().year-2019+1)+"岁了")
    elif("你" in message and  "女朋友" in message):
        if(gender == "男"):
            return "我没有女朋友"
        else:
            return "我是女生,不需要女朋友"
    elif("你" in message and  "男朋友" in message):
        if(gender == "女"):
            return "我没有男朋友"
        else:
            return "我是男生,不需要男朋友"
    elif(("性别" in message or ("男" in message or "女" in message)) and "你" in message and not( "我" in message )):
        return ("我是"+gender+"生")
    elif(("我" in message and "你" in message)and("爸" in message or "妈" in message or "儿子" in message or "女儿" in message)):
        return "我只是你的助手吧"
