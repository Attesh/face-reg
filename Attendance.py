from tkinter import *
from tkinter import  ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#import pyodbc
import pandas as pd
import cv2
import datetime
import os
import csv
from tkinter import filedialog







mydata=[]
class Student_Attendance:
                
        def __init__(self, root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Face Recognition System")

                ################Variable##########################
                self.var_id=StringVar()
                self.var_std_name=StringVar()
                self.var_dep=StringVar()
                self.var_roll=StringVar()
                self.var_time=StringVar()

                self.var_date=StringVar()
                self.var_attendance=StringVar()


                smallimg=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\face\side.JFIF")
                smallimg=smallimg.resize((300,130),Image.ANTIALIAS)
                self.smallimg=ImageTk.PhotoImage(smallimg)


                F_lbl=Label(self.root,image=self.smallimg)
                F_lbl.place(x=-100,y=-60,width=500,height=250)

                #BG Image
                backg=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\face\IMG_7059.jpg")
                backg=backg.resize((1530,710),Image.ANTIALIAS)
                self.backg=ImageTk.PhotoImage(backg)
                bg_img=Label(self.root,image=self.backg)
                bg_img.place(x=0,y=130,width=1530,height=710)


                #title
                title_lb1=Label(bg_img,text="ATTENDANCE Management System",font=("Raleway",35,'bold'),bg='white',fg='red')
                title_lb1.place(x=0,y=0,width=1530,height=60)

                main_frame=Frame(bg_img,bd=2)
                main_frame.place(x=0,y=60,width=1530,height=600)

                #left
                left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Student_Attendance Details",font=("times new roman",12,'bold'))
                left_frame.place(x=0,y=-6,width=780,height=595)
                #image in Frame
                img_left=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\face\side.JFIF")
                img_left=img_left.resize((820,120),Image.ANTIALIAS)
                self.img_left=ImageTk.PhotoImage(img_left)
                F_left_lbl=Label(left_frame,image=self.img_left)
                F_left_lbl.place(x=0,y=0,width=820,height=120)

                        # #Class student information

                class_lbl=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,font=("times new roman",12,'bold'))
                class_lbl.place(x=0,y=240,width=775,height=330)
                #student id
                student_id_label=Label(class_lbl,text="STUDENT ID",font=("times new roman",12,'bold'),bg="white")

                student_id_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

                student_id_entry=ttk.Entry(class_lbl,width=20,textvariable=self.var_id,font=("time new roman",12,"bold"))
                student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
                #student Name
                student_Name_label=Label(class_lbl,text="STUDENT Name",font=("times new roman",12,'bold'),bg="white")

                student_Name_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

                student_name_entry=ttk.Entry(class_lbl,width=20,textvariable=self.var_std_name,font=("time new roman",12,"bold"))
                student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

                #student Department
                student_RollNo_label=Label(class_lbl,text="Department",font=("times new roman",12,'bold'),bg="white")

                student_RollNo_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

                student_roll_entry=ttk.Entry(class_lbl,width=20,textvariable=self.var_dep,font=("time new roman",12,"bold"))
                student_roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

                        #student Roll No
                student_RollNo_label=Label(class_lbl,text="STUDENT ROLL NO",font=("times new roman",12,'bold'),bg="white")

                student_RollNo_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

                student_roll_entry=ttk.Entry(class_lbl,width=20,textvariable=self.var_roll,font=("time new roman",12,"bold"))
                student_roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

                                #student Time
                student_time_label=Label(class_lbl,text="Time",font=("times new roman",12,'bold'),bg="white")

                student_time_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)

                student_time_entry=ttk.Entry(class_lbl,width=20,textvariable=self.var_time,font=("time new roman",12,"bold"))
                student_time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

                                #student Date
                student_Date_label=Label(class_lbl,text="Date",font=("times new roman",12,'bold'),bg="white")
                student_Date_label.grid(row=2,column=2,padx=2,pady=10,sticky=W)

                student_date_entry=ttk.Entry(class_lbl,width=20,textvariable=self.var_date,font=("time new roman",12,"bold"))
                student_date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

                        #student GEnder
                student_attend_label=Label(class_lbl,text="Student_Attendance",font=("times new roman",12,'bold'),bg="white")
                student_attend_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)

                # student_gen_entry=ttk.Entry(class_lbl,textvariable=self.var_gender,width=20,font=("time new roman",12,"bold"))
                # student_gen_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
                Attend_combo=ttk.Combobox(class_lbl,textvariable=self.var_attendance,font=("times new roman",8,"bold"),state="readonly",width=14)
                Attend_combo["values"]=("status","present","absent")
                Attend_combo.current(0)
                Attend_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)




                #Button label
                Button_lbl=Frame(class_lbl,bd=2,bg='white',relief=RIDGE)
                Button_lbl.place(x=0,y=245,width=770,height=35)

                Save_Button=Button(Button_lbl,text="Import csv",command=self.importCsv,width=20,font=("times new roman",12,'bold'),bg="white")

                Save_Button.grid(row=0,column=0)
                ##############
                UP_Button=Button(Button_lbl,text="Export csv",command=self.exportCSV,width=20,font=("times new roman",12,'bold'),bg="white")

                UP_Button.grid(row=0,column=1)
                ##################
                DEL_Button=Button(Button_lbl,text="Update",width=20,font=("times new roman",12,'bold'),bg="white")

                DEL_Button.grid(row=0,column=2)
                ###################
                RES_Button=Button(Button_lbl,text="RESET",command=self.Reset_data,width=20,font=("times new roman",12,'bold'),bg="white")

                RES_Button.grid(row=0,column=3)
                #Right
                right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Student_Attendance Details",font=("times new roman",12,'bold'))
                right_frame.place(x=780,y=10,width=690,height=580)


                #image in Frame
                img_right=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\face\side.JFIF")
                img_right=img_right.resize((820,120),Image.ANTIALIAS)
                self.img_right=ImageTk.PhotoImage(img_right)
                F_right_lbl=Label(right_frame,image=self.img_right)
                F_right_lbl.place(x=0,y=0,width=820,height=120)

        


                #table Frame
                Table_frame=Frame(right_frame,bd=2,bg='white',relief=RIDGE)
                Table_frame.place(x=5,y=240,width=680,height=320)

                Scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
                Scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

                self.AttendanceReportTable=ttk.Treeview(Table_frame,column=("id","name","roll","dep","time","date","attendance"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
                
                Scroll_x.pack(side=BOTTOM,fill=X)
                Scroll_y.pack(side=RIGHT,fill=Y)
                Scroll_x.config(command=self.AttendanceReportTable.xview)
                Scroll_y.config(command=self.AttendanceReportTable.yview)
                self.AttendanceReportTable.heading("id",text="StudentId")
                self.AttendanceReportTable.heading("roll",text="Roll_No")
                self.AttendanceReportTable.heading("name",text="Name")
                self.AttendanceReportTable.heading("dep",text="Department")

                
                
                

                self.AttendanceReportTable.heading("time",text="time")
                
                self.AttendanceReportTable.heading("date",text="Date")
                self.AttendanceReportTable.heading("attendance",text="Student_Attendance")

                self.AttendanceReportTable["show"]='headings'
        #===========================colum setting================
                self.AttendanceReportTable.column("id",width=80)
                self.AttendanceReportTable.column("roll",width=80)
                self.AttendanceReportTable.column("name",width=80)
                self.AttendanceReportTable.column("dep",width=80)


                
               
                
                

                self.AttendanceReportTable.column("time",width=80)

                self.AttendanceReportTable.column("date",width=80)

                self.AttendanceReportTable.column("attendance",width=80)



                self.AttendanceReportTable.pack(fill=BOTH,expand=1)

                self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
                #=========Fetch data============
        def fetchData(self,rows):
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in rows:

                        self.AttendanceReportTable.insert("",END,values=i)
        def importCsv(self):
                global mydata
                mydata.clear()
                fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln) as myfile:
                        csvread=csv.reader(myfile,delimiter=",")
                        for i in csvread:
                                mydata.append(i)
                        self.fetchData(mydata) 

        def exportCSV(self):
                try:
                        if len(mydata)<1:
                                messagebox.showerror("No Data","No data found to export",parent=root)
                                return False
                        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                        with open(fln,mode='w',newline="")as myfile:
                                exp_write=csv.writer(myfile,delimiter=",")
                                for i in mydata:
                                        exp_write.writerow(i)
                                messagebox.showinfo("Data Export","data export file"+os.path.basename(fln)+"successfully")

                except Exception as es:
                        messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)  


        def get_cursor(self,event=""):
                cursor_focus=self.AttendanceReportTable.focus()
                content=self.AttendanceReportTable.item(cursor_focus)
                data=content['values']

                self.var_id.set(data[0]),
                self.var_std_name.set(data[1]),
                self.var_dep.set(data[2]),
                self.var_roll.set(data[3]),
                self.var_time.set(data[4]),
                self.var_date.set(data[5]),
                self.var_attendance.set(data[6]),

               # ==================REset=============
        def Reset_data(self):
                self.var_id.set     ("")
                self.var_std_name.set  ("")
                self.var_roll.set    ("")
                self.var_dep.set ("")
                self.var_time.set      ("")
                self.var_date.set("")
                self.var_attendance.set     ("")


if __name__== "__main__":
    root=Tk()
    obj=Student_Attendance(root)
    root.mainloop()



