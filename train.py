from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Training window")

        # title on DISPLAY
        title_lab=Label(self.root,text="TRAIN DATASET",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lab.place(x=0,y=0,width=1530,height=45)

        # TOP image 
        img_top=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\facedetect.jpg")
        img_top=img_top.resize((1530,740),Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(img_top)

        lab_1=Label(self.root,image=self.photo)
        lab_1.place(x=0,y=45,width=1530,height=740)

        # BUTTON train data
        b1_text=Button(lab_1,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1_text.place(x=1100,y=400,width=400,height=70)

        

    def train_classifier(self):
        data_dir=("data")
        #listcomprehension
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] 

        faces=[]
        ids=[] 

        for image in path:
            img=Image.open(image).convert('L')  # Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        # converting ids into numpy
        ids=np.array(ids)

        #====== Train the classifier and save ===========
        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set completed!!!")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()