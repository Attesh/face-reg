from tkinter import *
from tkinter import  ttk
import tkinter  as tk

import face_recognition
from PIL import Image,ImageTk
import numpy as np
from tkinter import messagebox
import mysql.connector
from numpy.core.fromnumeric import resize
#import pyodbc
import pandas as pd
import cv2
import datetime
import os
import train
import shelve
import itertools
from datetime import datetime

f=shelve.open('Encode')
c=f['array']
f.close()

i=shelve.open('ids')
e=i['ids']
i.close()


encodeListKnown=c
ids=e







class Face_R:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #title
        title_lb1=Label(self.root,text="Face Recoginition System",font=("Raleway",35,'bold'),bg='white',fg='red')
        title_lb1.place(x=0,y=0,width=1530,height=60)

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=60,width=1530,height=600)

        img_Top=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\F-2.jpg")
        img_Top=img_Top.resize((1528,800),Image.ANTIALIAS)
        self.img_Top=ImageTk.PhotoImage(img_Top)
        F_timg_Top_lbl=Label(self.root,image=self.img_Top)
        F_timg_Top_lbl.place(x=0,y=0,width=1528,height=800)





        img_Up=Image.open(r"C:\Users\kingb\OneDrive\Desktop\vs python\GUI\Gui_Image\F-3.jpg")
        img_Up=img_Up.resize((600,480),Image.ANTIALIAS)
        self.img_Up=ImageTk.PhotoImage(img_Up)
        F_timg_Up_lb2=Label(F_timg_Top_lbl,image=self.img_Up)
        F_timg_Up_lb2.place(x=1000,y=0,width=600,height=480)
    



        b1_5=Button(F_timg_Up_lb2,text=" Start ",command= self.camera,cursor="hand2",font=("Raleway",30,"bold"),bg="snow",fg="green")
        b1_5.place(x=-5,y=418,width=600,height=60)

        b1_5=Button(F_timg_Up_lb2,text="Press Enter To Stop ",cursor="hand2",font=("Raleway",30,"bold"),bg="snow",fg="green")
        b1_5.place(x=-5,y=359,width=600,height=60)


    
    def markAttendance(self,st_id,name,dep,roll):
        with open('Attendance.csv',"r+",newline="\n") as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry=line.split(',')
                nameList.append(entry[0])
            if ( (st_id not in nameList)and (name not in nameList)and (roll not in nameList)and (dep not in nameList)):
                now=datetime.now()
                ttstring=now.strftime('%H:%M:%S')
                dtstring=now.strftime('%d:%m:%y')
                f.writelines(f'\n{st_id},{name},{roll},{dep},{ttstring},{dtstring},present')
        
    def camera(self):
        cap =cv2.VideoCapture(0)


        while True:
            success ,img =cap.read()
            imgS=cv2.resize(img,(0,0),None,0.25,0.25)
            imgS= cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
            facesCurFrame=face_recognition.face_locations(imgS)
            encodesCurFrame=face_recognition.face_encodings(imgS,facesCurFrame)


            for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
                faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
                # print(matches)
                # # print(faceDis)
                matchIndex=np.argmin(faceDis)
                # print("matchIndex=",matchIndex)
                conn =mysql.connector.connect(
                    host="localhost",
                    user="root",
                        password="5264595Attesh",
                        database="face_recog")
                my_cursor=conn.cursor()
                my_cursor.execute("select Student_id from student ")
                i=my_cursor.fetchall()
                
                L=list(itertools.chain(*i))
                for i in range(len(L)):
                    if i==matchIndex:

                        my_cursor.execute("select Name from student ")
                        Na=my_cursor.fetchall()
                        # print(i)
                        id1=list(itertools.chain(*Na))  
                        # print(id1) 

                        my_cursor.execute("select Dep from student ")
                        dp=my_cursor.fetchall()
                        # print(i)
                        dep1=list(itertools.chain(*dp))  

                        my_cursor.execute("select Roll from student ")
                        RB=my_cursor.fetchall()
                        # print(i)
                        Roll1=list(itertools.chain(*RB))
                         

                
                
            
                if matches[matchIndex]:
                    name1=ids[matchIndex]
                    # print("name=",name1)
                    name=id1[name1] 
                    dep=dep1[name1]
                    roll=Roll1[name1] 
                    st_id=L[name1]

                    # print("Nmae=",name)

                    y1,x2,y2,x1=faceLoc
                    y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img,f"Name {name}",(x1,y2-6),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"CMS_id {roll}",(x1,y2+20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Student_id {st_id}",(x1,y2+40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department {dep}",(x1,y2+80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.markAttendance(st_id,name,dep,roll)
                    
                else:
                        name="unknow"
                        name not in id1[name1]
                        y1,x2,y2,x1=faceLoc
                        y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                        cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                                

                        

            cv2.imshow("webcam",img)
            if cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()







if __name__== "__main__":
    root=Tk()
    obj=Face_R(root)
    root.mainloop()
