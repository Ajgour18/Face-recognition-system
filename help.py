from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np




class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")

        # TOP image 
        img_top=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\com.jpg")
        img_top=img_top.resize((1530,740),Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(img_top)

        lab_1=Label(self.root,image=self.photo)
        lab_1.place(x=0,y=60,width=1530,height=740)


        # title on DISPLAY
        title_lab1=Label(self.root,text="Contact Us",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lab1.place(x=0,y=0,width=1530,height=60)

        # Content on DISPLAY
        title_lab2=Label(lab_1,text="WE WHOULD LOVE TO HEAR FROM\n\nYOU\n\nGET IN TOUCH\n\nE-MAIL\ncontact@ajay.com\n\nCALL\n7000690724\n\nADDRESS\nnew delhi - 110027",font=("times new roman",15,"bold"),fg="white",bg="black")
        title_lab2.place(x=1000,y=20,width=400,height=500)

        



if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()