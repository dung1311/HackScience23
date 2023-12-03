from tkinter import *
from tkinter import filedialog
import text_to_speech
import os
import PIL
from PIL import Image, ImageTk
import image
import cv2

userGuide = "Welcome to our waste classification system please leave trash in front of the screen"

def getPath():
    file_path = filedialog.askopenfilename(title="Chọn một hình ảnh", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path == '':
        #print('chua lay duoc file_path')
        pass
    else:
        #print('da lay duoc file_path' + str(file_path))
        image.detect(file_path)

def video():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.flip(frame, -1)
        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def tutorial():
    text_to_speech.speak(userGuide)

def main():
    root = Tk()
    root.geometry("")
    root.title("ITHEX trash detection")
    root.configure(background = '#9F2B68')

    img = ImageTk.PhotoImage(Image.open("background1.png"))
    label = Label(root, image = img)
    label.pack()
    btn1 = Button(root, text= "Image", background = '#34e8eb', foreground= 'black', command=getPath, width=10, height=4)
    btn1.place(x = 10, y = 10)
    # btn2 = Button(root, text='video', bg= 'black', fg= 'white', command=video)
    # btn2.place(x = 200, y = 10)
    btn3 = Button(root, text='User guide', background='#34e8eb', fg='black', command=tutorial, height=4)
    btn3.place(x = 230, y = 10)
    
    root.mainloop()

if __name__ == '__main__':
    main()


