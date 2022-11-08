import geoip2.database
import socket
import os

def ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip1=s.getsockname()[0]
    finally:
        s.close()
    return ip1

def position(ip):
    response = reader.city(ip)
    Country_IsoCode = response.country.iso_code
    Country_Name = response.country.name
    Country_NameCN = response.country.names['zh-CN']
    Country_SpecificName = response.subdivisions.most_specific.name
    Country_SpecificIsoCode = response.subdivisions.most_specific.iso_code
    City_Name = response.city.name
    City_PostalCode = response.postal.code
    Location_Latitude = response.location.latitude
    Location_Longitude = response.location.longitude
    print("  [*] Target: "+ip+" GeoLite2-Located")
    print("  [+] Country_IsoCode:  "+Country_IsoCode)
    print("  [+] Country_Name:  "+Country_Name)
    print("  [+] Country_NameCN:  "+Country_NameCN)
    print("  [+] Country_SpecificName:  "+Country_SpecificName)
    print("  [+] Country_SpecificIsoCode:  "+Country_SpecificIsoCode)
    print("  [+] City_Name:  "+str(City_Name))
    if City_PostalCode == None:
        City_PostalCode=None
    print("  [+] City_PostalCode: "+str(City_PostalCode))
    print("  [+] Location_Latitude: "+str(Location_Latitude))
    print("  [+] Location_Longitude: "+str(Location_Longitude))
    info={
        "ip":ip,
        "Country_IsoCode":Country_IsoCode,
        "Country_Name":Country_Name,
        "Country_NameCN":Country_Name,
        "Country_SpecificName":Country_SpecificName,
        "Country_SpecificIsoCode":Country_SpecificIsoCode,
        "City_Name":str(City_Name),
        "City_PostalCode":str(City_PostalCode),
        "Location_Latitude":str(Location_Latitude),
        "Location_Longitude":str(Location_Longitude)}
    return info

def getsite():
    global reader
    reader = geoip2.database.Reader(os.path.abspath('.')+"\\GeoLite2-City_20191112\\GeoLite2-City.mmdb")
    try:
        return position(ip())
    except BaseException:
        print("No revenue this IP:  "+ip())
print(ip())

def site(ip):
    global reader
    reader = geoip2.database.Reader(os.path.abspath('.')+"\\GeoLite2-City_20191112\\GeoLite2-City.mmdb")
    try:
        return position(ip)
    except BaseException:
        print("No revenue this IP:  "+ip)
