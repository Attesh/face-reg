from tkinter import *
from tkinter import  ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#import pyodbc
import pandas as pd
import cv2
import datetime








class developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #title


        # main_frame=Frame(self.root,bd=2)
        # main_frame.place(x=0,y=60,width=1530,height=600)

 
 
        img_Top=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\D-1.jpg")
        img_Top=img_Top.resize((1530,820),Image.ANTIALIAS)
        self.img_Top=ImageTk.PhotoImage(img_Top)
        F_timg_Top_lbl=Label(self.root,image=self.img_Top)
        F_timg_Top_lbl.place(x=0,y=0,width=1530,height=820)





#developer info
        dep_label=Label(F_timg_Top_lbl,text=" Developer info\nName : zeeshan Ali\n i am full stack developer",font=("times new roman",12,'bold'),bg="white")

        dep_label.place(x=492,y=280,width=440,height=280)






if __name__== "__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()
