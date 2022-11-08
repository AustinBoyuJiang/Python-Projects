import matplotlib.pyplot as plt
from math import *

def arange(x, y, k):
    res = []
    while (x <= y):
        res.append(x)
        x += k
    return res

def calc(x):
    return abs(x ** (2 / 3)) + (10 - x ** 2) ** 0.5 * sin(pi * x * k)

x = arange(-5, 6, 0.01)
lim = 10
k = 10
speed = 0.2
dir = -1
while True:
    plt.clf()
    plt.title("y=abs(pow(x, 2/3))+pow(10-pow(x,2),0.5)*sin(pi*x*k)     k=%s" % str(round(k, 3)))
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid()
    plt.plot(x, list(map(calc, x)))
    plt.pause(0.01)
    plt.ioff()
    k += speed * dir
    if (k >= lim or k <= -lim):
        dir *= -1
