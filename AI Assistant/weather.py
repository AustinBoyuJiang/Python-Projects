from translate import Translator
import urllib.request as r
import json

def tran(word,language):
    translator= Translator(from_lang="chinese",to_lang=language)
    if(language!="chinese"):
        return translator.translate(word).replace("&#39;","'").replace("。",".")
    else:
        return word

def weather(site,language):
    site = tran(site,"english")
    try:
        url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'.format(site)
        rst=r.urlopen(url).read().decode('utf-8')
        weatherList=json.loads(rst)
        weather={}
        weather.update({tran('天气情况',language):tran(weatherList['list'][0]['weather'][0]['description'],language)})
        weather.update({tran('气压',language):weatherList['list'][0]['main']['pressure']})
        weather.update({tran('最高温度',language):weatherList['list'][0]['main']['temp_max']})
        weather.update({tran('最低温度',language):weatherList['list'][0]['main']['temp_min']})
        weather.update({tran('当前温度',language):weatherList['list'][0]['main']['temp']})
        weather.update({tran('风',language):weatherList['list'][0]['wind']['speed']})
        weather.update({tran('发布时间',language):weatherList['list'][0]['dt_txt']})
        return weather
    except:
        pass

def output(weather):
    content=""
    if(weather!=None):
        for i in weather:
            print(i,weather[i])
            content = content+","+i+","+str(weather[i])
        return content
