import pinyin,os,re

def find(content):
    for i in string:
        if(string[i] == content):
            return i
    return ""

string = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","k":"-.-","l":".---","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}

while(1):
    os.system("cls")
    print("1. 英文转摩斯密码")
    print("2. 摩斯密码转英文")
    print("3. 退出程序")
    choise = input("\n请选择序号: ")
    os.system("cls")
    if(choise == "1"): 
        password = (str.lower(pinyin.get(re.sub(r'[^\w\s]','',str(input("输入英文字母: "))),format="strip"))).replace(" ","")
        new = ""
        try:
            for i in range(len(password)):
                if(i != len(password)-1):
                    new = new+string[password[i]]+" "
                else:
                    new = new+string[password[i]]
        except:
            new = "只能出现字母和数字"
        print("结果: "+new)
        input("\n[Enter]程序继续")        
    elif(choise == "2"):
        password = str(input("输入摩斯密码: "))
        password = password.split(" ")
        new = ""
        try:
            for i in password:
                    new = new+find(i)
        except:
            new = "请用空格分开"
        print("结果: "+new)
        input("\n[Enter]程序继续")
    elif(choise == "3"):
        input("[Enter]退出程序")
        exit()
    else:
        print("不存在该选项")
        input("\n[Enter]程序继续")
