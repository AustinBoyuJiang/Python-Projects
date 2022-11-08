#导入第三方库
import turtle
import math
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

def mouseMove():
    if(keyboard.is_pressed("space")==True):
        mx=mouseX
        my=mouseY
        while(keyboard.is_pressed("space")==True):
            mouseX=getMouse("x")-mx
            mouseX=getMouse("y")-my

#检查按键
def checkKey():
    global time
    if(keyboard.is_pressed("up")):
        if(time<3):
            time=time+0.005
    if(keyboard.is_pressed("down")):
        if(time>0.5):
            time=time-0.005

#移动到坐标
def moveTo(x,y,z):
    global time,mouseX,mouseY
    turtle.goto((cos(mouseX)*x-sin(mouseX)*y)*time,(cos(mouseY)*(cos(mouseX)*y+sin(mouseX)*x)+sin(mouseY)*z)*time)

#画场地
def drawGround(x,y,z,side):
    turtle.color("#000000")
    for i in range(math.floor(x/side)):
        moveTo((i+1)*side,0,0)
        turtle.down()
        moveTo((i+1)*side,0,z)
        turtle.up()
    for i in range(math.floor(z/side)):
        moveTo(0,0,(i+1)*side)
        turtle.down()
        moveTo(x,0,(i+1)*side)
        turtle.up()
    for i in range(math.floor(y/side)):
        moveTo(0,(i+1)*side,0)
        turtle.down()
        moveTo(x,(i+1)*side,0)
        turtle.up()
    for i in range(math.floor(x/side)):
        moveTo((i+1)*side,0,0)
        turtle.down()
        moveTo((i+1)*side,y,0)
        turtle.up()
    for i in range(math.floor(z/side)):
        moveTo(0,0,(i+1)*side)
        turtle.down()
        moveTo(0,y,(i+1)*side)
        turtle.up()
    for i in range(math.floor(y/side)):
        moveTo(0,(i+1)*side,0)
        turtle.down()
        moveTo(0,(i+1)*side,z)
        turtle.up()
    turtle.pensize(5)
    moveTo(0,0,0)
    turtle.color("#ff0000")
    turtle.down()
    moveTo(x,0,0)
    turtle.up()
    moveTo(0,0,0)
    turtle.color("#00ff00")
    turtle.down()
    moveTo(0,y,0)
    turtle.up()
    moveTo(0,0,0)
    turtle.color("#0000ff")
    turtle.down()
    moveTo(0,0,z)
    turtle.up()
    turtle.color("#000000")
    turtle.pensize(10)
    moveTo(0,0,0)
    turtle.down()
    moveTo(0,0,0)
    turtle.up()
    turtle.pensize(2)

#初始化
time=1.5
mouseX=0
mouseY=0
turtle.title("Back Ground")
turtle.color("#000000")
turtle.bgcolor("#ffffff")
turtle.pensize(2)
turtle.hideturtle()
turtle.speed(0)
turtle.delay(0)
turtle.tracer(False)

#主程序
while(1):
    mouseX=getMouse('x')
    mouseY=getMouse('y')
    turtle.clear()
    checkKey()
    drawGround(220,220,220,50)
    turtle.update()
