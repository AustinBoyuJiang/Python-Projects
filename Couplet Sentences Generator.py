#coding:utf-8
import synonyms
import jieba

def couplet(sen1):
    sen2 = ""
    s = ""
    words = " ".join(jieba.cut(sen1)).split(" ")
    for word in words:
        try:text = synonyms.nearby(word.strip('\''))[0][1]
        except:text = word.strip('\'')
        s = s+text
    n = 0
    for i in s:
        sen2 = sen2+i
        n = n+1
        if(n==len(sen1)):break
    return sen2
while(1):
    print("下联: "+couplet(str(input("上联:"))))
    print("")
