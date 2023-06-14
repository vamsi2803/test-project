from tkinter import*
from tkinter import ttk 
import tkinter
from PIL import Image, ImageTk
import os
from attendance import Attendance



class Attendance1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        #background image
        img3=Image.open(r"Images\at.jpg")
        img3=img3.resize((1366,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        #attendance
        img6=Image.open(r"Images\note.png")
        img6=img6.resize((200,170),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2")
        #b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b2.place(x=450,y=400,width=200,height=170)

        b1_1=Button(bg_img,text="Attendance Report",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=450,y=570,width=200,height=40)


        #exit
        img11=Image.open(r"Images\no.jpg")
        img11=img11.resize((200,170),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b2=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b2.place(x=750,y=400,width=200,height=170)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=750,y=570,width=200,height=40)

        


    def iExit(self):
      self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this Project",parent=self.root)
      if self.iExit>0:
        self.root.destroy() 
      else:
        return  
    def attendance_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)   





if __name__=="__main__":
    root=Tk()
    obj=Attendance1(root)
    root.mainloop()          