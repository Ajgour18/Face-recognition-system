from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np




class Face_RECOGNITION:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # title on DISPLAY
        title_lab=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lab.place(x=0,y=0,width=1530,height=60)

        # Left image 
        img_left=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\face-recognition_1.jpg")
        img_left=img_left.resize((600,730),Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(img_left)

        lab_1=Label(self.root,image=self.photo)
        lab_1.place(x=0,y=60,width=600,height=730)

        # Right image 
        img=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\facial_recognition_system_2.webp")
        img=img.resize((930,730),Image.Resampling.LANCZOS)
        self.photo_1=ImageTk.PhotoImage(img)

        lab_2=Label(self.root,image=self.photo_1)
        lab_2.place(x=600,y=60,width=930,height=730)

        # BUTTON train data
        b1_text=Button(lab_2,command=self.face_recog,text="Face Recognition",cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_text.place(x=355,y=640,width=200,height=40)

    # ==============  function  ==============

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            feature=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student_detail where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student_detail where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student_detail where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                # my_cursor.execute("select Division from student where Student_Id="+str(id))
                # di=my_cursor.fetchone()
                # di="+".join(di)

                 

                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    #cv2.putText(img,f"Division:{di}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        


if __name__ == "__main__":
    root = Tk()
    obj = Face_RECOGNITION(root)
    root.mainloop()