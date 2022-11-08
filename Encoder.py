import pinyin,os,re
string = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while(1):
    os.system("cls")
    password = pinyin.get(str(input("请输入密码: ")),format='strip')
    new = ""
    for i in password:
        try:
            new = new+str.lower(string[int((string.index(str.lower(i))+len(string)/2)%len(string))])
        except:
            new = new+"-"
    print("结果: "+new)
    input("\n[Enter]继续")
