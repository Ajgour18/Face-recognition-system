from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        # ===========Variables==========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

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
        title_lab=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lab.place(x=0,y=0,width=1530,height=45)

        # ===============Body================


        # main frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        # left frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",13,"bold"),bg="white")
        left_frame.place(x=10,y=10,width=760,height=580)

        # image on left frame
        img_left=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\students.jpeg")
        img_left=img_left.resize((750,130),Image.Resampling.LANCZOS)
        self.photo_left=ImageTk.PhotoImage(img_left)
        imageLabel=Label(left_frame,image=self.photo_left)
        imageLabel.place(x=8,y=0,width=740,height=130)

        # ============= current course in left frame =========================
        left_frame_current=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",13,"bold"),bg="white")
        left_frame_current.place(x=8,y=140,width=740,height=100)

        # Department label
        lab_dep=Label(left_frame_current,text="  Department  : ",font=("times new roman",13,"bold"),bg="white")
        lab_dep.grid(row=0,column=0,padx=10,sticky=W)
        
        # Combo Box
        dep_combo=ttk.Combobox(left_frame_current,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        # Course label
        lab_cou=Label(left_frame_current,text="   Course  : ",font=("times new roman",13,"bold"),bg="white")
        lab_cou.grid(row=0,column=2,padx=10,sticky=W)
        
        # Combo Box
        cou_combo=ttk.Combobox(left_frame_current,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        cou_combo["values"]=("Select","BE","MCA","PGDM","BCOM")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        # Year label
        lab_year=Label(left_frame_current,text="  Year  : ",font=("times new roman",13,"bold"),bg="white")
        lab_year.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        # Combo Box
        year_comb=ttk.Combobox(left_frame_current,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_comb["values"]=("Select","2000","2001","2002","2003")
        year_comb.current(0)
        year_comb.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # Semester label
        lab_sem=Label(left_frame_current,text="   Semester  : ",font=("times new roman",13,"bold"),bg="white")
        lab_sem.grid(row=1,column=2,padx=10,sticky=W)
        
        # Combo Box
        sem_combo=ttk.Combobox(left_frame_current,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("Select","1","2","3","4")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        # =================== Class student Information ====================
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",13,"bold"),bg="white")
        class_student_frame.place(x=8,y=245,width=740,height=300)

        # Student Id
        Student_lab=Label(class_student_frame,text="   Student ID  : ",font=("times new roman",13,"bold"),bg="white")
        Student_lab.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        Student_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student Name
        Student_name_lab=Label(class_student_frame,text="   Student Name  : ",font=("times new roman",13,"bold"),bg="white")
        Student_name_lab.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Student_Name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        Student_Name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Class division
        class_division_lab=Label(class_student_frame,text="   Class Division  : ",font=("times new roman",13,"bold"),bg="white")
        class_division_lab.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # div combo box
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=18,font=("times new roman",12,"bold"),state="readonly")
        div_combo["values"]=("Select","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        """class_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        class_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)"""

        # Roll no
        Rollno_lab=Label(class_student_frame,text="   Roll No  : ",font=("times new roman",13,"bold"),bg="white")
        Rollno_lab.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        Gender_lab=Label(class_student_frame,text="   Gender  : ",font=("times new roman",13,"bold"),bg="white")
        Gender_lab.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # Gender combo box
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select","MALE","FEMALE","OTHER")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        """Gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)"""

        # DOB
        DOB_lab=Label(class_student_frame,text="   DOB  : ",font=("times new roman",13,"bold"),bg="white")
        DOB_lab.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        Dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        Email_lab=Label(class_student_frame,text="   Email  : ",font=("times new roman",13,"bold"),bg="white")
        Email_lab.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone no
        phoneno_lab=Label(class_student_frame,text="   Phone No  : ",font=("times new roman",13,"bold"),bg="white")
        phoneno_lab.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phoneno_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phoneno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        add_lab=Label(class_student_frame,text="   Address  : ",font=("times new roman",13,"bold"),bg="white")
        add_lab.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher
        teach_lab=Label(class_student_frame,text="   Teacher  : ",font=("times new roman",13,"bold"),bg="white")
        teach_lab.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        phoneno_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        phoneno_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio buttons 
        self.var_r1=StringVar()
        rad_button_1=ttk.Radiobutton(class_student_frame,variable=self.var_r1,text="Take photo sample",value="yes")
        rad_button_1.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        rad_button_2=ttk.Radiobutton(class_student_frame,variable=self.var_r1,text="Take no photo sample",value="no")
        rad_button_2.grid(row=5,column=1,padx=10,pady=5,sticky=W)

        # button frame
        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=210,width=740,height=35)

        save_button=Button(button_frame,text="Save",command=self.add_data,width=19,bg="blue",fg="white",font=("times new roman",12,"bold"))
        save_button.grid(row=0,column=0)

        update_button=Button(button_frame,text="Update",command=self.update_data,width=20,bg="blue",fg="white",font=("times new roman",12,"bold"))
        update_button.grid(row=0,column=1)

        delete_button=Button(button_frame,text="Delete",command=self.delete_data,width=20,bg="blue",fg="white",font=("times new roman",12,"bold"))
        delete_button.grid(row=0,column=2)

        reset_button=Button(button_frame,text="Reset",command=self.Reset_data,width=20,bg="blue",fg="white",font=("times new roman",12,"bold"))
        reset_button.grid(row=0,column=3)

        button_frame2=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame2.place(x=0,y=245,width=740,height=70)

        take_photo_button=Button(button_frame2,command=self.generate_dataset,text="Take Photo Sample",width=40,bg="blue",fg="white",font=("times new roman",12,"bold"))
        take_photo_button.grid(row=0,column=0)
        update_photo_button=Button(button_frame2,text="Update photo Sample",width=40,bg="blue",fg="white",font=("times new roman",12,"bold"))
        update_photo_button.grid(row=0,column=1)




        

        # Right frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",13,"bold"),bg="white")
        Right_frame.place(x=780,y=10,width=680,height=580)

        # image on Right frame
        img_right=Image.open(r"C:\Users\ajgou\OneDrive\Pictures\Saved Pictures\students.jpeg")
        img_right=img_right.resize((670,130),Image.Resampling.LANCZOS)
        self.photo_right=ImageTk.PhotoImage(img_right)
        image_Label=Label(Right_frame,image=self.photo_right)
        image_Label.place(x=8,y=0,width=660,height=130)

        # Search System
        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",13,"bold"),bg="white")
        search_frame.place(x=8,y=140,width=660,height=70)

        search_lab=Label(search_frame,text=" Search : ",font=("times new roman",13,"bold"),bg="white")
        search_lab.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll no","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_button=Button(search_frame,text="Search",width=12,bg="blue",fg="white",font=("times new roman",12,"bold"))
        search_button.grid(row=0,column=3,padx=4)
        show_button=Button(search_frame,text="Show All",width=12,bg="blue",fg="white",font=("times new roman",12,"bold"))
        show_button.grid(row=0,column=4,padx=4)

        # ==============Table frame=============
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=8,y=210,width=660,height=340)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","division","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("division",text="Division")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ===============Function declaration=========
    
    # add data function
    def add_data(self):
        if self.var_dep.get()=="Select" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are mendatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_Recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_r1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student detail has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ============fetch data============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_Recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_detail")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    # ===========get_cursor===========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_r1.set(data[14])
        
    # Update data function
    def update_data(self):
        if self.var_dep.get()=="Select" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are mendatory",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_Recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_detail set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_r1.get(),self.var_std_id.get()))

                    
                    """sql="update student_detail set dep=%s,course=%s,year=%s,semester=%s,name=%s,div=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where Student_id=%s"

                    value=(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_r1.get(),self.var_std_id.get())

                    my_cursor.execute(sql,value)"""

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student detail successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # Delete Data function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_Recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student_detail where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # Reset Data function
    def Reset_data(self):
        self.var_dep.set("Select")
        self.var_course.set("Select")
        self.var_year.set("Select")
        self.var_semester.set("Select")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select")
        self.var_roll.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_r1.set("")

    #======generate dataset or Take photo Sample=======
    def generate_dataset(self):
        if self.var_dep.get()=="Select" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are mendatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_Recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_detail")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student_detail set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_r1.get(),self.var_std_id.get()==id+1))
                
                conn.commit()
                self.fetch_data()
                self.Reset_data()
                conn.close()

                # =========load predefined data face frontal ==============

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:  
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()