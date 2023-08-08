from tkinter import *
from tkinter import  ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#import pyodbc
import pandas as pd
import cv2
import datetime








class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        ################Variable##########################
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semster=StringVar()
        self.var_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        smallimg=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\S-1.JFIF")
        smallimg=smallimg.resize((500,250),Image.ANTIALIAS)
        self.smallimg=ImageTk.PhotoImage(smallimg)


        F_lbl=Label(self.root,image=self.smallimg)
        F_lbl.place(x=0,y=-60,width=500,height=250)


        smallimg1=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\S-2.JFIF")
        smallimg1=smallimg1.resize((500,250),Image.ANTIALIAS)
        self.smallimg1=ImageTk.PhotoImage(smallimg1)


        F_lbl=Label(self.root,image=self.smallimg1)
        F_lbl.place(x=500,y=-60,width=500,height=250)


        smallimg3=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\S-3.JFIF")
        smallimg3=smallimg3.resize((600,250),Image.ANTIALIAS)
        self.smallimg3=ImageTk.PhotoImage(smallimg3)


        F_lbl=Label(self.root,image=self.smallimg3)
        F_lbl.place(x=1000,y=-60,width=600,height=250)

        # BG Image
        backg=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-G-1.jpg")
        backg=backg.resize((1530,710),Image.ANTIALIAS)
        self.backg=ImageTk.PhotoImage(backg)
        bg_img=Label(self.root,image=self.backg)
        bg_img.place(x=0,y=130,width=1530,height=710)


        #title
        title_lb1=Label(self.root,text="Student Management System",font=("Comic Sans MS",35,'bold'),bg='snow',fg='black')
        title_lb1.place(x=0,y=130,width=1530,height=60)

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=200,width=1530,height=600)

        #left
        left_frame=LabelFrame(main_frame,bd=2,bg='white',text="Student Details",relief=RIDGE,font=("times new roman",12,'bold'))
        left_frame.place(x=0,y=-8,width=780,height=595)
        #image in Frame
        img_left=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\L_F_1.JFIF")
        img_left=img_left.resize((820,120),Image.ANTIALIAS)
        self.img_left=ImageTk.PhotoImage(img_left)
        F_left_lbl=Label(left_frame,image=self.img_left)
        F_left_lbl.place(x=0,y=0,width=820,height=120)


        #Current course information

        current_lbl=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text="Current Course",font=("times new roman",12,'bold'))
        current_lbl.place(x=5,y=120,width=770,height=120)

        #Department
        dep_label=Label(current_lbl,text="Department",font=("times new roman",12,'bold'),bg="white")

        dep_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        dep_box=ttk.Combobox(current_lbl,textvariable=self.var_dep, font=("times new roman",15,"bold"),state="readonly",width=17)
        dep_box["values"]=("Select Department","Computer","IT")
        dep_box.current(0)
        dep_box.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_lbl,text="Course",font=("times new roman",12,'bold'),bg="white")

        course_label.grid(row=0,column=2)

        dep_box=ttk.Combobox(current_lbl,textvariable=self.var_course,font=("times new roman",15,"bold"),state="readonly",width=17)
        dep_box["values"]=("Select Course","Bsc","IT")
        dep_box.current(0)
        dep_box.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #YEAR
        year_label=Label(current_lbl,text="YEAR",font=("times new roman",12,'bold'),bg="white")

        year_label.grid(row=1,column=0)

        dep_box=ttk.Combobox(current_lbl,textvariable=self.var_year,font=("times new roman",15,"bold"),state="readonly",width=17)
        dep_box["values"]=("Select Year","2017","2018")
        dep_box.current(0)
        dep_box.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #SEmster
        semster_label=Label(current_lbl,text="SEMESTER",font=("times new roman",12,'bold'),bg="white")

        semster_label.grid(row=1,column=2)

        dep_box=ttk.Combobox(current_lbl,textvariable=self.var_semster,font=("times new roman",15,"bold"),state="readonly",width=17)
        dep_box["values"]=("Select Semester","1","2")
        dep_box.current(0)
        dep_box.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #Class student information

        class_lbl=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text="Class Student Information",font=("times new roman",12,'bold'))
        class_lbl.place(x=0,y=240,width=775,height=330)
        #student id
        student_id_label=Label(class_lbl,text="ID_N0",font=("times new roman",12,'bold'),bg="white")

        student_id_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        student_id_entry=ttk.Entry(class_lbl,textvariable=self.var_id,width=20,font=("time new roman",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #student Name
        student_Name_label=Label(class_lbl,text=" Name",font=("times new roman",12,'bold'),bg="white")

        student_Name_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        student_name_entry=ttk.Entry(class_lbl,textvariable=self.var_std_name,width=20,font=("time new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #student class division
        student_div_label=Label(class_lbl,text=" Division",font=("times new roman",12,'bold'),bg="white")

        student_div_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        # student_div_entry=ttk.Entry(class_lbl,textvariable=self.var_div,width=20,font=("time new roman",12,"bold"))
        # student_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_lbl,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=20)
        div_combo["values"]=("A","B","C","D","E")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        #student Roll No
        student_RollNo_label=Label(class_lbl,text=" ROLL NO",font=("times new roman",12,'bold'),bg="white")

        student_RollNo_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        student_roll_entry=ttk.Entry(class_lbl,textvariable=self.var_roll,width=20,font=("time new roman",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #student GEnder
        student_gen_label=Label(class_lbl,text="Gender",font=("times new roman",12,'bold'),bg="white")

        student_gen_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        # student_gen_entry=ttk.Entry(class_lbl,textvariable=self.var_gender,width=20,font=("time new roman",12,"bold"))
        # student_gen_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gen_combo=ttk.Combobox(class_lbl,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gen_combo["values"]=("Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        #student DOB
        
        student_DOB_label=Label(class_lbl,text="DOB",font=("times new roman",12,'bold'),bg="white")

        student_DOB_label.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        student_dob_entry=ttk.Entry(class_lbl,textvariable=self.var_dob,width=20,font=("time new roman",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #student phone no
        student_phone_label=Label(class_lbl,text=" Phone No",font=("times new roman",12,'bold'),bg="white")

        student_phone_label.grid(row=3,column=2,padx=2,pady=10,sticky=W)

        student_Phone_entry=ttk.Entry(class_lbl,textvariable=self.var_phone,width=20,font=("time new roman",12,"bold"))
        student_Phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #student Address
        student_Adrre_label=Label(class_lbl,text=" Address",font=("times new roman",12,'bold'),bg="white")

        student_Adrre_label.grid(row=4,column=0,padx=2,pady=10,sticky=W)

        student_Addr_entry=ttk.Entry(class_lbl,textvariable=self.var_address,width=20,font=("time new roman",12,"bold"))
        student_Addr_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        T_name_label=Label(class_lbl,text="Teacher Name",font=("times new roman",12,'bold'),bg="white")

        T_name_label.grid(row=4,column=2,padx=2,pady=10,sticky=W)

        T_Name_entry=ttk.Entry(class_lbl,textvariable=self.var_teacher,width=20,font=("time new roman",12,"bold"))
        T_Name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #student Email
        student_Email_label=Label(class_lbl,text=" Email",font=("times new roman",12,'bold'),bg="white")

        student_Email_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)

        student_email_entry=ttk.Entry(class_lbl,textvariable=self.var_email,width=20,font=("time new roman",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)



        #radio Buttons
        self.var_radio1=StringVar()

        radiobtn1=ttk.Radiobutton(class_lbl,variable=self.var_radio1,text="Take Photo Sample",command=self.sel,value="Yes")
        radiobtn1.grid(row=6,column=0)
        radiobtn2=ttk.Radiobutton(class_lbl,variable=self.var_radio1,text="No Photo Sample",command=self.sel,value="No")
        radiobtn2.grid(row=6,column=1)
        #Button Frame
        Button_lbl=Frame(class_lbl,bd=2,bg='white',relief=RIDGE)
        Button_lbl.place(x=0,y=245,width=770,height=35)


        Save_Button=Button(Button_lbl,text="Save",command=self.add_data,width=20,font=("times new roman",12,'bold'),bg="white")

        Save_Button.grid(row=0,column=0)
        ###############
        UP_Button=Button(Button_lbl,text="UPDATE",command=self.update_data,width=20,font=("times new roman",12,'bold'),bg="white")

        UP_Button.grid(row=0,column=1)
        ##################
        DEL_Button=Button(Button_lbl,text="DELETE",command=self.delete_data,width=20,font=("times new roman",12,'bold'),bg="white")

        DEL_Button.grid(row=0,column=2)
        ###################
        RES_Button=Button(Button_lbl,text="RESET",command=self.Reset_data,width=20,font=("times new roman",12,'bold'),bg="white")

        RES_Button.grid(row=0,column=3)


        #FRAME TAKE PHOTE
        Taken_Button_lbl=Frame(class_lbl,bd=2,bg='white',relief=RIDGE)
        Taken_Button_lbl.place(x=0,y=280,width=770,height=20)
        ##################
        TAKE_photo_Button=Button(Taken_Button_lbl,text="TAKE PHOTO SAMPLE",command=self.generate_data_set,width=120,font=("times new roman",8,'bold'),bg="white")

        TAKE_photo_Button.grid(row=0,column=0)


        #Right
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Details",font=("times new roman",12,'bold'))
        right_frame.place(x=780,y=-8,width=790,height=580)


        #image in Frame
        img_right=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\R-F-1.JFIF")
        img_right=img_right.resize((820,120),Image.ANTIALIAS)
        self.img_right=ImageTk.PhotoImage(img_right)
        F_right_lbl=Label(right_frame,image=self.img_right)
        F_right_lbl.place(x=0,y=0,width=820,height=120)

        ##==================search=====================


        #Class student information

        search_lbl=LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE,text="Search System",font=("times new roman",12,'bold'))
        search_lbl.place(x=0,y=120,width=780,height=120)

        student_search_label=Label(search_lbl,text="Search By:",font=("times new roman",12,'bold'),bg="white")

        student_search_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)


        search_box=ttk.Combobox(search_lbl,font=("times new roman",12,"bold"),state="readonly",width=20)
        search_box["values"]=("Select Semester","Roll_No","Phone_No")
        search_box.current(0)
        search_box.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_lbl,width=20,font=("time new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_Button=Button(search_lbl,text="Search",width=14,font=("times new roman",10,'bold'),bg="white")

        search_Button.grid(row=0,column=3,padx=5)

        show_all_Button=Button(search_lbl,text="Show_All",width=14,font=("times new roman",10,'bold'),bg="white")

        show_all_Button.grid(row=0,column=4,padx=5)


        #table Frame
        Table_frame=Frame(right_frame,bd=2,bg='white',relief=RIDGE)
        Table_frame.place(x=5,y=240,width=780,height=320)

        Scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.STUDENT_TABLE=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.STUDENT_TABLE.xview)
        Scroll_y.config(command=self.STUDENT_TABLE.yview)

        self.STUDENT_TABLE.heading("dep",text="Department")
        self.STUDENT_TABLE.heading("course",text="Course")
        self.STUDENT_TABLE.heading("year",text="Year")
        self.STUDENT_TABLE.heading("sem",text="Semester")
        self.STUDENT_TABLE.heading("id",text="StudentId")
        self.STUDENT_TABLE.heading("name",text="Name")
        

        self.STUDENT_TABLE.heading("div",text="Division")
        self.STUDENT_TABLE.heading("roll",text="Roll_No")
        self.STUDENT_TABLE.heading("gender",text="Gender")
        self.STUDENT_TABLE.heading("dob",text="DOB")
        self.STUDENT_TABLE.heading("email",text="Email")
        self.STUDENT_TABLE.heading("phone",text="Phone")
        self.STUDENT_TABLE.heading("address",text="Address")
        self.STUDENT_TABLE.heading("teacher",text="Teacher")
        self.STUDENT_TABLE.heading("photo",text="PhotoSampleStatus")
        self.STUDENT_TABLE["show"]='headings'
#===========================colum setting================

        self.STUDENT_TABLE.column("dep",width=80)
        self.STUDENT_TABLE.column("course",width=80)

        self.STUDENT_TABLE.column("year",width=80)
        self.STUDENT_TABLE.column("sem",width=80)

        self.STUDENT_TABLE.column("id",width=80)
        self.STUDENT_TABLE.column("name",width=80)

        self.STUDENT_TABLE.column("roll",width=80)

        self.STUDENT_TABLE.column("gender",width=80)

        self.STUDENT_TABLE.column("div",width=80)

        self.STUDENT_TABLE.column("dob",width=80)

        self.STUDENT_TABLE.column("email",width=80)
        self.STUDENT_TABLE.column("phone",width=80)
        self.STUDENT_TABLE.column("address",width=80)
        self.STUDENT_TABLE.column("teacher",width=80)
        self.STUDENT_TABLE.column("photo",width=80)

        self.STUDENT_TABLE.pack(fill=BOTH,expand=1)
        self.STUDENT_TABLE.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ================function declaration=========kkkkkkkKK

    def add_data(self):

        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:

                conn =mysql.connector.connect(
                host="localhost",
                user="root",
                password="5264595Attesh",
                database="face_recog"
)
                # pyodbc.connect('Driver={SQL Server};'
                #       'Server=DESKTOP-RK91D5E;'
                #       'Database=FaceRecoginition;'
                #       'Trusted_Connection=yes;')
                my_cursur=conn.cursor()
                my_cursur.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )", (
                                                                                                                                    self.var_dep.get()       ,  
                                                                                                                                    self.var_course.get()    ,
                                                                                                                                    self.var_year.get()      ,
                                                                                                                                    self.var_semster.get()   ,                          
                                                                                                                                    self.var_id.get()          ,
                                                                                                                                    self.var_std_name.get()  ,
                                                                                                                                    self.var_div.get()          ,
                                                                                                                                    self.var_roll.get()         ,
                                                                                                                                    self.var_gender.get()     , 
                                                                                                                                    self.var_dob.get()        ,
                                                                                                                                    self.var_email.get()        , 
                                                                                                                                    self.var_phone.get()         ,
                                                                                                                                    self.var_address.get()      , 
                                                                                                                                    self.var_teacher.get()     ,
                                                                                                                                    self.var_radio1.get()
               ))

            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","done")
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)    



    # =====================Fetch database=====================
    def fetch_data(self):

        conn =mysql.connector.connect(
        host="localhost",
        user="root",
        password="5264595Attesh",
        database="face_recog")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from Student")
        data=my_cursur.fetchall()

        if len(data)!=0:
            self.STUDENT_TABLE.delete(* self.STUDENT_TABLE.get_children())
            for i in data:
                self.STUDENT_TABLE.insert("" ,END,values=i)
            conn.commit()
        conn.close()

#=========================get cursor========================

    def get_cursor(self,event=""):
        cursor_focus=self.STUDENT_TABLE.focus()
        content=self.STUDENT_TABLE.item(cursor_focus)
        data=content['values']

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semster.set(data[3]),
        self.var_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ++++++++++==========Updated+++++++++===========

    def update_data(self):


        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:

                Update=messagebox.askyesno("Upadte","Do you want to update this student detail",parent=self.root)
                if Update > 0:
                
                    conn =mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="5264595Attesh",
                    database="face_recog",
                    charset='utf8')
                    my_cursur=conn.cursor()
                    my_cursur.execute("Update student set  Dep = %s, course =%s, Year =%s, Semester=%s, Name = %s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id = %s" ,
                        (                                                                                                                                         
                    self.var_dep.get()   ,                                                                                                                                                                                                
                    self.var_course.get()    ,
                    self.var_year.get()      ,
                    self.var_semster.get()   ,                          
                    self.var_std_name.get()  ,
                    
                    self.var_div.get()          ,
                    self.var_roll.get()         ,
                    self.var_gender.get()     , 
                    self.var_dob.get()        ,
                    self.var_email.get()        , 
                    self.var_phone.get()         ,
                    self.var_address.get()      , 
                    self.var_teacher.get()     ,
                    self.var_radio1.get()       ,
                    self.var_id.get()    )   )                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Sucess","Student details successfully updated completed",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)       
#===================delete function======================================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required ",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete > 0:
                    conn =mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="5264595Attesh",
                    database="face_recog")
                    my_cursur=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursur.execute(sql,val)
                else:
                    if not delete:
                        return
 
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student details successfully Deleted completed",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

               # ==================REset=============
    def Reset_data(self):
        self.var_dep.set     ("Select Department")
        self.var_course.set  ("Select Course")
        self.var_year.set    ("Select Year")
        self.var_semster.set ("Select Semester")
        self.var_id.set      ("")
        self.var_std_name.set("")
        self.var_div.set     ("Select Division")
        self.var_roll.set    ("")
        self.var_gender.set  ("Select Male")
        self.var_dob.set     ("")
        self.var_email.set   ("")
        self.var_phone.set   ("")
        self.var_address.set ("")
        self.var_teacher.set ("")
        self.var_radio1.set  ("")

    def generate_data_set(self):

        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn =mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="5264595Attesh",
                    database="face_recog"
                    )
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+= 1

                my_cursor.execute("""Update student set Name = %s, Dep = %s, course =%s, Year =%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id = %s""" ,
                                                                                                                                                                                                                                                (                                                                                                                                        
                                                                                                                                                                                                                                        self.var_dep.get()   ,                                                                                                                                                                                                
                                                                                                                                                                                                                                        self.var_course.get()    ,
                                                                                                                                                                                                                                        self.var_year.get()      ,
                                                                                                                                                                                                                                        self.var_semster.get()   ,                          
                                                                                                                                                                                                                                        self.var_std_name.get()  ,
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                        self.var_div.get()          ,
                                                                                                                                                                                                                                        self.var_roll.get()         ,
                                                                                                                                                                                                                                        self.var_gender.get()     , 
                                                                                                                                                                                                                                        self.var_dob.get()        ,
                                                                                                                                                                                                                                        self.var_email.get()        , 
                                                                                                                                                                                                                                        self.var_phone.get()         ,
                                                                                                                                                                                                                                        self.var_address.get()      , 
                                                                                                                                                                                                                                        self.var_teacher.get()     ,
                                                                                                                                                                                                                                        self.var_radio1.get()       ,
                                                                                                                                                                                                                                        self.var_id.get()==id+1                                                                               
                                                                                                                                                                                                                                                ))                                                                                                                                                                 
                
                conn.commit()
                self.fetch_data()
                self.Reset_data()
                conn.close()
                face_classifier=cv2.CascadeClassifier(r"C:\Users\kingb\OneDrive\Desktop\vs python\PythonApplication1\cascades\data\haarcascade_frontalface_default.xml")
                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop
                cap=cv2.VideoCapture(0)
                img_id=0
                
                while True:
                    ret,my_frame=cap.read()
                    if face_crop(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_crop(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        
                        file_name_path="C:\\Users\\kingb\\OneDrive\\Desktop\\vs python\\Data\\pic."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("crop face",face)
                    # for x in my_result:
                    #     id+=1
                    if cv2.waitKey(1)==13 or int(img_id)==1:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","image captured!!")   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  


    def sel(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:

                Update=1
                if Update > 0:       
        
                
                    conn =mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="5264595Attesh",
                    database="face_recog",
                    charset='utf8')
                    my_cursur=conn.cursor()
                    my_cursur.execute("""Update student set  PhotoSample=%s where Student_id = %s""" ,
                        (                                                                                                                                         
              
                    self.var_radio1.get()       ,
                    self.var_id.get()    )   )                                                                        
                                                                                                                                                                                                        
                                                                                                                                                             
                else:
                    if  not Update:
                        return
                # messagebox.showinfo("Sucess","Student details successfully updated completed",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)











if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()



