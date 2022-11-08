from urllib.request import urlopen
from translate import Translator
from bs4 import BeautifulSoup
import win32api
import requests

def search(search):
    search = search.strip(" ").strip("\n")
    if(search ==""):
        return "搜索什么"
    #website = "https://zh.wikipedia.org/zh-cn/"+search
    website = "https://www.google.com/search?q="+search+"&safe=active&ssui=on"
    win32api.ShellExecute(0, "open",website,"","", 1)
    return ("已为你搜索\"" + search + "\"")
