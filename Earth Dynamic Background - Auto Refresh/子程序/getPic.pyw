import requests
import os

#判断路径
def checkDir(download_path):
  mkdirlambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True
  mkdirlambda(download_path)

#爬取图片
def crawlWallpaper(download_path = 'pic'):
  checkDir(download_path)
  picture_url = 'http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG'
  res = requests.get(picture_url)
  with open(os.path.join(download_path, './download.jpg'), 'wb') as f:
    f.write(res.content)

crawlWallpaper()
