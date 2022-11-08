from playsound import playsound
from aip import AipSpeech
import os
n = 0

def speak(content):
    global n
    n = n+1
    name = "audio"+str(n)
    APP_ID = "17899212"
    API_KEY = "NP4VQ1QvI65HtGCNcR8couNP"
    SECRET_KEY = "nEqGXWG6eLglOA5jt4HQsIPwCGyGo7IB"
    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
    result=client.synthesis(text=str(content),options={"vol":5,"per":4})
    file = name+".mp3"
    with open(file, 'wb') as f:
        f.write(result)
    f.close()
    playsound(file)
    os.remove(file)

while(1):speak(input("输入文字:"))
