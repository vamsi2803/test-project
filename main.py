from tkinter import*
from tkinter import ttk 
import tkinter
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from attendance1 import Attendance1


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
       
      

       #background image
        img3=Image.open(r"Images\p1.jpg")
        img3=img3.resize((1366,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        #************Time**************88
        def time():
          string=strftime("%H:%M:%S %p")
          lbl.config(text=string)
          lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background="white",foreground="skyblue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()


       #student button
        img4=Image.open(r"Images\student.jpg")
        img4=img4.resize((200,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=150,width=200,height=170)

        b1_1=Button(bg_img,text="Student Registration",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=320,width=200,height=40)


        #Detect face button
        img5=Image.open(r"Images\fr.jpg")
        img5=img5.resize((200,170),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=550,y=150,width=200,height=170)

        b1_1=Button(bg_img,text="Take Attendance",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=550,y=320,width=200,height=40)


        
        #Attendance face button
        img6=Image.open(r"Images\note.png")
        img6=img6.resize((200,170),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b2.place(x=900,y=150,width=200,height=170)

        b1_1=Button(bg_img,text="Attendance Report",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=900,y=320,width=200,height=40)



        #train button
        img8=Image.open(r"Images\train.jpg")
        img8=img8.resize((200,170),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b2=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b2.place(x=200,y=430,width=200,height=170)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=600,width=200,height=40)


        #photos face button
        img9=Image.open(r"Images\db1.jpg")
        img9=img9.resize((200,170),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b2=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b2.place(x=550,y=430,width=200,height=170)

        b1_1=Button(bg_img,text="Dataset",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=550,y=600,width=200,height=40)



        #exit button
        img11=Image.open(r"Images\no.jpg")
        img11=img11.resize((200,170),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b2=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b2.place(x=900,y=430,width=200,height=170)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=900,y=600,width=200,height=40)

    def open_img(self):
          os.startfile("data")


    def iExit(self):
      self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this Project",parent=self.root)
      if self.iExit>0:
        self.root.destroy() 
      else:
        return       

      #***************Function buttons*****************
    
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)


    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Train(self.new_window)

    def face_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window) 

    def attendance_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window) 

    def developer_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Developer(self.new_window)  

    def help_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance1(self.new_window)       

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()



