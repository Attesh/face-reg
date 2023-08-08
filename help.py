from tkinter import *
from tkinter import  ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#import pyodbc
import pandas as pd
import cv2
import datetime








class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # #title




 
 
        img_Top=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\H-2.jpg")
        img_Top=img_Top.resize((1620,1000),Image.ANTIALIAS)
        self.img_Top=ImageTk.PhotoImage(img_Top)

        F_timg_Top_lbl=Label(self.root,image=self.img_Top)
        F_timg_Top_lbl.place(x=0,y=0,width=1620,height=1000)


        title_lb1=Label(F_timg_Top_lbl,text="Help Center",font=("Raleway",35,'bold'),bg='navajo white',fg='light salmon')
        title_lb1.place(x=550,y=0,width=300,height=60)



        # main_frame=Frame(F_timg_Top_lbl,bd=2,bg="white")
        # main_frame.place(x=1100,y=0,width=600,height=1000)



#developer info
        dep_label=Label(F_timg_Top_lbl,text="Email:kingbalti00@gmail.com",font=("times new roman",12,'bold'),bg="white")

        dep_label.place(x=640,y=620)


if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
