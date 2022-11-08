import random,os

a=dict()
aw=dict()

def addword():
    n=str(input("请输入这个单词:"))
    x=str(input("请输入中文意思:"))
    a[n]=x
    aw[x]=n

def showall():
    if len(a)>=1:
        for i in a:
            print(i+": "+a[i])
    else:
        print("未收录单词")

def show():
    print("1.所有单词")
    print("2.添加单词")
    print("3.搜索单词")

def specialword():
    n = input("请输入这个单词:")
    if n in a.keys():
        print(a.get(n))
    else:
        if n in aw.keys():
            print(aw.get(n))
        else:
            print("没有这个单词")
            addword()

while(1):
    os.system("cls")
    show()
    x=input("\n请选择序号:")
    if x=='1':
        showall()
    elif x=='2':
        addword()
    elif x=='3':
        specialword()
    else:
        print("输入有误")
    input("\n回车继续")
