from translate import Translator
import sys,re

def translat(text,lan):
    translator= Translator(from_lang=lan,to_lang="english")
    translation = translator.translate(str.lower(text))
    translation = str.lower(re.sub(r'[^\w\s]','',translation))
    if(translation==str.lower(text)):
        if(lan=="english"):
            translator= Translator(from_lang="english",to_lang="chinese")
            translation = translator.translate(str.lower(text))
        else:
            translator= Translator(from_lang="english",to_lang=lan)
            translation = translator.translate(str.lower(text))
    return str.capitalize(str.lower(translation))
