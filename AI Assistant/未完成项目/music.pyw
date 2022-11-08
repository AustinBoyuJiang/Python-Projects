from selenium.webdriver.common.by import By
from urllib.request import urlopen
from playsound import playsound
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib

def play(name):
    page = urlopen("https://music.163.com/#/search/m/?s="+name+"&type=1")
    code = BeautifulSoup( page.read( ), "html.parser" )
    
    
    id = 77211
    url="http://music.163.com/song/media/outer/url?id="+str(id)+".mp3"
    print("正在下载",name)
    try:
        urllib.request.urlretrieve(url,"./%s.mp3"% "music")
    except:
        print("下载失败")
    else:
        print("下载成功")
        print("正在播放")
        print("播放结束")

play("Monster")
