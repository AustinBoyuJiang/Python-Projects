#导入第三方库
import turtle
import math
import pygame
import win32api
import win32con
import pyautogui
import keyboard

#三角函数cos
def cos(n):
    return math.cos(math.radians(n))

#三角函数sin   
def sin(n):
    return math.sin(math.radians(n))

#获取鼠标位置
def getMouse(xy):
    x,y=pyautogui.position()
    x=x-win32api.GetSystemMetrics(win32con.SM_CXSCREEN)/2
    y=y-win32api.GetSystemMetrics(win32con.SM_CYSCREEN)/2
    if(xy=='x'):return x
    elif(xy=='y'):return y

#检查按键
def checkKey():
    global timePlus,time
    if(keyboard.is_pressed("up")):
        if(timePlus<3):
            timePlus=timePlus+0.01
    if(keyboard.is_pressed("down")):
        if(timePlus>0.5):
            timePlus=timePlus-0.01
    time=time+(timePlus-time)*0.01

#移动到坐标
def moveTo(x,y,z):
    global time,mouseX,mouseY
    turtle.goto((cos(mouseX)*x-sin(mouseX)*y)*time,(cos(mouseY)*(cos(mouseX)*y+sin(mouseX)*x)+sin(mouseY)*z)*time)

#画立方体
def drawCube(x,y,z,side):
    moveTo(x+side,y+side,z+side)
    turtle.down()
    moveTo(x-side,y+side,z+side)
    moveTo(x-side,y-side,z+side)
    moveTo(x+side,y-side,z+side)
    moveTo(x+side,y+side,z+side)
    moveTo(x+side,y+side,z-side)
    moveTo(x+side,y-side,z-side)
    moveTo(x+side,y-side,z+side)
    moveTo(x+side,y-side,z-side)
    moveTo(x-side,y-side,z-side)
    moveTo(x-side,y-side,z+side)
    moveTo(x-side,y-side,z-side)
    moveTo(x-side,y+side,z-side)
    moveTo(x+side,y+side,z-side)
    moveTo(x-side,y+side,z-side)
    moveTo(x-side,y+side,z+side)
    turtle.up()

#初始化
time=1.5
timePlus=1.5
mouseX=0
mouseY=0
turtle.title("立方体")
turtle.color("#000000")
turtle.bgcolor("#ffffff")
turtle.hideturtle()
turtle.speed(0)
turtle.delay(0)
turtle.tracer(False)
pygame.mixer.init()
pygame.mixer.music.load("CORSAK - 溯 Reverse (Live).mp3")
pygame.mixer.music.play(-1)

#主程序
while(1):
    mouseX=mouseX+(getMouse('x')-mouseX)*0.002
    mouseY=mouseY+(getMouse('y')-mouseY)*0.002
    turtle.pensize(time*2)
    turtle.clear()
    checkKey()
    drawCube(50,50,50,40)
    drawCube(50,50,-50,40)
    drawCube(50,-50,50,40)
    drawCube(50,-50,-50,40)
    drawCube(-50,50,50,40)
    drawCube(-50,50,-50,40)
    drawCube(-50,-50,50,40)
    drawCube(-50,-50,-50,40)
    turtle.update()
