from tkinter import *
from math import exp,log,sin,cos,tan

class Calculator:
    def __init__(self):
        window=Tk()
        window.title("简易计算器")

        frame1=Frame(window).pack()
        self.e1, self.e2 = StringVar(), StringVar()
        Label(frame1,text="请输入表达式：").pack() #放置标签“请输入表达式”
        Entry(frame1,textvariable = self.e1,justify = RIGHT, width=28).pack() #第一个entry
        Label(frame1,text="输出结果：").pack() #放置标签“输出结果”
        Entry(frame1,textvariable = self.e2,justify = RIGHT, width=28).pack() #第二个entry

        frame2=Frame(window)
        frame2.pack()  
        op=[[1,2,3,'+'],[4,5,6,'-'],[7,8,9,'*'],[0,'.','=','/'],['(',')','exp','log'],['sin','cos','tan','clear']]    
        for i in range(6):  #放置按钮
            for j in range(4):
                if op[i][j] == '=':
                    Button(frame2,text = op[i][j],command = lambda: self.e2.set(str(eval(self.e1.get()))),width=6).grid(row =i,column=j)
                elif op[i][j] == 'clear':
                    Button(frame2,text = op[i][j],command = lambda: (self.e1.set(''),self.e2.set('')),width=6).grid(row =i,column=j)
                else:
                    Button(frame2,text = str(op[i][j]),command = lambda w=self.e1, c=str(op[i][j]): w.set(w.get() + c),width=6).grid(row=i,column=j)
        window.mainloop()

Calculator()
