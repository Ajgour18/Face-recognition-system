from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_RECOGNITION
from developer import Developer
from help import Help
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")


        # image 1
        img=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\face2.jpg")
        img=img.resize((510,130),Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)

        lab_1=Label(self.root,image=self.photo)
        lab_1.place(x=0,y=0,width=510,height=130)

        # image 2
        img2=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\face1.webp")
        img2=img2.resize((510,130),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img2)

        lab_2=Label(self.root,image=self.photo1)
        lab_2.place(x=510,y=0,width=510,height=130)

        # image 3
        img3=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\face3.jpg")
        img3=img3.resize((510,130),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img3)

        lab_3=Label(self.root,image=self.photo2)
        lab_3.place(x=1020,y=0,width=510,height=130)

        # BACKGROUNDimage 
        img4=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\background.jpg")
        img4=img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photo3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # title on DISPLAY
        title_lab=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lab.place(x=0,y=0,width=1530,height=45)

        # BUTTONS
        # STUDENTS BUTTONS
        img5=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\students.jpeg")
        img5=img5.resize((200,200),Image.Resampling.LANCZOS)
        self.photo5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photo5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1_text=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b1_text.place(x=200,y=300,width=200,height=40)


        # FACE DETECTOR BUTTONS
        img6=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\facedetect.jpg")
        img6=img6.resize((200,200),Image.Resampling.LANCZOS)
        self.photo6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,command=self.face_recognition,image=self.photo6,cursor="hand2")
        b2.place(x=510,y=100,width=200,height=200)

        b2_text=Button(bg_img,command=self.face_recognition,text="Face Detector",cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b2_text.place(x=510,y=300,width=200,height=40)


        # ATTENDANCE BUTTONS
        img7=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\attandance.jpg")
        img7=img7.resize((200,200),Image.Resampling.LANCZOS)
        self.photo7=ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photo7,cursor="hand2")
        b3.place(x=830,y=100,width=200,height=200)

        b3_text=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b3_text.place(x=830,y=300,width=200,height=40)

        # HELP BUTTONS
        img8=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\help.jpg")
        img8=img8.resize((200,200),Image.Resampling.LANCZOS)
        self.photo8=ImageTk.PhotoImage(img8)

        b4=Button(bg_img,command=self.Help_button,image=self.photo8,cursor="hand2")
        b4.place(x=1150,y=100,width=200,height=200)

        b4_text=Button(bg_img,command=self.Help_button,text="HELP",cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b4_text.place(x=1150,y=300,width=200,height=40)

        #####
        # TRAIN FACE BUTTONS
        img9=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\train.webp")
        img9=img9.resize((200,200),Image.Resampling.LANCZOS)
        self.photo9=ImageTk.PhotoImage(img9)

        b5=Button(bg_img,image=self.photo9,command=self.train_data,cursor="hand2")
        b5.place(x=200,y=370,width=200,height=200)

        b5_text=Button(bg_img,text="Train Face",command=self.train_data,cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b5_text.place(x=200,y=570,width=200,height=40)


        # PHOTO BUTTONS
        img10=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\photospng.png")
        img10=img10.resize((200,200),Image.Resampling.LANCZOS)
        self.photo10=ImageTk.PhotoImage(img10)

        b6=Button(bg_img,image=self.photo10,cursor="hand2",command=self.open_img)
        b6.place(x=510,y=370,width=200,height=200)

        b6_text=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b6_text.place(x=510,y=570,width=200,height=40)


        # Developer BUTTONS
        img11=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\hd wallpaper\developer.jpg")
        img11=img11.resize((200,200),Image.Resampling.LANCZOS)
        self.photo11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,command=self.developer_button,image=self.photo11,cursor="hand2")
        b7.place(x=830,y=370,width=200,height=200)

        b7_text=Button(bg_img,command=self.developer_button,text="Developer",cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b7_text.place(x=830,y=570,width=200,height=40)

        # EXIT BUTTONS
        img12=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\exit.jpg")
        img12=img12.resize((200,200),Image.Resampling.LANCZOS)
        self.photo12=ImageTk.PhotoImage(img12)

        b8=Button(bg_img,image=self.photo12,cursor="hand2")
        b8.place(x=1150,y=370,width=200,height=200)

        b8_text=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b8_text.place(x=1150,y=570,width=200,height=40)
    

    def open_img(self):
        os.startfile("data")

        
    # ===============functions================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_RECOGNITION(self.new_window)

    def developer_button(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def Help_button(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()