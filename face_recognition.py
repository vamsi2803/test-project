from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="TAKE ATTENDANCE",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1366,height=45)

         #1st image
        """img_top=Image.open(r"Images\train.jpg")
        img_top=img_top.resize((600,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=600,height=700)"""


        #2nd image
        img_bottom=Image.open(r"Images\face_recognition.jpg")
        img_bottom=img_bottom.resize((900,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=55,width=1366,height=700)

        #Button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=580,y=620,width=200,height=40)

    #****************** Mark Attendance******************
    def mark_attendance(self,r,n,d):
        with open("mouni.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))  
                name_list.append(entry[0])
            
            if((r not in name_list) and  (n not in name_list)  and  (d not in name_list)):
            # if entry[0]==r and entry[4].strip()==datetime.now().strftime("%d/%m/%y"):
                #return
                with open('mouni.csv','a+',newline='\n') as f:
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")



    #***************Face recognition***************

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            coords=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))

                conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n=str(n)
                n=n.replace('(','').replace("'",'').replace("'",'').replace(')','').replace(',','')
                #n="+".join(str(n))
                #separator=""
                #n=separator.join(str(x) for x in n)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r=str(r)
                r=r.replace('(','').replace("'",'').replace("'",'').replace(')','').replace(',','')
                #r="+".join(str(r))

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d=str(d)
                d=d.replace('(','').replace("'",'').replace("'",'').replace(',','').replace(')','')
                #d="+".join(str(d))


                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(r,n,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coords=[x,y,w,h]

            return coords 

        def recognize(img,clf,faceCascade):
            coords=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf) 
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
       # clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0) #0 for pc cam if external cam we use 1

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



   




if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()                  