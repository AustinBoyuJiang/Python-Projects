# coding=utf-8
import speech_recognition as sr
import logging

def identify():
    logging.basicConfig(level=logging.DEBUG)
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

while(1):
    print(identify())
