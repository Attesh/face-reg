from tkinter import *
import tkinter as ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import TRAIN

from face_recoginyion import Face_R
from Attendance import Student_Attendance
from developer import developer
from help import Help
import os
#import cv2
#import numpy as np
#import face_recognition
#import os
#from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title("face recognition system")
        #canvas.grid(columnspan=3)
        #########small image in side by side 
        smallimg=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\2im.JFIF")
        smallimg=smallimg.resize((510,300),Image.ANTIALIAS)
        self.smallimg=ImageTk.PhotoImage(smallimg)


        F_lbl=Label(self.root,image=self.smallimg)
        F_lbl.place(x=0,y=-60,width=510,height=300)
#2nd image
        smallimg2=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\1.JFIF")
        smallimg2=smallimg2.resize((510,300),Image.ANTIALIAS)
        self.smallimg2=ImageTk.PhotoImage(smallimg2)


        F_lb2=Label(self.root,image=self.smallimg2)
        F_lb2.place(x=500,y=-60,width=510,height=300)
#3rd image
        smallimg3=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\3.JFIF")
        smallimg3=smallimg3.resize((510,300),Image.ANTIALIAS)
        self.smallimg3=ImageTk.PhotoImage(smallimg3)


        F_lb3=Label(self.root,image=self.smallimg3)
        F_lb3.place(x=1000,y=-70,width=510,height=300)
        #BG Image 
        backg=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-G-1.jpg")
        backg=backg.resize((1530,710),Image.ANTIALIAS)
        self.backg=ImageTk.PhotoImage(backg)
        bg_img=Label(self.root,image=self.backg)
        bg_img.place(x=0,y=130,width=1530,height=710)


        #title
        title_lb1=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Symbol 8",35,'bold'),bg='snow',fg='black')
        title_lb1.place(x=0,y=0,width=1530,height=45)



        #Button 1
        but_img=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-1.png")
        but_img=but_img.resize((220,220),Image.ANTIALIAS)
        self.but_img=ImageTk.PhotoImage(but_img)

        b1=Button(bg_img,image=self.but_img,command=self.student_detail,cursor='hand2')
        b1.place(x=200,y=100,width=220,height=220)
        #command=student_detail
        b1_1=Button(bg_img,text="Student Detail",command=self.student_detail,cursor="hand2",font=("Raleway",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)


        #Button 2
        but_img1=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-2.png")
        but_img1=but_img1.resize((220,220),Image.ANTIALIAS)
        self.but_img1=ImageTk.PhotoImage(but_img1)

        b2=Button(bg_img,image=self.but_img1,cursor='hand2',command=self.student_Face_det)
        b2.place(x=500,y=100,width=220,height=220)

        b1_2=Button(bg_img,text="Face Detection",cursor="hand2",command=self.student_Face_det,font=("Raleway",15,"bold"),bg="white",fg="black")
        b1_2.place(x=500,y=300,width=220,height=40)


        #Button 3
        but_img2=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-3.JFIF")
        but_img2=but_img2.resize((220,220),Image.ANTIALIAS)
        self.but_img2=ImageTk.PhotoImage(but_img2)

        b3=Button(bg_img,image=self.but_img2,cursor='hand2',command=self.student_Attendance)
        b3.place(x=800,y=100,width=220,height=220)

        b1_3=Button(bg_img,text="Attendance ",cursor="hand2",command=self.student_Attendance,font=("Raleway",15,"bold"),bg="white",fg="black")
        b1_3.place(x=800,y=300,width=220,height=40)

        #Button 4
        but_img3=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-4.png")
        but_img3=but_img3.resize((220,220),Image.ANTIALIAS)
        self.but_img3=ImageTk.PhotoImage(but_img3)

        b4=Button(bg_img,image=self.but_img3,cursor='hand2',command=self.student_help)
        b4.place(x=1100,y=100,width=220,height=220)

        b1_4=Button(bg_img,text="Help Center ",cursor="hand2",command=self.student_help,font=("Raleway",15,"bold"),bg="white",fg="black")
        b1_4.place(x=1100,y=300,width=220,height=40)

        #Button 5
        but_img4=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-5.png")
        but_img4=but_img4.resize((220,220),Image.ANTIALIAS)
        self.but_img4=ImageTk.PhotoImage(but_img4)

        b5=Button(bg_img,image=self.but_img4,cursor='hand2',command=self.student_encode)
        b5.place(x=200,y=380,width=220,height=220)

        b1_5=Button(bg_img,text=" Encoding ",cursor="hand2",command=self.student_encode,font=("Raleway",15,"bold"),bg="white",fg="black")
        b1_5.place(x=200,y=580,width=220,height=40)


        #Button 6
        but_img5=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-6.JFIF")
        but_img5=but_img5.resize((220,220),Image.ANTIALIAS)
        self.but_img5=ImageTk.PhotoImage(but_img5)

        b6=Button(bg_img,image=self.but_img5,cursor='hand2',command=self.open_img,)
        b6.place(x=500,y=380,width=220,height=220)

        b1_6=Button(bg_img,text="Photos ",cursor="hand2",command=self.open_img,font=("Raleway",15,"bold"),bg="white",fg="black")
        b1_6.place(x=500,y=580,width=220,height=40)


        #Button 7
        but_img6=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-7.JFIF")
        but_img6=but_img6.resize((220,220),Image.ANTIALIAS)
        self.but_img6=ImageTk.PhotoImage(but_img6)

        b7=Button(bg_img,image=self.but_img6,cursor='hand2',command=self.student_dev)
        b7.place(x=800,y=380,width=220,height=220)

        b1_7=Button(bg_img,text="Develpoer ",cursor="hand2",command=self.student_dev,font=("Raleway",15,"bold"),bg="white",fg="black")
        b1_7.place(x=800,y=580,width=220,height=40)

        #Button 8
        but_img7=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\B-8.png")
        but_img7=but_img7.resize((220,220),Image.ANTIALIAS)
        self.but_img7=ImageTk.PhotoImage(but_img7)

        b8=Button(bg_img,image=self.but_img7,cursor='hand2',command=self.iExit)
        b8.place(x=1100,y=380,width=220,height=220)

        b1_8=Button(bg_img,text=" EXIT",cursor="hand2",command=self.iExit,font=("Raleway",15,"bold"),bg="white",fg="black")
        b1_8.place(x=1100,y=580,width=220,height=40)
    def open_img(self):
        os.startfile(r"C:\Users\kingb\OneDrive\Desktop\vs python\Data")
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def student_encode(self):
        self.new_window=Toplevel(self.root)
        self.app=TRAIN(self.new_window)
    def student_Face_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_R(self.new_window)
    def student_Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Attendance(self.new_window)

    def student_dev(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)

    def student_help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()       
