import os,sys,time
path = os.getcwd()
file_name=os.listdir(path)
n=0
s=0
print("警告：即将修改该目录下所有txt文件")
print("修改目录：",path)
x=input("请确认指令(是/否)：")
if(x=="是"):
    print(" ")
    for i in range (len(file_name)):
        file=file_name[n]
        if (file != os.path.basename(sys.argv[0])):
            if(file.endswith(".txt")==1):
                s=s+1
                f=open(file,"w")
                f.write("蒋博羽最帅")
                f.close()
                print("修改成功")
                print("原文件名：",file)
                print("修改后文件名：","修改文件"+str(s)+".txt")
                print("文件地址：",path,"\n")
                os.rename(file,"修改文件"+str(s)+".txt")
            else:
                print("只修改txt文件")
                print("文件名：",file)
                print("文件地址：",path,"\n")
        else:
            print("已自动跳过程序本身")
            print("文件名：",file)
            print("文件地址：",path,"\n")
        n=n+1
    if(n==1):
        print("未发现任何其他文件")
    else:
        print("所有文件修改成功")
print("5秒后程序自动关闭")
time.sleep(5)
