from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # title on DISPLAY
        title_lab=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lab.place(x=0,y=0,width=1530,height=60)





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()