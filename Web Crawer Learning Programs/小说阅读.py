#初始化
from urllib.request import urlopen#导入第三方库
from bs4 import BeautifulSoup
import pypinyin,time,math,re,os
website = "http://www.quanben.io"#变初始化
choise="否"


while(1): 
    #小说分类界面
    os.system('cls')#获取分类数据
    page = urlopen( website )
    soup = BeautifulSoup( page.read( ), "html.parser" )
    content = soup.div.find_all("a")
    classifyWebsite={}
    classifyList=[]
    print( "内容取自全本小说网" )
    print( "原网址: ",website,"\n" )
    for i in content:#输出分类
        print( str(len(classifyList)+1)+". "+i.text )
        classifyList.append( i.text )
        classifyWebsite[ i.text ] = website+i[ "href" ]
    print("")
    choise=str(input("是否退出: "))
    print("")
    if(choise=="是"):
        break
    

    while(1):
        #小说名界面
        if(choise!="是"):
            while(1):#获取小说名数据
                try:
                    number=int(input("请输入分类序号: "))
                except:
                    print("请输入正确类型\n")
                else:
                    if(number>=1 and number<=len(classifyList)):
                        break
                    else:
                        print("不存在该序号\n")
        os.system('cls')
        namepage=classifyWebsite[classifyList[number-1]]
        page = urlopen( namepage )
        soup = BeautifulSoup( page.read( ), "html.parser" )
        content = soup.find_all("div")[2].find_all("div")
        nameWebsite={}
        nameList=[]
        print( "内容取自全本小说网" )
        print( "原网址: ",namepage,"\n" )
        n=0
        for i in range (math.ceil((len(content)-2)/2)):#输出小说名
            print( str(len(nameList)+1)+". "+content[n].h3.text )
            nameList.append( content[n].h3.text )
            nameWebsite[ content[n].h3.text ] = website+content[n].h3.a[ "href" ]
            n=n+2
        print("")
        choise=str(input("是否返回: "))
        print("")
        if(choise=="是"):
            break
        
        s=3
        choise="否"
        while(1):
            if(choise=="3" or choise=="否"):
                #小说目录界面
                if(choise=="否"):
                    while(1):#获取目录网址
                        try:
                            number=int(input("请输入书名序号: "))
                        except:
                            print("请输入正确类型\n")
                        else:
                            if(number>=1 and number<=len(nameList)):
                                break
                            else:
                                print("不存在该序号\n")
                os.system('cls')
                bookdir=nameWebsite[nameList[number-1]]+"list.html"
                print( "内容取自全本小说网" )
                print( "原网址: ",bookdir,"\n" )
                pageWebsite={}
                dirList=[]
                page = urlopen( bookdir )#获取目录数据
                soup = BeautifulSoup( page.read( ), "html.parser" )
                print( soup.title.text )#输出小说介绍
                print( soup.p.get_text( ) )
                n=2
                content = soup.find_all( 'p' )
                for i in range ( len( content ) ):
                    if( n<4 ):
                        print( content[ n ].text )
                    n=n+1
                print( "" )
                content = soup.ul.find_all( "li" )#输出小说目录
                for i in content:
                    print( str(len(dirList)+1)+". "+i.text )
                    dirList.append( i.text )
                    pageWebsite[ i.text ] = website+i.a[ "href" ]
                print("")                
                choise=str(input("是否返回: "))
                print("")
                if(choise=="是"):
                    break


            #小说内容界面（正在修改）
            '''
            问题1: 无法获取文章全部
            问题2: 无法频繁访问网站
            '''
            if(s==3):#获得本章网址
                while(1):
                    try:
                        number=int(input("请输入章节序号: "))
                    except:
                        print("请输入正确类型\n")
                    else:
                        if(number>=1 and number<=len(dirList)):
                            break
                        else:
                            print("不存在该序号\n")
            os.system('cls')
            thispage = pageWebsite[dirList[number-1]]
            print( "内容取自全本小说网" )
            print( "原网址: ",thispage,"\n" )
            page = urlopen( thispage )#获取本章数据
            soup = BeautifulSoup( page.read( ), "html.parser" )
            content=soup.find_all("p")
            n=0#输出本章内容
            for i in content:
                if( n!=0 ):
                    print( "    ",end="")
                print( i.text+"\n" )
                if( n==0 ):
                    print( "" )
                n=n+1
            while(1):#选择操作
                print("1. 上一章")
                print("2. 下一章")
                print("3. 目录")
                choise=str(input("请选择操作序号: "))
                if(choise=="1"):
                    if(number<=1):
                        print("已经是第一章了\n")
                    else:
                        number=number-1
                        s=1
                        break
                elif(choise=="2"):
                    if(number>=len(dirList)):
                        print("已经是最后一章了\n")
                    else:
                        s=2
                        number=number+1
                        break
                elif(choise=="3"):
                    s=3
                    break
                else:
                    print("不存在该序号\n")
