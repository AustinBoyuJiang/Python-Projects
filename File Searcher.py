import string,os,sys,math,time,shutil    #导入函数库

def get_disklist(): #获得电脑磁盘路径函数
    disk_list = []
    for c in string.ascii_uppercase:
        disk = c+":"
        if os.path.isdir(disk):
            disk_list.append(disk)
    return disk_list
    a=0
    
def formatSize(byte):   #文件大小的单位转换函数
    byte = float(byte)
    kb = byte / 1024
    if (kb >= 1024):
        M = kb / 1024
        if (M >= 1024):
            G = M / 1024
            return (str((math.ceil(G*100)/100))+"G")
        else:
            return (str((math.ceil(M*100)/100))+"M")
    else:
        return (str((math.ceil(kb*100)/100))+"kb")
    
def getDocSize(path):   #获得文件大小函数
    size = os.path.getsize(path)
    return formatSize(size)

def getFileSize(path):  #获得文件夹大小函数
    sumsize = 0
    filename = os.walk(path+"\\")
    for root, dirs, files in filename:
        for fle in files:
            size = os.path.getsize(os.path.join(root,fle))
            sumsize += size
    return formatSize(sumsize)
while(1):
    
    os.system('cls')    #清屏
    disk_name=get_disklist()    #程序初始化
    print("Search files\n") 
    name = input("Search content:")
    
    if(not(":" in name)):   #判断输入是否为路径
        while(1):   #如果判断是文件：
            choise = input(str("\ndefault or custom:")) #获得查询路径
            print("")
            if(choise=="custom"):
                path = input("Search path:")
                if(os.path.exists(path)):
                    if(os.path.isfile(path)):
                        print("This is a file,not path")
                    else:
                        a=1
                        break
                else:
                    print("There is no this path")
            elif(choise=="default"):
                path=0
                break
            else:
                print("Please select the correct reply")
                
        print("Please wait patiently")  #开始查询文件
        print("Search result:\n")
        n=0
        dir_path=[]
        if(path==0):    #判断是默认路径还是自定义路径
            for disk in disk_name:  #如果是自定义路径的话：
                for root,dirs,files in os.walk(disk+"\\"):
                    for file in files:
                        if(str.lower(name) in str.lower(file)):
                            n=n+1
                            print(str(n)+".",file)
                            print("path:",root,"\n")
                            dir_path.append(os.path.join(root,file))
                    for dir1 in dirs:
                        if(str.lower(name) in str.lower(dir1)):
                            n=n+1
                            print(str(n)+".",dir1)
                            print("path:",root,"\n")
                            dir_path.append(os.path.join(root, dir1))
                            
        else:   #如果是默认路径的话(全机搜索)：
            if(path[-1]!="\\"):
                path=path+"\\"
            for root,dirs,files in os.walk(path):
                for file in files:
                    if(name in file):
                        n=n+1
                        print(str(n)+".",file)
                        print("path:",root,"\n")
                        dir_path.append(os.path.join(root,file))
                for dir1 in dirs:
                    if(name in dir1):
                        n=n+1
                        print(str(n)+".",dir1)
                        print("path:",root,"\n")
                        dir_path.append(os.path.join(root, dir1))            
        print("There are "+str(n)+" result")
        
        while(1):   #查询完后对文件操作
            choise=input("\ncontinue or operation:")
            print("")
            if(choise=="operation"):    #操作：
                while(1):
                    choise=input("info or open or delete:") #选择操作
                    print("")
                    
                    if(choise=="open"): #打开文件
                        try:
                            choise=int(input("Serial number:")) #获得查询文件序号
                        except BaseException:
                            print("Please enter integer")
                        else:
                            try:
                                os.system("start explorer "+dir_path[choise-1])
                                print(dir_path[choise-1]," has been opened")
                            except BaseException:
                                print("There is no this option")
                        break
                    
                    elif(choise=="info"):   #查询文件信息
                        try:
                            choise=int(input("Serial number:"))
                        except BaseException:
                            print("Please enter integer")
                        else:
                            try:
                                print("\nfile name: ",os.path.basename(dir_path[choise-1])) #文件名
                                if(os.path.isfile(dir_path[choise-1])): #文件大小
                                    print("file size: ",getDocSize(dir_path[choise-1]))
                                else:
                                    print("file size: ",getFileSize(dir_path[choise-1]))
                                creationTime = time.localtime(os.stat(dir_path[choise-1]).st_ctime) #文件创建日期
                                print("file creation time: ",time.strftime('%Y-%m-%d',creationTime))
                                print("file path: ",os.path.dirname(dir_path[choise-1]))    #文件路径
                            except BaseException:
                                print("There is no this option")
                        break
                    
                    elif(choise=="delete"): #删除文件
                        try:
                            choise=int(input("Serial number:"))
                        except BaseException:
                            print("Please enter integer")
                        else:
                            try:
                                if(dir_path[choise-1]==os.path.abspath(__file__)):
                                    print("Can't delete this procedure")
                                else:
                                    if (os.path.isdir(dir_path[choise-1])):
                                        shutil.rmtree(dir_path[choise-1])
                                    else:
                                        os.remove(dir_path[choise-1])
                                    print(dir_path[choise-1]," has been deleted")
                            except BaseException:
                                print("There is no this option")
                        break
                    else:
                        break  
            else:   #跳过
                break
            
    else:   #如果判断是路径：
        if(os.path.isdir(name)):    #电脑中是否含有此路径
            while(1):
                choise=input("\ncontinue or operation:")
                print("")
                
                if(choise=="operation"):    #操作：
                    if(os.path.isdir(name)):
                        while(1):
                            choise=input("info or open or delete:") #选择操作
                            print("")
                            
                            if(choise=="open"): #打开文件
                                os.system("start explorer "+name)
                                print(name," has been opened")
                                
                            elif(choise=="info"):   #查询文件信息
                                print("file name: ",os.path.basename(name))
                                print("file size: ",getFileSize(name))
                                creationTime = time.localtime(os.stat(name).st_ctime)
                                print("file creation time: ",time.strftime('%Y-%m-%d',creationTime))
                                print("file path: ",os.path.dirname(name))
                                
                            elif(choise=="delete"): #删除文件
                                if(name in os.path.abspath(__file__)):
                                    print("Can't delete your own parent directory")
                                else:
                                    shutil.rmtree(name)
                                    print(name," has been deleted")
                            break
                    else:   #判断文件是否被删
                        print("This path has been deleted")
                else:   #跳过
                    break
        else:   
            print("There is no this path")
