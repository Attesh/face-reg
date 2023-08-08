from tkinter import *
from tkinter import  ttk
import face_recognition
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import xml.etree.ElementTree as ET
#import pyodbc
import pandas as pd
import cv2
import datetime
import os

import shelve






class TRAIN:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")




        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=60,width=1530,height=600)

        img_Top=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\E-4.jpg")
        img_Top=img_Top.resize((1920,1080),Image.ANTIALIAS)
        self.img_Top=ImageTk.PhotoImage(img_Top)
        F_timg_Top_lbl=Label(self.root,image=self.img_Top)
        F_timg_Top_lbl.place(x=0,y=0,width=1920,height=1080)

        #title
        title_lb1=Label(F_timg_Top_lbl,text="Encoding Data",font=("SimSun",25,'bold'),bg='black',fg='snow')
        title_lb1.place(x=550,y=0,width=300,height=60)

        b1_5=Button(F_timg_Top_lbl,text="Pair Matching",command=self.ENCODING,cursor="hand2",font=("SimSun",30,"bold"),bg="snow",fg="green")
        b1_5.place(x=550,y=380,width=400,height=60)


    def ENCODING(SELF):

        en=[]
        images=[]
        ids=[]
        #############Load image
        data_dir=(r"C:\Users\kingb\OneDrive\Desktop\vs python\Data")


        my_list=os.listdir(data_dir)
        print(my_list)
        for file in my_list:
                
            currentImg=cv2.imread(f'{data_dir}/{file}')#given array
            img= cv2.cvtColor(currentImg,cv2.COLOR_BGR2RGB)
            id=int(os.path.split(file)[1].split('.')[1])
            images.append(currentImg)
            ids.append(id)
        print(ids)   
        shF=shelve.open("ids")
        id_no=ids
        shF['ids']=ids
        shF.close()
            # cv2.imshow("webcam",currentImg)
            # cv2.waitKey(1)==13
        # ids=np.array(ids)

        def findEncodings(images):
            encodeList=[]
            for img in images:
                img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                encode=face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
                    
            return encodeList
        encodeListKnown=findEncodings(images)
        print(len(encodeListKnown))
        print(encodeListKnown)

        def create_encodeTxt():
            f=shelve.open("Encode")
            array=encodeListKnown
            f['array']=array
            f.close()
        create_encodeTxt()

        def create_idsTxt():
            i=shelve.open("ids")
            id_no=ids
            i['ids']=ids
            i.close()
        create_idsTxt()
        cv2.destroyAllWindows()
        print("encoding completed!")
        messagebox.showinfo("Encoding","Encoding Completed")
        

if __name__== "__main__":
    root=Tk()
    obj=TRAIN(root)
    root.mainloop()
