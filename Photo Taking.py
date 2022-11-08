import cv2,os

def desktop():
    path = os.path.join(os.path.expanduser("~"), "Desktop") + "\\"
    return path

def name(file):
    path = desktop()
    n = 1
    while(os.path.exists(path+file+str(n)+".png")):
        n=n+1
    return path+file+str(n)+".png"

def shoot():
    cap=cv2.VideoCapture(0)
    while True:
        sucess,img=cap.read()
        color=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow("img",color)
        k=cv2.waitKey(1)
        if (k == 27):
            cap.release()
            exit()
        elif (k == ord("s")):
            filename = name("photo")
            cv2.imwrite(filename,img)
            cv2.destroyAllWindows()
            print("拍摄成功  路径: "+filename)

shoot()
