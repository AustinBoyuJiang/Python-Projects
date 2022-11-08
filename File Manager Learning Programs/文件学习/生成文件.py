import os
while(1):
    pr=["哈哈哈","被骗啦","气不气","又多了","空文件","别看了","真没了","不说了","==========再见=========="]
    name="生成文件"
    serial=0
    suffix ="txt"
    while(1):
        try:
            n=int(input("生成文件数量："))
        except BaseException:
            print("请输入正确类型\n")
        else:
            print("")
            break
    for i in range(n):
        file=name+str(serial+1)+"."+suffix
        if(serial < 9):
            content=pr[serial]
        else:
            content=pr[8]
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
