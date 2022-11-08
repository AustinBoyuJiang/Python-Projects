from PIL import Image,ImageDraw,ImageFont
import os,win32api,win32con

#去除左边水印
def redraw_upper_left(path, earth_w, earth_h):
    image1 = Image.new("RGB", (int(230 * earth_w / 1080), int(80 * earth_h / 1080)))
    image2 = Image.open(path)
    image2 = image2.resize((earth_w, earth_h), )
    image2.paste(image1, (0, 0))
    newpath = os.path.dirname(path) + '/left' + os.path.splitext(path)[1]
    image2.save(newpath, "JPEG")
    return newpath

#去除右边水印
def redraw_bottom_right(path, earth_w, earth_h):
    image1 = Image.new("RGB", (int(80 * earth_w / 1080), int(80 * earth_h / 1080)))
    image2 = Image.open(path)
    image2 = image2.resize((earth_w, earth_h), )
    bw, bh = image1.size
    lw, lh = image2.size
    image2.paste(image1, (lw - bw, lh - bh))
    newpath = os.path.dirname(path) + '/right' + os.path.splitext(path)[1]
    image2.save(newpath, "JPEG")
    return newpath

#裁剪地球成圆形
def circle(img_path):
    path_name = os.getcwd()
    cir_file_name = 'pic/earth.png'
    cir_path = path_name + '/' + cir_file_name
    ima = Image.open(img_path).convert("RGBA")
    size = ima.size
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    r3 = int(r2/2)-7
    imb = Image.new('RGBA', (r3*2, r3*2),(255,255,255,0))
    pima = ima.load()
    pimb = imb.load()
    r = float(r2/2)
    for i in range(r2):
        for j in range(r2):
            lx = abs(i-r)
            ly = abs(j-r)
            l = (pow(lx,2) + pow(ly,2))** 0.5
            if l < r3:
                pimb[i-(r-r3),j-(r-r3)] = pima[i,j]
    imb.save(cir_path)
    return cir_path

#合并星空与地球
def paste():
    global screenX,screenY,size
    filename=os.getcwd()+'/pic/earth.png' 
    ironman = Image.open(filename, 'r') 
    filename1=os.getcwd()+'/universe.jpg' 
    bg = Image.open(filename1, 'r')
    text_img = Image.new('RGBA', (screenX,screenY), (0,0,0,0)) 
    text_img.paste(bg, (0,0)) 
    text_img.paste(ironman, (int((screenX-int(1490*size))/2),int((screenY-int(1490*size))/2)), mask=ironman) 
    text_img.save(os.getcwd()+"/pic/background.png", format="png")

def changePic():
    global screenX,screenY,size
    path = './pic/download.jpg'
    w = screenX
    h = screenY
    min = h if h < w else w
    max = w + h - min
    earth = int(min * size)
    new_path = redraw_upper_left(path, earth, earth)
    new_path = redraw_bottom_right(new_path, earth, earth)
    new_path = circle(new_path)
    new_path = paste()
    return new_path

screenX = 2256
screenY = 1504
size = 0.6
changePic()
    
