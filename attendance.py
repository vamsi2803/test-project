from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        #------Variables------
        self.var_atten_Id=StringVar()
        self.var_atten_Name=StringVar()
        self.var_atten_Dep=StringVar()
        self.var_atten_Date=StringVar()
        self.var_atten_Time=StringVar()
        self.var_atten_Attendance=StringVar()

        """ #first img
        img=Image.open(r"Images\cls.jpg")
        img=img.resize((700,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=700,height=200)

        
        #second img
        img1=Image.open(r"Images\grp.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)    

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=700,y=0,width=800,height=200)"""

        #bgimg
        bg=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\bgimg.png")
        bg=bg.resize((1366,768),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.bg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        #*************Left Image************
        left=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\re.jpg")
        left=left.resize((490,530),Image.ANTIALIAS)
        self.left=ImageTk.PhotoImage(left)

        left_img=Label(self.root,image=self.left)
        left_img.place(x=50,y=100,width=490,height=550)

        """main_frame=Frame(bg_img,bd=2,bg="blue")
        main_frame.place(x=5,y=50,width=1340,height=700)"""
        
       

        #Right label frame
        Right_frame=LabelFrame(self.root,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=550,y=100,width=750,height=550)

        table_frame=Frame( Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=740,height=520)  


        #*************Scroll Bar**************
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("Id","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X) #setting scroll on x axis
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Id",text="Student ID")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("Id",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        global mydata
        mydata.clear()
        with open("mouni.csv","r+",newline="\n") as f:
            csvread=csv.reader(f,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


      #**************Fetch Data*************
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    """def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)"""  

    #export csv
    def exportCsv(self): 
        try:
            if len(mydata)<1:
              messagebox.showerror("No Data","No Data found to export",parent=self.root)
              return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+ os.path.basename(fln) +"successfully")
        except Exception as es:
                 messagebox.showerror("Error",f"Due To:(str(es))",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_Id.set(rows[0])
        self.var_atten_Name.set(rows[1])
        self.var_atten_Dep.set(rows[2])
        self.var_atten_Date.set(rows[3])
        self.var_atten_Time.set(rows[4])
        self.var_atten_Attendance.set(rows[5])


    def reset_data(self):
        self.var_atten_Id.set("")
        self.var_atten_Name.set("")
        self.var_atten_Dep.set("")
        self.var_atten_Date.set("")
        self.var_atten_Time.set("")
        self.var_atten_Attendance.set("")

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()       