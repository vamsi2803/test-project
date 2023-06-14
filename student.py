from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        #**********variables declaration**********
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()


        #first img 
        img=Image.open(r"Images\grp.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)

      
      #second img
        img1=Image.open(r"Images\cls.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=500,height=130)

      #Third image
        img2=Image.open(r"Images\grp.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=130)


         #background image
        img3=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\bgimg.png")
        img3=img3.resize((1366,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1366,height=768)

        title_lbl=Label(bg_img,text="STUDENT DETAILS",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1350,height=700)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=700,height=550)

        img_left=Image.open(r"Images\clg1.jpg")
        img_left=img_left.resize((690,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=690,height=130)

       #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=690,height=120)

      #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,),state="read only")
        dep_combo["values"]=("Select Department","CSE","ECE","EEE","CIVIL","CHEMICAL","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

      # Course 
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,),state="read only")
        course_combo["values"]=("Select Course","B.TECH","M.TECH","MCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

      # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,),state="read only")
        year_combo["values"]=("Select Year","I YEAR","II YEAR","III YEAR","IV YEAR")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

       #Semester 
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=20,font=("times new roman",10,),state="read only")
        semester_combo["values"]=("Select Semester","I SEM","II SEM")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

      #Class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=260,width=690,height=330)
       
       #Student id
        studentId_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

       #Student Name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

       #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12))
        #gender_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,),state="readonly", width=24)
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


       #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12))
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

       #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12))
        email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

       #Phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12))
        phone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W) 

       #Radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

       
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1) 

       #Buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=685,height=80)    

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")   
        save_btn.grid(row=1,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")   
        update_btn.grid(row=1,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")   
        delete_btn.grid(row=1,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")   
        reset_btn.grid(row=1,column=3)

        #Button frame2
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=685,height=30)  

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=80,font=("times new roman",12,"bold"),bg="blue",fg="white")   
        take_photo_btn.grid(row=0,column=0)

       # update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=38,font=("times new roman",12,"bold"),bg="blue",fg="white")   
        #update_photo_btn.grid(row=0,column=1)

        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=720,y=10,width=610,height=550)

        img_right=Image.open(r"Images\clg1.jpg")
        img_right=img_right.resize((690,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=690,height=130)

        search_lbl=Label(Right_frame,text="REGISTERED STUDENTS",font=("times new roman",25,"bold"),bg="white",fg="purple")
        search_lbl.place(x=5,y=145,width=600,height=45)


        # ***********Search System***************
        """Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=600,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="pink")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,width=20,font=("times new roman",10,),state="read only")
        search_combo["values"]=("Select","Student Id","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W) 


        search_btn=Button(Search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")   
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(Search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")   
        showall_btn.grid(row=0,column=4,padx=4)"""

       #***************Table frame******************
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=600,height=300)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("Dept","Course","Year","Sem","Id","Name","Gender","DOB","Email ID","Phone No","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X) #setting scroll on x axis
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="Student Id")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email ID",text="Email ID")
        self.student_table.heading("Phone No",text="Phone No")
        
        self.student_table.heading("Photo",text="PhotoSampleStatus") 

        self.student_table["show"]="headings"

        self.student_table.column("Dept",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        
        self.student_table.column("Name",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email ID",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("Photo",width=150) 

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

     #********************function declaration*************    
    def add_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_radio1.get()

                                                                                               ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)         
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

       #**************fetch data***********
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="face_recognizer")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()
      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("",END,values=i)
        conn.commit()
      conn.close()  

     #**************get cursor*************
    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]

      self.var_dep.set(data[0]),
      self.var_course.set(data[1]),
      self.var_year.set(data[2]),
      self.var_semester.set(data[3]),  
      self.var_std_id.set(data[4]),
      self.var_std_name.set(data[5]),
      self.var_gender.set(data[6]),
      self.var_dob.set(data[7]),
      self.var_email.set(data[8]),
      self.var_phone.set(data[9]),
      self.var_radio1.set(data[10])

     #update function
    def update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
        try:
          Update=messagebox.askyesno("Update","Do you want to update this Student details",parent=self.root)
          if Update>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,PhotoSample=%s where Student_id=%s" ,(
                                                                                                                                                                 self.var_dep.get(),
                                                                                                                                                                 self.var_course.get(),
                                                                                                                                                                 self.var_year.get(),
                                                                                                                                                                 self.var_semester.get(),
                                                                                                                                                                 self.var_std_name.get(),
                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                 self.var_phone.get(),
                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                 self.var_std_id.get()
                                                                                                                                                                ))
          else:
            if not Update:
              return
          messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
          conn.commit()
          self.fetch_data()
          conn.close()
        except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

     #***********delete function******************8
    def delete_data(self):
      if self.var_std_id.get()=="":
        messagebox.showerror("Error","Student id must be required",parent=self.root)
      else:
        try:
          delete=messagebox.askyesno("Student Delete Page","Do you want to Delete this student",parent=self.root)
          if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="face_recognizer")
            my_cursor=conn.cursor()
            sql="delete from student where Student_id=%s"
            val=(self.var_std_id.get(),)
            my_cursor.execute(sql,val)
          else:
            if not delete:
              return
          conn.commit()
          self.fetch_data()
          conn.close()  
          messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     
    
     #**************Reset function************
    def reset_data(self):
      self.var_dep.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester")
      self.var_std_id.set("")
      self.var_std_name.set("")
      self.var_gender.set("Male")
      self.var_dob.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_radio1.set("")


      #*********Generate dataset or take photo Samples*********
    def generate_dataset(self):  
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
        try:
          conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from student")
          myresult=my_cursor.fetchall()
          id=0
          for x in myresult:
            id+=1
          my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,PhotoSample=%s where Student_id=%s" ,(
                                                                                                                                                                 self.var_dep.get(),
                                                                                                                                                                 self.var_course.get(),
                                                                                                                                                                 self.var_year.get(),
                                                                                                                                                                 self.var_semester.get(),
                                                                                                                                                                 self.var_std_name.get(),
                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                 self.var_phone.get(),
                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                 self.var_std_id.get()
                                                                                                                                                                ))
          conn.commit()
          self.fetch_data()
          self.reset_data()
          conn.close()

           #**************Load predefined data on face frontals from opencv**************
          face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
          
          def face_cropped(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.3,5)

            #scaling factor=1.3
            #Minimum neighbour=5

            for(x,y,w,h) in faces:
              face_cropped=img[y:y+h,x:x+w]
              return face_cropped
          cap=cv2.VideoCapture(0)
          img_id=0
          while True:
            ret,my_frame=cap.read()
            if face_cropped(my_frame) is not None:
              img_id+=1
              face=cv2.resize(face_cropped(my_frame),(450,450))
              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
              file_name_path="data/user."+str(id)+"."+str(img_id) +".jpg"
              cv2.imwrite(file_name_path,face)
              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
              cv2.imshow("Cropped Face", face)

            if cv2.waitKey(1)==13 or int(img_id)==100:
              break
          cap.release()
          cv2.destroyAllWindows()

          messagebox.showinfo("Result","Generating data sets completed!!!")  

        
        except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  



                                                                                                                                                                            
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()       