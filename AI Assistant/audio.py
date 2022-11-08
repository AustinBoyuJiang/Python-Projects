import speech_recognition as sr
from playsound import playsound
from aip import AipSpeech
import os,random,sys,chardet

def speak(name,content,gender):
    if(gender == "男"):
        per = 2
    elif(gender == "女"):
        per = 4
    APP_ID="17899212"
    API_KEY="NP4VQ1QvI65HtGCNcR8couNP"
    SECRET_KEY="nEqGXWG6eLglOA5jt4HQsIPwCGyGo7IB"
    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
    result=client.synthesis(text=str(content),options={"vol":5,"per":per})
    file = name+".mp3"
    with open(file, 'wb') as f:
        f.write(result)
    f.close()
    playsound(file)
    os.remove(file)

def identify():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    test = r.recognize_google(audio, language='cmn-Hans-CN', show_all=True)
    try:
        word = test['alternative'][0]['transcript']
    except:
        word = ""
        return None
    else:
        return word

def rouse(name):
    content = ["我在","什么事","怎么了"]
    while(not(name in str(identify()))):
        pass
    return content[random.randint(0,len(content)-1)]
