import cv2
import os
def take_image():
    cap=cv2.VideoCapture(0)
    print("Capturing Started..")

    while True:
        ret,img=cap.read()
        cv2.imshow("Image data collector",img)
        key=cv2.waitKey(1)
        
        if key==ord("0"):
            dir='Number_0'
            if not os.path.exists(dir):
                os.mkdir(dir)
            num=len(os.listdir(dir))
            cv2.imwrite(dir+f"/{num+1}.jpeg",img)
            print(f"File Saved as {num+1}.jpeg in {dir}")

        if key==ord("1"):
            dir='Number_1'
            if not os.path.exists(dir):
                os.mkdir(dir)
            num=len(os.listdir(dir))
            cv2.imwrite(dir+f"/{num+1}.jpeg",img)
            print(f"File Saved as {num+1}.jpeg in {dir}")

        if key==ord("2"):
            dir='Number_2'
            if not os.path.exists(dir):
                os.mkdir(dir)
            num=len(os.listdir(dir))
            cv2.imwrite(dir+f"/{num+1}.jpeg",img)
            print(f"File Saved as {num+1}.jpeg in {dir}")

        if key==ord("3"):
            dir='Number_3'
            if not os.path.exists(dir):
                os.mkdir(dir)
            num=len(os.listdir(dir))
            cv2.imwrite(dir+f"/{num+1}.jpeg",img)
            print(f"File Saved as {num+1}.jpeg in {dir}")

        if key==ord("4"):
            dir='Number_4'
            if not os.path.exists(dir):
                os.mkdir(dir)
            num=len(os.listdir(dir))
            cv2.imwrite(dir+f"/{num+1}.jpeg",img)
            print(f"File Saved as {num+1}.jpeg in {dir}")

        if key==ord("5"):
            dir='Number_5'
            if not os.path.exists(dir):
                os.mkdir(dir)
            num=len(os.listdir(dir))
            cv2.imwrite(dir+f"/{num+1}.jpeg",img)
            print(f"File Saved as {num+1}.jpeg in {dir}")

        if key==ord("q"):
            print("Capturing completed..")
            break
    cv2.destroyAllWindows()
take_image()