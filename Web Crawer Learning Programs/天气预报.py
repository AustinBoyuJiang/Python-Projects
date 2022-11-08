from translate import Translator
import urllib.request as r
import json
while(1):
    s=input('请输入城市(国家+城市): ')
    translator= Translator(from_lang="chinese",to_lang="english")
    a = translator.translate(s)
    try:
        url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'.format(a)
        rst=r.urlopen(url).read().decode('utf-8')
        weather=json.loads(rst)
        print('天气情况',weather['list'][0]['weather'][0]['description'],'\n'+
        '气压',weather['list'][0]['main']['pressure'],'\n'+
        '最高温度',weather['list'][0]['main']['temp_max'],'\n'+
        '最低温度',weather['list'][0]['main']['temp_min'],'\n'+
        '当前温度',weather['list'][0]['main']['temp'],'\n'+
        '风',weather['list'][0]['wind']['speed'],'\n'+
        '发布时间',weather['list'][0]['dt_txt'],'\n')
    except:
        print("没收录",s,"地区\n")
