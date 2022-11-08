#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import time
import pywifi

wifi = pywifi.PyWiFi()
ifaceList =wifi.interfaces()#获得无线网卡对象列表
#print(wifi.interfaces())
#for i in ifaceList:
    #print(i)
iface = ifaceList[0]

#一般第一个就是你需要的无线网卡，但是要是有多块无线网卡时，此处需#要指定你要使用的是那块无线网卡。

iface.disconnect() 

#由于我的无线网卡已经连接WIFI了，所以要想使用iface.scan()，必须要断#开wifi链接
time.sleep(1)

print(iface.status())
iface.scan()#无线网卡扫描无线网络

result = iface.scan_results()#获取扫描结果列表

for i in range(len(result)):
    print(result[i].ssid,result[i].signal)
